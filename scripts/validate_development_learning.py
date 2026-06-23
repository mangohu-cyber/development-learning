#!/usr/bin/env python3
"""Validate development-learning data consistency."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REVIEW_LINK_RE = re.compile(r"`reviews[\\/](.+?\.md)`")
SKILL_CANDIDATE_RE = re.compile(r"^- `([^`]+)`[：:]", re.MULTILINE)


def default_agents_home(skill_root: Path) -> Path:
    return skill_root.parent.parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def validate_data(data_root: Path) -> list[str]:
    errors: list[str] = []
    index_path = data_root / "index.md"
    candidates_path = data_root / "skill-candidates.md"
    evolution_path = data_root / "development-learning-evolution.md"
    reviews_dir = data_root / "reviews"

    for path in (index_path, candidates_path, evolution_path):
        if not path.exists():
            errors.append(f"Missing required file: {path}")
    if not reviews_dir.exists():
        errors.append(f"Missing reviews directory: {reviews_dir}")
    if errors:
        return errors

    index_text = read_text(index_path)
    candidates_text = read_text(candidates_path)
    evolution_text = read_text(evolution_path)

    for relative in REVIEW_LINK_RE.findall(index_text):
        review_path = reviews_dir / relative
        if not review_path.exists():
            errors.append(f"Index references missing review: {review_path}")

    for candidate in SKILL_CANDIDATE_RE.findall(index_text):
        if f"## {candidate}" not in candidates_text:
            errors.append(f"Index candidate missing detail section: {candidate}")

    if "development-learning" not in evolution_text:
        errors.append("Evolution log does not mention development-learning")

    review_names = [path.name for path in reviews_dir.glob("*.md")]
    duplicate_reviews = sorted(name for name in set(review_names) if review_names.count(name) > 1)
    for duplicate in duplicate_reviews:
        errors.append(f"Duplicate review filename found: {duplicate}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate development-learning data consistency.")
    parser.add_argument(
        "--agents-home",
        help="Agent home containing data/development-learning. Defaults to the parent of the skills directory.",
    )
    parser.add_argument("--data-root", help="Explicit development-learning data root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skill_root = Path(__file__).resolve().parent.parent
    if args.data_root:
        data_root = Path(args.data_root).expanduser().resolve()
    else:
        agents_home = Path(args.agents_home).expanduser().resolve() if args.agents_home else default_agents_home(skill_root)
        data_root = agents_home / "data" / "development-learning"

    errors = validate_data(data_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"development-learning data validation passed: {data_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
