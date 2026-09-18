#!/usr/bin/env python3
"""Portable entry point for validating the public KUKULKAN sample."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.validator import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
