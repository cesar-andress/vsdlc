"""Learned metadata-only baselines for contamination classification."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Protocol

import numpy as np
from scipy.sparse import hstack
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

from vsdlc_mining.decontamination_schema import BINARY_DECONTAMINATION_LABELS, PRIMARY_LABELS
from vsdlc_mining.metadata_features import (
    NUMERIC_FEATURE_NAMES,
    collapse_binary_decontamination,
    rows_to_feature_records,
)

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


class RowEstimator(Protocol):
    def fit(self, rows: list[dict[str, str]], y: list[str]) -> "RowEstimator": ...

    def predict(self, rows: list[dict[str, str]]) -> list[str]: ...


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _resolve_reference_label(row: dict[str, str], *, field: str) -> str:
    return (row.get(field) or "").strip().upper()


def merge_metadata_with_labels(
    metadata_rows: list[dict[str, str]],
    label_rows: list[dict[str, str]],
    *,
    label_field: str = "majority_label",
) -> list[dict[str, str]]:
    label_by_repo = {
        (row.get("repo_full_name") or "").strip(): row
        for row in label_rows
        if row.get("repo_full_name")
    }
    merged: list[dict[str, str]] = []
    for row in metadata_rows:
        repo = (row.get("repo_full_name") or "").strip()
        if not repo or repo not in label_by_repo:
            continue
        label = _resolve_reference_label(label_by_repo[repo], field=label_field)
        if not label:
            continue
        merged_row = dict(row)
        merged_row[label_field] = label
        merged.append(merged_row)
    return merged


def _feature_matrix(rows: list[dict[str, str]]) -> tuple[list[str], np.ndarray]:
    records = rows_to_feature_records(rows)
    numeric = np.asarray(records["numeric"], dtype=float)
    return records["documents"], numeric


class TfidfLogisticEstimator:
    def __init__(self) -> None:
        self._tfidf = TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_features=5000)
        self._scaler = StandardScaler()
        self._clf = LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42)

    def fit(self, rows: list[dict[str, str]], y: list[str]) -> "TfidfLogisticEstimator":
        documents, numeric = _feature_matrix(rows)
        text_features = self._tfidf.fit_transform(documents)
        numeric_features = self._scaler.fit_transform(numeric)
        features = hstack([text_features, numeric_features])
        self._clf.fit(features, y)
        return self

    def predict(self, rows: list[dict[str, str]]) -> list[str]:
        documents, numeric = _feature_matrix(rows)
        text_features = self._tfidf.transform(documents)
        numeric_features = self._scaler.transform(numeric)
        features = hstack([text_features, numeric_features])
        return [str(label) for label in self._clf.predict(features)]


class TfidfRandomForestEstimator:
    def __init__(self) -> None:
        self._tfidf = TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_features=5000)
        self._scaler = StandardScaler()
        self._clf = RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced_subsample",
            random_state=42,
            n_jobs=1,
        )

    def fit(self, rows: list[dict[str, str]], y: list[str]) -> "TfidfRandomForestEstimator":
        documents, numeric = _feature_matrix(rows)
        text_features = self._tfidf.fit_transform(documents)
        numeric_features = self._scaler.fit_transform(numeric)
        features = hstack([text_features, numeric_features])
        self._clf.fit(features, y)
        return self

    def predict(self, rows: list[dict[str, str]]) -> list[str]:
        documents, numeric = _feature_matrix(rows)
        text_features = self._tfidf.transform(documents)
        numeric_features = self._scaler.transform(numeric)
        features = hstack([text_features, numeric_features])
        return [str(label) for label in self._clf.predict(features)]


class EmbeddingLogisticEstimator:
    def __init__(self, *, model_name: str = EMBEDDING_MODEL_NAME) -> None:
        self.model_name = model_name
        self._encoder = None
        self._scaler = StandardScaler()
        self._clf = LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42)

    def _ensure_encoder(self) -> Any:
        if self._encoder is None:
            from sentence_transformers import SentenceTransformer

            self._encoder = SentenceTransformer(self.model_name)
        return self._encoder

    def fit(self, rows: list[dict[str, str]], y: list[str]) -> "EmbeddingLogisticEstimator":
        encoder = self._ensure_encoder()
        documents, numeric = _feature_matrix(rows)
        text_embeddings = encoder.encode(documents, show_progress_bar=False)
        numeric_scaled = self._scaler.fit_transform(numeric)
        features = np.hstack([text_embeddings, numeric_scaled])
        self._clf.fit(features, y)
        return self

    def predict(self, rows: list[dict[str, str]]) -> list[str]:
        encoder = self._ensure_encoder()
        documents, numeric = _feature_matrix(rows)
        text_embeddings = encoder.encode(documents, show_progress_bar=False)
        numeric_scaled = self._scaler.transform(numeric)
        features = np.hstack([text_embeddings, numeric_scaled])
        return [str(label) for label in self._clf.predict(features)]


def _summary_metrics(y_true: list[str], y_pred: list[str], labels: tuple[str, ...]) -> dict[str, Any]:
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_macro": precision_score(y_true, y_pred, labels=list(labels), average="macro", zero_division=0),
        "recall_macro": recall_score(y_true, y_pred, labels=list(labels), average="macro", zero_division=0),
        "f1_macro": f1_score(y_true, y_pred, labels=list(labels), average="macro", zero_division=0),
        "precision_weighted": precision_score(
            y_true, y_pred, labels=list(labels), average="weighted", zero_division=0
        ),
        "recall_weighted": recall_score(y_true, y_pred, labels=list(labels), average="weighted", zero_division=0),
        "f1_weighted": f1_score(y_true, y_pred, labels=list(labels), average="weighted", zero_division=0),
        "classification_report": classification_report(
            y_true,
            y_pred,
            labels=list(labels),
            output_dict=True,
            zero_division=0,
        ),
        "label_distribution_true": dict(Counter(y_true)),
        "label_distribution_pred": dict(Counter(y_pred)),
    }


def _cross_validated_predictions(
    rows: list[dict[str, str]],
    labels: list[str],
    *,
    estimator_factory: Callable[[], RowEstimator],
    n_splits: int,
    random_state: int,
) -> list[str]:
    splitter = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    y_pred = [""] * len(rows)
    indices = np.arange(len(rows))

    for train_idx, test_idx in splitter.split(indices, labels):
        train_rows = [rows[i] for i in train_idx]
        train_labels = [labels[i] for i in train_idx]
        test_rows = [rows[i] for i in test_idx]
        estimator = estimator_factory()
        estimator.fit(train_rows, train_labels)
        predictions = estimator.predict(test_rows)
        for position, prediction in zip(test_idx, predictions):
            y_pred[position] = prediction
    return y_pred


def _failure_analysis(
    rows: list[dict[str, str]],
    y_true: list[str],
    predictions_by_model: dict[str, list[str]],
) -> dict[str, Any]:
    repos = [row.get("repo_full_name", "") for row in rows]
    all_wrong = []
    exclude_errors: Counter[tuple[str, str]] = Counter()
    for index, repo in enumerate(repos):
        true_label = y_true[index]
        wrong_models = [
            model_name
            for model_name, preds in predictions_by_model.items()
            if preds[index] != true_label
        ]
        if len(wrong_models) == len(predictions_by_model):
            all_wrong.append(
                {
                    "repo_full_name": repo,
                    "true_label": true_label,
                    "predictions": {name: predictions_by_model[name][index] for name in predictions_by_model},
                    "github_description": (rows[index].get("github_description") or "")[:160],
                }
            )
        for model_name, preds in predictions_by_model.items():
            pred = preds[index]
            if true_label == "EXCLUDE" or pred == "EXCLUDE":
                exclude_errors[(true_label, pred)] += 1

    return {
        "all_models_wrong_count": len(all_wrong),
        "all_models_wrong_examples": all_wrong[:12],
        "exclude_involving_errors": {f"{true}->{pred}": count for (true, pred), count in exclude_errors.items()},
    }


def evaluate_task(
    rows: list[dict[str, str]],
    *,
    label_field: str,
    label_transform: Callable[[str], str] | None,
    categories: tuple[str, ...],
    n_splits: int,
    random_state: int,
    include_embeddings: bool,
) -> dict[str, Any]:
    filtered_rows: list[dict[str, str]] = []
    labels: list[str] = []
    for row in rows:
        raw_label = _resolve_reference_label(row, field=label_field)
        if label_transform is not None:
            mapped = label_transform(raw_label)
            if not mapped:
                continue
            raw_label = mapped
        if raw_label not in categories:
            continue
        filtered_rows.append(row)
        labels.append(raw_label)

    model_factories: dict[str, Callable[[], RowEstimator]] = {
        "tfidf_logistic_regression": TfidfLogisticEstimator,
        "tfidf_random_forest": TfidfRandomForestEstimator,
    }
    if include_embeddings:
        model_factories["sentence_embedding_logistic_regression"] = EmbeddingLogisticEstimator

    predictions_by_model: dict[str, list[str]] = {}
    model_results: dict[str, Any] = {}
    for model_name, factory in model_factories.items():
        y_pred = _cross_validated_predictions(
            filtered_rows,
            labels,
            estimator_factory=factory,
            n_splits=n_splits,
            random_state=random_state,
        )
        predictions_by_model[model_name] = y_pred
        model_results[model_name] = _summary_metrics(labels, y_pred, categories)

    return {
        "n_repositories": len(filtered_rows),
        "label_field": label_field,
        "categories": list(categories),
        "numeric_feature_names": list(NUMERIC_FEATURE_NAMES),
        "metadata_text_fields": [
            "repo_full_name",
            "github_description",
            "github_topics",
            "primary_language",
            "ci_evidence",
            "release_evidence",
            "sample_stratum",
            "detected_instruction_artifacts",
        ],
        "models": model_results,
        "failure_analysis": _failure_analysis(filtered_rows, labels, predictions_by_model),
    }


def run_learned_baseline_evaluation(
    metadata_path: Path,
    labels_path: Path,
    *,
    label_field: str = "majority_label",
    n_splits: int = 5,
    random_state: int = 42,
    include_embeddings: bool = True,
) -> dict[str, Any]:
    metadata_rows = _read_rows(metadata_path)
    label_rows = _read_rows(labels_path)
    merged_rows = merge_metadata_with_labels(metadata_rows, label_rows, label_field=label_field)

    three_class = evaluate_task(
        merged_rows,
        label_field=label_field,
        label_transform=None,
        categories=PRIMARY_LABELS,
        n_splits=n_splits,
        random_state=random_state,
        include_embeddings=include_embeddings,
    )
    binary = evaluate_task(
        merged_rows,
        label_field=label_field,
        label_transform=collapse_binary_decontamination,
        categories=BINARY_DECONTAMINATION_LABELS,
        n_splits=n_splits,
        random_state=random_state,
        include_embeddings=include_embeddings,
    )

    return {
        "schema_version": "0.2",
        "metadata_file": str(metadata_path),
        "labels_file": str(labels_path),
        "label_field": label_field,
        "evaluation": {
            "method": "stratified_k_fold_cross_validation",
            "n_splits": n_splits,
            "random_state": random_state,
            "features": "metadata-visible fields only (no labels, no functional inspection)",
            "embedding_model": EMBEDDING_MODEL_NAME if include_embeddings else None,
        },
        "three_class": three_class,
        "binary_contamination": binary,
    }
