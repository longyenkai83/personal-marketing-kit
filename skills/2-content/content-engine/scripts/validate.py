#!/usr/bin/env python3
"""
Validate content-engine artifacts against their JSON schemas.

Usage:
    python scripts/validate.py {profile|insights|hooks|content} <path/to/file.json>

Exit codes: 0 = pass, 1 = invalid JSON / file missing, 2 = schema validation failed.

On Windows, prefix with PYTHONIOENCODING=utf-8 for VN/emoji output:
    PYTHONIOENCODING=utf-8 python scripts/validate.py profile output/.../profile.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft7Validator
except ImportError:
    print("ERROR: missing dependency 'jsonschema'. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(1)

SKILL_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = {
    "profile": SKILL_ROOT / "schemas" / "profile.schema.json",
    "insights": SKILL_ROOT / "schemas" / "insights.schema.json",
    "hooks": SKILL_ROOT / "schemas" / "hooks.schema.json",
    "content": SKILL_ROOT / "schemas" / "content.schema.json",
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def custom_checks(artifact_type: str, data: dict) -> list[str]:
    """Schema-level rules can't catch — invariants beyond JSON schema."""
    errors = []

    if artifact_type == "profile":
        ev = data.get("evidence_summary", {})
        observed = ev.get("observed_pct", 0)
        ready = ev.get("ready_for_hook_stage", False)
        if ready and observed < 60:
            errors.append(f"evidence_summary.ready_for_hook_stage=true but observed_pct={observed} < 60")
        if not ready and observed >= 60:
            errors.append(f"evidence_summary.ready_for_hook_stage=false but observed_pct={observed} >= 60 (should be true)")

        verbatim_bank = data.get("voice", {}).get("verbatim_bank", [])
        if len(verbatim_bank) < 5:
            errors.append(f"voice.verbatim_bank has {len(verbatim_bank)} items, schema requires >= 5")

    elif artifact_type == "hooks":
        hooks = data.get("hooks", [])
        # Check voice-vocabulary rule (informational, not strict — runtime should enforce)
        without_voice = [h["id"] for h in hooks if not h.get("uses_voice_words")]
        if without_voice:
            errors.append(f"INFO: {len(without_voice)} hooks missing uses_voice_words tag — Stage 3 rule violated. Examples: {without_voice[:5]}")

        # Check hook type variety per insight
        from collections import defaultdict
        by_insight = defaultdict(set)
        for h in hooks:
            by_insight[h["paired_insight_id"]].add(h["type"])
        low_variety = [iid for iid, types in by_insight.items() if len(types) < 2]
        if low_variety:
            errors.append(f"INFO: {len(low_variety)} insights have <2 hook types — variety rule violated. Examples: {low_variety[:5]}")

    elif artifact_type == "content":
        posts = data.get("posts", [])
        for post in posts:
            cp = post.get("constraints_passed", {})
            failed = [k for k, v in cp.items() if v is False]
            if failed:
                errors.append(f"post {post['id']} failed constraints: {failed}")

    return errors


def main():
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    artifact_type = sys.argv[1]
    file_path = Path(sys.argv[2])

    if artifact_type not in SCHEMAS:
        print(f"ERROR: artifact_type must be one of {list(SCHEMAS.keys())}", file=sys.stderr)
        sys.exit(1)

    if not file_path.exists():
        print(f"ERROR: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    schema_path = SCHEMAS[artifact_type]
    if not schema_path.exists():
        print(f"ERROR: schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)

    try:
        data = load_json(file_path)
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    schema = load_json(schema_path)
    validator = Draft7Validator(schema)
    schema_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))

    has_errors = False
    if schema_errors:
        has_errors = True
        print(f"❌ Schema validation FAILED for {file_path.name}:")
        for err in schema_errors:
            path = ".".join(str(p) for p in err.path) or "<root>"
            print(f"  - {path}: {err.message}")

    custom_errors = custom_checks(artifact_type, data)
    if custom_errors:
        info_only = all(e.startswith("INFO:") for e in custom_errors)
        if not info_only:
            has_errors = True
        print(f"\n{'⚠️ ' if info_only else '❌ '}Custom rule check for {artifact_type}:")
        for err in custom_errors:
            print(f"  - {err}")

    if not has_errors:
        print(f"✅ {file_path.name} valid against {artifact_type}.schema.json")
        sys.exit(0)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()