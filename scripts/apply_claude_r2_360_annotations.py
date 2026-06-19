#!/usr/bin/env python3
"""Build gold_sample_360_pilot.csv and claude_r2 patch from batch files + annotations."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.gold_sample import GOLD_SAMPLE_FIELDS, eligible_to_gold_row  # noqa: E402
from vsdlc_mining.models import EligibleRepo  # noqa: E402
from vsdlc_mining.utils import read_jsonl  # noqa: E402

ANNOTATIONS_PATH = ROOT / "data/processed/claude_r2_annotations.json"
BATCH_DIR = ROOT / "data/processed/claude_batches"
PILOT_PATH = ROOT / "data/processed/gold_sample_360_pilot.csv"
PATCH_PATH = ROOT / "data/processed/gold_sample_360_pilot_claude_r2_patch.csv"
PATCH_FIELDS = [
    "repo_full_name",
    "primary_label",
    "confidence",
    "evidence_notes",
    "annotator_id",
    "annotation_round",
]
ANNOTATOR_ID = "claude_r2"
ANNOTATION_ROUND = "1"


def parse_batch(path: Path) -> list[dict[str, str | int]]:
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"\nRepository (\d+):", text)[1:]
    repos: list[dict[str, str | int]] = []
    for index in range(0, len(blocks), 2):
        body = blocks[index + 1]

        def field(name: str) -> str:
            match = re.search(rf"^{name}: (.*)$", body, re.M)
            return match.group(1).strip() if match else ""

        repos.append(
            {
                "stars": int(field("Stars") or 0),
                "language": field("Primary language"),
                "description": field("Description"),
            }
        )
    return repos


def match_slot(
    slot: dict[str, str | int],
    eligible: list[EligibleRepo],
    used: set[str],
) -> EligibleRepo | None:
    desc = str(slot["description"])
    language = str(slot["language"])
    stars = int(slot["stars"])

    def candidates() -> list[EligibleRepo]:
        pool = [
            repo
            for repo in eligible
            if repo.stars == stars
            and (repo.primary_language or "") == language
            and repo.full_name not in used
        ]
        exact = [
            repo
            for repo in pool
            if (repo.github_description or "").strip() == desc
        ]
        if len(exact) == 1:
            return exact
        if desc:
            partial = [
                repo
                for repo in pool
                if desc in (repo.github_description or "")
            ]
            if len(partial) == 1:
                return partial
        if not desc:
            empty = [repo for repo in pool if not (repo.github_description or "").strip()]
            if len(empty) == 1:
                return empty
        return pool if len(pool) == 1 else exact or pool

    matched = candidates()
    if len(matched) == 1:
        return matched[0]
    if len(matched) > 1 and not desc:
        matched = sorted(matched, key=lambda repo: repo.full_name)
        return matched[0]
    return None


def load_batch_annotations() -> dict[int, list[dict[str, str]]]:
    payload = json.loads(ANNOTATIONS_PATH.read_text(encoding="utf-8"))
    return {int(key): value for key, value in payload.items()}


def main() -> None:
    eligible = read_jsonl(
        ROOT / "data/interim/eligible_repos_enriched.jsonl", EligibleRepo
    )
    by_name = {repo.full_name: repo for repo in eligible}
    annotations = load_batch_annotations()

    ordered_names: list[str] = []
    unmatched: list[tuple[int, int, dict[str, str | int]]] = []
    used: set[str] = set()

    for batch_num in range(1, 13):
        batch_path = BATCH_DIR / f"claude_batch_{batch_num:02d}.txt"
        if not batch_path.exists():
            continue
        slots = parse_batch(batch_path)
        for repo_num, slot in enumerate(slots, start=1):
            repo = match_slot(slot, eligible, used)
            if repo is None:
                unmatched.append((batch_num, repo_num, slot))
                continue
            used.add(repo.full_name)
            ordered_names.append(repo.full_name)

    if unmatched:
        details = "\n".join(
            f"batch {batch} repo {repo}: stars={slot['stars']} lang={slot['language']!r}"
            for batch, repo, slot in unmatched
        )
        raise SystemExit(f"Failed to match {len(unmatched)} slots:\n{details}")

    rows: list[dict[str, str]] = []
    patch_rows: list[dict[str, str]] = []
    annotated = 0

    for index, full_name in enumerate(ordered_names):
        batch_num = index // 30 + 1
        repo_num = index % 30 + 1
        repo = by_name[full_name]
        row = eligible_to_gold_row(repo)

        if batch_num in annotations and repo_num <= len(annotations[batch_num]):
            ann = annotations[batch_num][repo_num - 1]
            row["primary_label"] = ann["primary_label"]
            row["confidence"] = ann["confidence"]
            row["evidence_notes"] = ann["evidence_notes"]
            row["annotator_id"] = ANNOTATOR_ID
            row["annotation_round"] = ANNOTATION_ROUND
            patch_rows.append(
                {
                    "repo_full_name": full_name,
                    "primary_label": ann["primary_label"],
                    "confidence": ann["confidence"],
                    "evidence_notes": ann["evidence_notes"],
                    "annotator_id": ANNOTATOR_ID,
                    "annotation_round": ANNOTATION_ROUND,
                }
            )
            annotated += 1

        rows.append(row)

    PILOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with PILOT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=GOLD_SAMPLE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    with PATCH_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PATCH_FIELDS)
        writer.writeheader()
        writer.writerows(patch_rows)

    print(f"wrote {len(rows)} pilot rows to {PILOT_PATH}")
    print(f"wrote {len(patch_rows)} patch rows to {PATCH_PATH}")
    print(f"annotated {annotated} / {len(rows)} rows")


if __name__ == "__main__":
    main()
