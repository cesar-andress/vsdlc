from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_compute_exclude_disagreement_stats_cli() -> None:
    root = Path(__file__).resolve().parents[1]
    script = root / "scripts" / "compute_exclude_disagreement_stats.py"
    output = root / "data" / "processed" / "exclude_disagreement_stats_test.json"
    subprocess.run(
        [
            sys.executable,
            str(script),
            "--output",
            str(output),
        ],
        check=True,
        cwd=root,
    )
    payload = json.loads(output.read_text(encoding="utf-8"))
    human = payload["human_human"]
    assert human["total_disagreements"] == 78
    assert human["exclude_involving"]["percent_of_disagreements"] == 55.1
    assert human["patterns"]["exclude_vs_conventional"]["percent_of_disagreements"] == 52.6
    inspection = payload["metadata_vs_inspection"]
    assert inspection["exclude_involving"]["percent_of_disagreements"] == 60.0
