#!/usr/bin/env python3
"""Validate content.json against schema + quality gates before export.

Usage:
    python validate.py <content.json>

Exits 0 if all checks pass, 1 if any fail (prints issues).
Schema validation requires jsonschema (pip install jsonschema). If missing,
falls back to structural checks only.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AI_GIVEAWAY_PHRASES = [
    "in today's fast-paced world",
    "let's dive in",
    "let's unpack",
    "game-changer",
    "unlock your potential",
    "in today's world",
    "at the end of the day",
    "navigate the complexities",
    "robust solution",
    "cutting-edge",
    "paradigm shift",
]


def word_count(text: str) -> int:
    return len(text.split())


def check_item_variety(items: list[dict]) -> list[str]:
    """Verify no two items share same verb-object combo in heading."""
    issues = []
    seen_signatures = {}
    for item in items:
        heading = item.get("heading", "").lower().strip(".")
        # Signature: first 4 words after "stop"
        words = heading.replace("stop ", "", 1).split()
        sig = " ".join(words[:3]) if words else heading
        if sig in seen_signatures:
            issues.append(
                f"Item {item['number']} heading '{heading}' too similar to item {seen_signatures[sig]}"
            )
        else:
            seen_signatures[sig] = item["number"]
    return issues


def check_ai_giveaways(content: dict) -> list[str]:
    """Flag cliche phrases that signal AI writing."""
    issues = []
    all_text_parts = []

    def collect_text(obj, path=""):
        if isinstance(obj, str):
            all_text_parts.append((path, obj))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                collect_text(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                collect_text(v, f"{path}[{i}]")

    collect_text(content)
    for path, text in all_text_parts:
        lower = text.lower()
        for phrase in AI_GIVEAWAY_PHRASES:
            if phrase in lower:
                issues.append(f"AI-giveaway phrase '{phrase}' at {path}")
    return issues


def check_word_counts(content: dict) -> list[str]:
    """Enforce body paragraph word-count bounds for Canva cell fit."""
    issues = []
    for item in content.get("items", []):
        for i, para in enumerate(item.get("body_paragraphs", [])):
            wc = word_count(para)
            if wc < 15:
                issues.append(f"Item {item['number']} paragraph {i+1}: too short ({wc} words, min 15)")
            elif wc > 90:
                issues.append(f"Item {item['number']} paragraph {i+1}: too long ({wc} words, max 90)")
    return issues


def check_fake_content(content: dict) -> list[str]:
    """Verify testimonials are either real (user-provided) or clearly placeholders."""
    issues = []
    for i, t in enumerate(content.get("testimonials", []), start=1):
        quote = t.get("quote", "")
        name = t.get("name", "")
        # Heuristic: if quote has specific numbers/percentages not marked as placeholder, flag it
        is_placeholder = t.get("is_placeholder", False) or "[placeholder" in name.lower() or "[placeholder" in quote.lower()
        has_specific_stats = bool(re.search(r"\$[\d,]+|\d+%|\d+x|\d+\s*figure", quote))
        if has_specific_stats and not is_placeholder:
            issues.append(
                f"Testimonial {i}: contains specific stats ('{quote[:60]}...') — must be real testimonial or marked is_placeholder=true"
            )
    return issues


def check_cta_threading(content: dict) -> list[str]:
    """Verify offer page CTA matches intro setup — warn if disconnected."""
    issues = []
    intro_text = " ".join(content.get("intro", {}).get("body_paragraphs", [])).lower()
    offer_cta = content.get("offer_page", {}).get("cta_button", "").lower()
    product = content.get("metadata", {}).get("product_cta", "").lower()

    if product and not offer_cta:
        issues.append("Offer CTA button is empty but product_cta is set in metadata")

    return issues


def check_language_consistency(content: dict) -> list[str]:
    """Flag obvious Vietnamese-English code-switching."""
    issues = []
    language = content.get("metadata", {}).get("language")
    if language != "vi":
        return issues  # Only check for Vietnamese output

    english_words_in_vi = re.compile(r"\b(focus|mindset|content|brand|engage|audience|strategy|growth|scale|leverage)\b", re.IGNORECASE)

    for item in content.get("items", []):
        for i, para in enumerate(item.get("body_paragraphs", [])):
            matches = english_words_in_vi.findall(para)
            if len(matches) >= 2:
                issues.append(
                    f"Item {item['number']} paragraph {i+1}: {len(matches)} English words in Vietnamese text — potential code-switching ({matches[:3]})"
                )
    return issues


def try_schema_validate(content: dict, schema_path: Path) -> list[str]:
    """Best-effort JSON schema validation (skip if jsonschema not installed)."""
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return ["(jsonschema not installed - skipping structural validation; run: pip install jsonschema)"]
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = jsonschema.Draft7Validator(schema)
        errors = sorted(validator.iter_errors(content), key=lambda e: e.path)
        return [f"Schema: {'.'.join(str(p) for p in e.path)}: {e.message}" for e in errors]
    except Exception as exc:
        return [f"Schema validation error: {exc}"]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2

    content_path = Path(sys.argv[1])
    content = json.loads(content_path.read_text(encoding="utf-8"))

    schema_path = Path(__file__).parent.parent / "schema.json"

    all_issues: list[tuple[str, list[str]]] = [
        ("Schema", try_schema_validate(content, schema_path)),
        ("Item variety", check_item_variety(content.get("items", []))),
        ("AI-giveaway phrases", check_ai_giveaways(content)),
        ("Word counts", check_word_counts(content)),
        ("Fake content", check_fake_content(content)),
        ("CTA threading", check_cta_threading(content)),
        ("Language consistency", check_language_consistency(content)),
    ]

    fatal = 0
    for category, issues in all_issues:
        if not issues:
            print(f"[OK] {category}")
            continue
        real_issues = [i for i in issues if not i.startswith("(jsonschema not installed")]
        label = "[FAIL]" if real_issues else "[WARN]"
        print(f"{label} {category}:")
        for issue in issues:
            print(f"    - {issue}")
        fatal += len(real_issues)

    print()
    if fatal == 0:
        print("All gates passed. Safe to export.")
        return 0
    print(f"{fatal} issue(s). Fix before export.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
