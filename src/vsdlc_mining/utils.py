"""Shared utilities: logging, JSONL I/O, and text helpers."""

from __future__ import annotations

import json
import logging
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Iterable, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def setup_logging(level: int = logging.INFO) -> None:
    """Configure root logger for CLI scripts."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def ensure_parent(path: Path) -> None:
    """Create parent directories for an output path."""
    path.parent.mkdir(parents=True, exist_ok=True)


def write_jsonl(path: Path, records: Iterable[BaseModel]) -> int:
    """Serialize Pydantic models to JSONL; returns record count."""
    ensure_parent(path)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(record.model_dump_json())
            handle.write("\n")
            count += 1
    return count


def append_jsonl(path: Path, records: Iterable[BaseModel]) -> int:
    """Append Pydantic models to JSONL; returns appended record count."""
    ensure_parent(path)
    count = 0
    with path.open("a", encoding="utf-8") as handle:
        for record in records:
            handle.write(record.model_dump_json())
            handle.write("\n")
            count += 1
    return count


def read_jsonl(path: Path, model: type[T]) -> list[T]:
    """Load JSONL file into typed models."""
    records: list[T] = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(model.model_validate_json(line))
            except Exception as exc:  # noqa: BLE001 — audit-friendly surfacing
                raise ValueError(f"Invalid JSONL at {path}:{line_no}") from exc
    return records


def write_json(path: Path, payload: dict[str, Any]) -> None:
    """Write a JSON document atomically with stable key ordering."""
    ensure_parent(path)
    tmp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            tmp_path = Path(handle.name)
            json.dump(payload, handle, indent=2, sort_keys=True, default=str)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
        tmp_path = None
    finally:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink()


def read_json(path: Path) -> dict[str, Any]:
    """Load a JSON document."""
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return payload


def _close_truncated_json(raw: str) -> str:
    """Append quote/bracket closers for a json.dump payload cut mid-stream."""
    stack: list[str] = []
    in_string = False
    escape = False
    for ch in raw:
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            stack.append("}")
        elif ch == "[":
            stack.append("]")
        elif ch in "}]" and stack and stack[-1] == ch:
            stack.pop()
    if in_string:
        raw += '"'
    raw += "".join(reversed(stack))
    return raw


def salvage_json(path: Path) -> tuple[dict[str, Any], int]:
    """Recover a JSON object truncated by an interrupted write."""
    raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        raise ValueError(f"Empty JSON document in {path}")

    for trim in range(len(raw)):
        candidate = raw[: len(raw) - trim]
        attempts = (candidate, _close_truncated_json(candidate))
        for attempt in attempts:
            try:
                payload = json.loads(attempt)
            except json.JSONDecodeError:
                continue
            if isinstance(payload, dict):
                return payload, trim
    raise ValueError(f"Could not salvage JSON object in {path}")


def normalize_text(value: str | None) -> str:
    """Lowercase and collapse whitespace for keyword matching."""
    if not value:
        return ""
    return re.sub(r"\s+", " ", value.strip().lower())


def contains_keyword(haystack: str, keywords: Iterable[str]) -> str | None:
    """Return the first keyword found in haystack, else None."""
    text = normalize_text(haystack)
    for keyword in keywords:
        if keyword.lower() in text:
            return keyword
    return None
