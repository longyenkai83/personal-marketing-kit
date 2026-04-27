#!/usr/bin/env python3
"""
Validate Claude Code subagent file (.md) against schema + 10 best-practice gates.

Usage:
    python scripts/validate.py <path/to/subagent.md>

Output:
    Markdown-formatted audit report on stdout.

Exit codes:
    0 = schema valid + ≥8/10 gates passed
    1 = file missing / invalid arguments
    2 = schema invalid OR <8/10 gates passed

On Windows, prefix with PYTHONIOENCODING=utf-8 for VN/emoji output.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: missing dependency 'pyyaml'. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    from jsonschema import Draft7Validator
except ImportError:
    print("ERROR: missing dependency 'jsonschema'. Install: pip install jsonschema", file=sys.stderr)
    sys.exit(1)


SKILL_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = SKILL_ROOT / "schemas" / "subagent.schema.json"


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    """Extract YAML frontmatter and body from markdown text."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return None, text
    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        return {"_yaml_error": str(e)}, match.group(2)
    body = match.group(2).strip()
    return frontmatter, body


def best_practice_gates(frontmatter: dict, body: str) -> list[tuple[str, str, str]]:
    """Run 10 gates. Returns list of (name, status, detail)
    where status is 'pass' / 'warn' / 'info' / 'na'."""
    gates: list[tuple[str, str, str]] = []
    desc = frontmatter.get("description", "") or ""
    body_lower = body.lower()
    body_words = len(body.split())

    # Gate 1 — description_clear
    if len(desc) >= 30:
        gates.append(("description_clear", "pass", f"description {len(desc)} chars"))
    else:
        gates.append(("description_clear", "warn", f"description chỉ {len(desc)} chars (cần ≥30 để Claude biết khi nào delegate)"))

    # Gate 2 — tools_restricted
    has_tools = "tools" in frontmatter or "disallowedTools" in frontmatter
    if has_tools:
        gates.append(("tools_restricted", "pass", "tools/disallowedTools đã set"))
    else:
        gates.append(("tools_restricted", "warn", "không có tools/disallowedTools — subagent inherit hết tools từ parent (security risk + thiếu focus)"))

    # Gate 3 — model_explicit
    if "model" in frontmatter:
        gates.append(("model_explicit", "pass", f"model = {frontmatter['model']}"))
    else:
        gates.append(("model_explicit", "warn", "model field không set — default = inherit (bỏ cơ hội control cost)"))

    # Gate 4 — role_defined
    has_role = bool(re.search(r"\b(you are|bạn là|you're)\b", body_lower))
    if has_role:
        gates.append(("role_defined", "pass", "có 'You are/Bạn là' trong body"))
    else:
        gates.append(("role_defined", "warn", "system prompt thiếu role definition ('You are X' / 'Bạn là X')"))

    # Gate 5 — procedure_present
    has_numbered_steps = bool(re.search(r"^\s*[1-9][0-9]*\.\s+\S", body, re.MULTILINE))
    has_procedure_keyword = bool(re.search(r"\b(when invoked|procedure|workflow|khi được gọi|khi:|quy trình)\b", body_lower))
    if has_numbered_steps or has_procedure_keyword:
        gates.append(("procedure_present", "pass", "có numbered steps hoặc procedure keyword"))
    else:
        gates.append(("procedure_present", "warn", "system prompt thiếu numbered procedure (cần 1. 2. 3. để subagent biết workflow)"))

    # Gate 6 — description_concise
    if len(desc) <= 500:
        gates.append(("description_concise", "pass", f"description {len(desc)} chars ≤500"))
    else:
        gates.append(("description_concise", "warn", f"description {len(desc)} chars >500 — quá dài, chuyển nội dung sang body"))

    # Gate 7 — body_substantive
    if body_words >= 30:
        gates.append(("body_substantive", "pass", f"body {body_words} từ"))
    else:
        gates.append(("body_substantive", "warn", f"body chỉ {body_words} từ (cần ≥30 — subagent sẽ improvise nếu thiếu hướng dẫn)"))

    # Gate 8 — memory_instructions (conditional)
    if frontmatter.get("memory"):
        has_memory_inst = bool(re.search(r"\b(memory|knowledge|memory\.md|ghi nhớ|cập nhật|update.*memory)\b", body_lower))
        if has_memory_inst:
            gates.append(("memory_instructions", "pass", f"memory={frontmatter['memory']} + body có instructions update"))
        else:
            gates.append(("memory_instructions", "warn", f"memory={frontmatter['memory']} nhưng body không có instructions update memory → memory directory sẽ rỗng"))
    else:
        gates.append(("memory_instructions", "na", "memory không enable — không cần check"))

    # Gate 9 — auto_trigger_signal (info)
    auto_phrase = bool(re.search(r"\b(use proactively|automatically|use immediately|proactively|use this when)\b", desc.lower()))
    if auto_phrase:
        gates.append(("auto_trigger_signal", "info", "có cụm 'Use proactively / automatically' → Claude tự delegate"))
    else:
        gates.append(("auto_trigger_signal", "info", "không có cụm 'Use proactively' → user phải @-mention thủ công (OK nếu cố ý)"))

    # Gate 10 — no_wildcard_misuse
    tools_field = frontmatter.get("tools")
    has_wildcard = False
    if isinstance(tools_field, str):
        has_wildcard = "*" in tools_field
    elif isinstance(tools_field, list):
        has_wildcard = any("*" in str(t) for t in tools_field)
    if has_wildcard:
        gates.append(("no_wildcard_misuse", "warn", "tools field có '*' — không phải syntax Claude Code (bỏ field nếu muốn inherit all)"))
    else:
        gates.append(("no_wildcard_misuse", "pass", "tools format ok"))

    return gates


def detect_anti_patterns(frontmatter: dict, body: str) -> list[tuple[str, str]]:
    """Detect common anti-patterns. Returns list of (label, detail)."""
    found: list[tuple[str, str]] = []
    desc = frontmatter.get("description", "") or ""

    # A1 — Multi-purpose (description đề cập nhiều task khác)
    task_words = re.findall(r"\b(review|debug|test|deploy|refactor|search|analyze|fix|format|lint|migrate)\b", desc.lower())
    if len(set(task_words)) >= 3:
        found.append(("A1 — Multi-purpose", f"description đề cập ≥3 task khác nhau ({', '.join(set(task_words))}). Tách thành nhiều subagent focused."))

    # A4 — Model overkill (Opus + read-only)
    is_opus = str(frontmatter.get("model", "")).startswith("opus") or "opus" in str(frontmatter.get("model", "")).lower()
    tools = frontmatter.get("tools", "")
    tools_str = tools if isinstance(tools, str) else ", ".join(tools) if isinstance(tools, list) else ""
    is_readonly = (
        ("Edit" not in tools_str) and ("Write" not in tools_str) and ("disallowedTools" not in frontmatter or "Edit" in str(frontmatter.get("disallowedTools", "")))
        if tools_str
        else False
    )
    if is_opus and is_readonly:
        found.append(("A4 — Model overkill", "model: opus cho subagent read-only — Haiku đủ và rẻ hơn 4-5x."))

    # A3 — Permission bypass với destructive tools
    if frontmatter.get("permissionMode") == "bypassPermissions":
        has_dangerous = any(t in tools_str for t in ["Edit", "Write", "Bash"])
        if has_dangerous:
            found.append(("A3 — Permission bypass nguy hiểm", "permissionMode: bypassPermissions + có Edit/Write/Bash → có thể chạy lệnh phá hoại không cần xác nhận."))

    # A5 — Memory cho one-shot task
    one_shot_keywords = ["once", "one-time", "single", "one shot", "1 lần", "duy nhất"]
    if frontmatter.get("memory") and any(kw in body.lower() for kw in one_shot_keywords):
        found.append(("A5 — Memory cho one-shot", "memory enabled nhưng task là one-shot. Memory để build knowledge across conversations — bỏ field."))

    # A7 — initialPrompt cho subagent (chỉ cho main session)
    if "initialPrompt" in frontmatter:
        found.append(("A7 — initialPrompt misplaced", "initialPrompt chỉ áp dụng khi run as main session via `--agent`. Subagent thông thường (delegate) không dùng — bỏ field."))

    return found


def render_report(path: Path, frontmatter: dict | None, body: str, schema_errors: list, gates: list, anti_patterns: list) -> str:
    """Render audit report as markdown."""
    name = "<unparseable>"
    if frontmatter and isinstance(frontmatter, dict):
        name = frontmatter.get("name", "<unnamed>")
    lines = [f"# Audit: {name}", "", f"**File:** `{path}`", ""]

    # Schema validation
    lines.append("## Schema validation")
    lines.append("")
    if frontmatter is None:
        lines.append("❌ Không tìm thấy YAML frontmatter (file phải bắt đầu bằng `---`)")
    elif "_yaml_error" in frontmatter:
        lines.append(f"❌ YAML parse error: {frontmatter['_yaml_error']}")
    elif schema_errors:
        lines.append("❌ Schema errors:")
        for err in schema_errors:
            path_str = ".".join(str(p) for p in err.path) or "<root>"
            lines.append(f"- `{path_str}`: {err.message}")
    else:
        lines.append("✅ Frontmatter valid theo Claude Code subagent spec.")
    lines.append("")

    # Gates
    pass_count = sum(1 for _, status, _ in gates if status == "pass")
    total_real_gates = sum(1 for _, status, _ in gates if status not in ("info", "na"))
    pass_real = sum(1 for _, status, _ in gates if status == "pass")

    lines.append(f"## Best practice gates ({pass_real}/{total_real_gates} passed, {len(gates)} total)")
    lines.append("")
    lines.append("| Gate | Status | Detail |")
    lines.append("|---|---|---|")
    icons = {"pass": "✅", "warn": "⚠️", "info": "ℹ️", "na": "—"}
    for i, (name_, status, detail) in enumerate(gates, 1):
        lines.append(f"| {i}. {name_} | {icons[status]} | {detail} |")
    lines.append("")

    # Anti-patterns
    lines.append("## Anti-pattern check")
    lines.append("")
    if anti_patterns:
        for label, detail in anti_patterns:
            lines.append(f"- ⚠️ **{label}** — {detail}")
    else:
        lines.append("✅ Không phát hiện anti-pattern phổ biến.")
    lines.append("")

    # Recommendations
    lines.append("## Recommendations")
    lines.append("")
    critical = [(n, d) for n, s, d in gates if s == "warn" and n in ("description_clear", "tools_restricted", "model_explicit", "role_defined", "procedure_present", "body_substantive", "no_wildcard_misuse")]
    improvement = [(n, d) for n, s, d in gates if s == "warn" and n in ("description_concise", "memory_instructions")]

    if critical or schema_errors or any("nguy hiểm" in d for _, d in anti_patterns):
        lines.append("### 🔴 Critical (must fix)")
        for n, d in critical:
            lines.append(f"- **{n}**: {d}")
        for label, detail in anti_patterns:
            if "nguy hiểm" in detail:
                lines.append(f"- **{label}**: {detail}")
        lines.append("")

    if improvement or any("Multi-purpose" in label or "overkill" in label.lower() or "one-shot" in label or "misplaced" in label for label, _ in anti_patterns):
        lines.append("### 🟡 Improvement (should fix)")
        for n, d in improvement:
            lines.append(f"- **{n}**: {d}")
        for label, detail in anti_patterns:
            if "nguy hiểm" not in detail:
                lines.append(f"- **{label}**: {detail}")
        lines.append("")

    info_gates = [(n, d) for n, s, d in gates if s == "info"]
    if info_gates:
        lines.append("### 🔵 Info")
        for n, d in info_gates:
            lines.append(f"- **{n}**: {d}")
        lines.append("")

    parse_failed = frontmatter is None or (isinstance(frontmatter, dict) and "_yaml_error" in frontmatter)

    if parse_failed:
        lines.append("### 🔴 Critical (must fix)")
        if frontmatter is None:
            lines.append("- File thiếu YAML frontmatter — phải bắt đầu bằng `---` và có ít nhất `name` + `description`.")
        else:
            lines.append(f"- YAML parse error — sửa cú pháp YAML trước. Lỗi: `{frontmatter['_yaml_error']}`")
        lines.append("- _Common cause:_ giá trị bắt đầu bằng `*` cần quote (ví dụ `tools: \"*\"` thay vì `tools: *`). Lưu ý: `*` không phải Claude Code syntax — bỏ field nếu muốn inherit all.")
        lines.append("")
    elif not (critical or improvement or info_gates or anti_patterns):
        lines.append("✅ Không có gì cần fix — subagent production-ready.")
        lines.append("")

    # Verdict
    lines.append("## Tóm tắt")
    lines.append("")
    if parse_failed:
        lines.append("**Score:** N/A (parse failed)")
        lines.append("")
        lines.append("**Verdict:** ❌ File không parse được — fix YAML/frontmatter trước khi audit lại.")
    else:
        lines.append(f"**Score:** {pass_real}/{total_real_gates} gates passed.")
        lines.append("")
        if schema_errors or pass_real < total_real_gates - 1:
            lines.append("**Verdict:** ❌ Chưa production-ready. Fix Critical + Improvement trước.")
        elif pass_real == total_real_gates:
            lines.append("**Verdict:** ✅ Production-ready.")
        else:
            lines.append("**Verdict:** 🟡 Gần OK — fix 1-2 Improvement để hoàn thiện.")

    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)

    schema_errors = []
    gates = []
    anti_patterns = []

    if frontmatter is not None and "_yaml_error" not in frontmatter:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft7Validator(schema)
        schema_errors = sorted(validator.iter_errors(frontmatter), key=lambda e: list(e.path))
        gates = best_practice_gates(frontmatter, body)
        anti_patterns = detect_anti_patterns(frontmatter, body)

    report = render_report(path, frontmatter, body, schema_errors, gates, anti_patterns)
    print(report)

    pass_count = sum(1 for _, s, _ in gates if s == "pass")
    total_real = sum(1 for _, s, _ in gates if s not in ("info", "na"))
    if frontmatter is None or "_yaml_error" in frontmatter or schema_errors or (total_real and pass_count < total_real - 1):
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()