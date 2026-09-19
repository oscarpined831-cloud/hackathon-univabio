#!/usr/bin/env python3
"""Validate the reviewed, non-sensitive KUKULKAN example metrics.

This module checks data shape and simple demonstration thresholds. It does not
run a predictive model and must not be interpreted as clinical validation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

REQUIRED_RESIDUES = ("Lys22", "Asp44", "Gly46")
REQUIRED_FIELDS = ("pLDDT", "target", "verified")
DEFAULT_SAMPLE = Path(__file__).parents[1] / "data" / "sample" / "validation_metrics.json"


def load_metrics(path: Path) -> Dict[str, Any]:
    """Load and validate the public sample JSON document."""
    with path.open(encoding="utf-8") as handle:
        document = json.load(handle)

    if document.get("data_status") != "example_audit_data":
        raise ValueError("data_status must be 'example_audit_data'")
    metrics = document.get("residues")
    if not isinstance(metrics, dict):
        raise ValueError("residues must be an object")

    missing = [residue for residue in REQUIRED_RESIDUES if residue not in metrics]
    if missing:
        raise ValueError(f"missing residues: {', '.join(missing)}")

    for residue in REQUIRED_RESIDUES:
        entry = metrics[residue]
        if not isinstance(entry, dict) or any(field not in entry for field in REQUIRED_FIELDS):
            raise ValueError(f"{residue} must contain {', '.join(REQUIRED_FIELDS)}")
        if not isinstance(entry["pLDDT"], (int, float)) or not 0 <= entry["pLDDT"] <= 100:
            raise ValueError(f"{residue}.pLDDT must be between 0 and 100")
        if not isinstance(entry["target"], str) or not isinstance(entry["verified"], bool):
            raise ValueError(f"{residue} has invalid field types")
    return document


def validate_metrics(document: Dict[str, Any], threshold: float = 85.0) -> List[str]:
    """Return human-readable failures against the demonstration threshold."""
    failures = []
    for residue in REQUIRED_RESIDUES:
        entry = document["residues"][residue]
        if entry["pLDDT"] < threshold or not entry["verified"]:
            failures.append(residue)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_SAMPLE)
    parser.add_argument("--threshold", type=float, default=85.0)
    args = parser.parse_args()

    try:
        document = load_metrics(args.path)
        failures = validate_metrics(document, args.threshold)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}")
        return 1

    for residue, entry in document["residues"].items():
        status = "PASS" if residue not in failures else "FAIL"
        print(f"{residue}: pLDDT={entry['pLDDT']:.1f} target={entry['target']} [{status}]")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
