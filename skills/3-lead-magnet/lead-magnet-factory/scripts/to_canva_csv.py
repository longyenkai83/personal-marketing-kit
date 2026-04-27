#!/usr/bin/env python3
"""Convert content.json to Canva Bulk Create CSV.

Usage:
    python to_canva_csv.py <input.json> <output.csv>

The CSV has exactly ONE data row (one ebook = one design in Canva).
Column headers match placeholder names in reference/canva_template_spec.md.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def split_title_by_highlight(title: str, highlight_words: list[str]) -> tuple[str, str, str]:
    """Split a title into (part1, highlight, part2) based on first highlight word found.

    If no highlight matches, returns (title, "", "").
    """
    if not highlight_words:
        return title, "", ""
    for hw in highlight_words:
        if hw in title:
            idx = title.index(hw)
            return title[:idx].rstrip(), hw, title[idx + len(hw):].lstrip()
    return title, "", ""


def build_row(content: dict) -> dict[str, str]:
    row: dict[str, str] = {}

    # Metadata
    row["author_name"] = content["metadata"].get("author_name", "")

    # Cover
    cover = content["cover"]
    p1, hl, p2 = split_title_by_highlight(cover["title_full"], cover.get("title_highlight_words", []))
    row["cover_title_part1"] = p1
    row["cover_title_highlight"] = hl
    row["cover_title_part2"] = p2
    row["cover_subtitle"] = cover.get("subtitle", "")

    # Intro
    intro = content["intro"]
    row["intro_hook_title"] = intro["hook_title"]
    paras = intro.get("body_paragraphs", [])
    row["intro_body_1"] = paras[0] if len(paras) > 0 else ""
    row["intro_body_2"] = paras[1] if len(paras) > 1 else ""
    row["intro_body_3"] = paras[2] if len(paras) > 2 else ""
    row["intro_cta_line"] = intro.get("cta_line", "")
    row["intro_cta_summary"] = intro.get("cta_summary", "")

    # Items 1-12
    items = content["items"]
    if len(items) != 12:
        raise ValueError(f"Expected exactly 12 items, got {len(items)}")
    for item in items:
        n = item["number"]
        row[f"item_{n}_number"] = str(n)
        row[f"item_{n}_heading"] = item["heading"]
        bodies = item.get("body_paragraphs", [])
        row[f"item_{n}_body_1"] = bodies[0] if len(bodies) > 0 else ""
        row[f"item_{n}_body_2"] = bodies[1] if len(bodies) > 1 else ""

    # Offer page
    offer = content["offer_page"]
    op1, ohl, op2 = split_title_by_highlight(offer["title"], offer.get("title_highlight_words", []))
    row["offer_header"] = offer.get("header", "")
    row["offer_title_part1"] = op1
    row["offer_title_highlight"] = ohl
    row["offer_title_part2"] = op2
    row["offer_description"] = offer.get("description", "")
    for i, benefit in enumerate(offer.get("benefits", []), start=1):
        row[f"benefit_{i}_emoji"] = benefit.get("emoji", "")
        row[f"benefit_{i}_title"] = benefit.get("title", "")
        row[f"benefit_{i}_desc"] = benefit.get("description", "")
    row["offer_cta_button"] = offer.get("cta_button", "")

    # Testimonials
    for i, t in enumerate(content.get("testimonials", []), start=1):
        row[f"testimonial_{i}_name"] = t.get("name", "")
        row[f"testimonial_{i}_role"] = t.get("role", "")
        row[f"testimonial_{i}_quote"] = t.get("quote", "")

    # Closing page
    closing = content["closing_page"]
    cp1, chl, cp2 = split_title_by_highlight(
        closing["title"],
        closing.get("title_highlight_words", []) or [closing["title"].split()[-1]],
    )
    row["closing_title_part1"] = cp1
    row["closing_title_highlight"] = chl
    row["closing_title_part2"] = cp2
    row["closing_intro_line"] = closing.get("intro_line", "")
    for i, d in enumerate(closing.get("differentiators", []), start=1):
        row[f"diff_{i}_emoji"] = d.get("emoji", "")
        row[f"diff_{i}_title"] = d.get("title", "")
        row[f"diff_{i}_desc"] = d.get("description", "")
    row["closing_final_hook"] = closing.get("final_hook", "")
    row["closing_cta_button"] = closing.get("cta_button", "")
    row["closing_tagline"] = closing.get("closing_tagline", "")
    row["closing_signature"] = closing.get("signature_line", "")

    return row


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    content = json.loads(in_path.read_text(encoding="utf-8"))
    row = build_row(content)

    # Preserve insertion order as column order
    fieldnames = list(row.keys())
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(row)

    print(f"Wrote {len(fieldnames)} columns to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
