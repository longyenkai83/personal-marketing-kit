#!/usr/bin/env python3
"""
Render content.json into individual markdown post files for human review.

Usage:
    python scripts/render_post.py <path/to/content.json>

Outputs: <content.json's_dir>/posts/{post_id}_{formula}.md (one file per post).

On Windows, prefix with PYTHONIOENCODING=utf-8.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


FORMAT_LABEL = {
    "ig_caption": "IG Caption",
    "reels_30s": "Reels (30s)",
    "reels_60s": "Reels (60s)",
    "fb_post": "FB Post",
}

GOAL_LABEL = {
    "awareness": "Awareness",
    "lead": "Lead",
    "sale": "Sale",
}


def render_post(post: dict) -> str:
    pid = post["id"]
    fmt = post["format"]
    formula = post["formula"].upper()
    goal = post.get("goal", "")
    hook_id = post.get("hook_id", "")
    insight_id = post.get("insight_id", "")
    word_count = post.get("word_count", "?")

    lines = [
        f"# {pid} — {formula} ({FORMAT_LABEL.get(fmt, fmt)})",
        "",
        f"**Goal:** {GOAL_LABEL.get(goal, goal)} · **Hook:** `{hook_id}` · **Insight:** `{insight_id}` · **Words:** {word_count}",
        "",
        "---",
        "",
    ]

    body = post.get("body", {})
    if "full_text" in body and body["full_text"]:
        lines.append("## Body")
        lines.append("")
        lines.append(body["full_text"])
        lines.append("")
    elif "beats" in body and body["beats"]:
        lines.append("## Script (beats)")
        lines.append("")
        for beat in body["beats"]:
            label = beat["label"].upper()
            text = beat["text"]
            duration = beat.get("duration_sec")
            dur_str = f" _{duration}s_" if duration else ""
            lines.append(f"- **[{label}]**{dur_str} {text}")
        lines.append("")

    cta = post.get("cta", {})
    if cta:
        lines.append("## CTA")
        lines.append("")
        if cta.get("text"):
            lines.append(f"{cta['text']}")
        if cta.get("keyword"):
            lines.append(f"_Keyword:_ `{cta['keyword']}`")
        if cta.get("link"):
            lines.append(f"_Link:_ {cta['link']}")
        lines.append("")

    hashtags = post.get("hashtags", [])
    if hashtags:
        lines.append("## Hashtags")
        lines.append("")
        lines.append(" ".join(f"#{h.lstrip('#')}" for h in hashtags))
        lines.append("")

    constraints = post.get("constraints_passed", {})
    if constraints:
        lines.append("## Validation")
        lines.append("")
        for key, val in constraints.items():
            mark = "✅" if val else "❌"
            lines.append(f"- {mark} {key}")
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    content_path = Path(sys.argv[1])
    if not content_path.exists():
        print(f"ERROR: file not found: {content_path}", file=sys.stderr)
        sys.exit(1)

    with content_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    posts = data.get("posts", [])
    if not posts:
        print("WARN: no posts in content.json", file=sys.stderr)
        sys.exit(0)

    output_dir = content_path.parent / "posts"
    output_dir.mkdir(exist_ok=True)

    for post in posts:
        pid = post["id"]
        formula = post["formula"]
        out_path = output_dir / f"{pid}_{formula}.md"
        with out_path.open("w", encoding="utf-8") as fh:
            fh.write(render_post(post))
        print(f"  wrote {out_path}")

    print(f"\n✅ Rendered {len(posts)} posts to {output_dir}")


if __name__ == "__main__":
    main()