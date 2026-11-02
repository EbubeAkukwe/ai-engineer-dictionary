#!/usr/bin/env python3
"""Lightweight checks for dictionary entry metadata and required sections."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = [
    "Simple explanation",
    "Technical explanation",
    "Why it matters in AI engineering",
    "How it works",
    "Practical example",
    "Related terms",
    "Further reading",
]
REQUIRED_FIELDS = ["title:", "description:", "term:", "letter:", "category:", "difficulty:"]

def main() -> int:
    errors = []
    seen_terms = {}

    for path in sorted((ROOT / "dictionary").glob("*/*.qmd")):
        if path.name in {"index.qmd"}:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path.relative_to(ROOT)}: missing YAML front matter")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append(f"{path.relative_to(ROOT)}: malformed YAML front matter")
            continue
        front_matter = parts[1]
        body = parts[2]

        for field in REQUIRED_FIELDS:
            if not re.search(rf"(?m)^{re.escape(field)}", front_matter):
                errors.append(f"{path.relative_to(ROOT)}: missing `{field[:-1]}` metadata")

        term_match = re.search(r'(?m)^term:\s*["\']?(.+?)["\']?\s*$', front_matter)
        if term_match:
            term = term_match.group(1).strip().strip('"\'').casefold()
            if term in seen_terms:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate term also found in "
                    f"{seen_terms[term]}"
                )
            else:
                seen_terms[term] = str(path.relative_to(ROOT))

        for section in REQUIRED_SECTIONS:
            if f"## {section}" not in body:
                errors.append(f"{path.relative_to(ROOT)}: missing section `{section}`")

    if errors:
        print("Entry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(seen_terms)} dictionary entries successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
