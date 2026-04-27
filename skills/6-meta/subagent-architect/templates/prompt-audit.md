# AUDIT mode — Prompt template

> Internal prompt cho AUDIT mode. Input = đường dẫn file `.md`. Output = report VN-friendly.

## Workflow

1. Verify file tồn tại + đọc được
2. Run `scripts/validate.py <path>` — capture stdout
3. Parse output validate.py
4. Render report theo template dưới
5. Show report cho user

## Report template

```markdown
# Audit: {agent-name}

**File:** `{path}`
**Scope:** `{project | user | other}`
**Source:** `{detected from path}`

---

## Schema validation

{nếu pass:}
✅ Frontmatter valid theo Claude Code subagent spec.

{nếu fail:}
❌ Schema errors:
- `{field-path}`: {error message}
- ...

---

## Best practice gates ({pass}/10 passed)

| Gate | Status | Detail |
|---|---|---|
| 1. description_clear | ✅/⚠️ | ... |
| 2. tools_restricted | ✅/⚠️ | ... |
| 3. model_explicit | ✅/⚠️ | ... |
| 4. role_defined | ✅/⚠️ | ... |
| 5. procedure_present | ✅/⚠️ | ... |
| 6. description_concise | ✅/⚠️ | ... |
| 7. body_substantive | ✅/⚠️ | ... |
| 8. memory_instructions | ✅/⚠️/N-A | ... |
| 9. auto_trigger_signal | ℹ️ | ... |
| 10. no_wildcard_misuse | ✅/⚠️ | ... |

---

## Recommendations

### 🔴 Critical (must fix)
{liệt kê schema errors + gate 1/2/3/4/5/7/10 fails}

### 🟡 Improvement (should fix)
{gate 6/8 fails + anti-patterns detected}

### 🔵 Optional (consider)
{gate 9 info + minor improvements}

---

## Anti-pattern check

{nếu detected:}
- ⚠️ **A1 — Multi-purpose:** Description đề cập ≥3 task khác nhau. Tách thành 3 subagent.
- ⚠️ **A4 — Model overkill:** Read-only task dùng `model: opus`. Chuyển sang `haiku` để giảm cost.
- ...

{nếu không detected: "✅ Không phát hiện anti-pattern phổ biến."}

---

## Tóm tắt

**Score:** {pass}/10 gates passed.

**Verdict:**
- 9-10/10: Production-ready
- 7-8/10: Cần fix 1-3 điều, sau đó OK
- 5-6/10: Cần rework đáng kể
- <5/10: Rebuild từ đầu (chạy BUILD mode)
```

## Specifically for chronic problems

Nếu detect các pattern dưới, thêm advice vào "Recommendations":

### "Subagent không bao giờ tự trigger"
→ Check Gate 1 (description_clear) + Gate 9 (auto_trigger_signal). Description có nhắc đúng task không? Có "Use proactively when..." không? Doc nói: "Claude uses each subagent's description to decide when to delegate tasks."

### "Subagent fails với permission errors"
→ Check `tools` field. Có thiếu tool cần thiết không (Read/Grep/Glob/Bash là minimum cho hầu hết tasks)? Hoặc `permissionMode` quá strict (`dontAsk` chặn cả tool đã allowlist).

### "Subagent output verbose, eat parent context"
→ Check Gate 7 (body_substantive). Body có nói cụ thể về output format không? Subagent verbose vì không biết scope. Add "## Output format" với word limit + structure rõ.

### "Subagent run lâu, đốt token"
→ Check Gate 3 (model_explicit). Đang dùng Opus cho task đơn giản? Switch sang Haiku/Sonnet. Hoặc set `maxTurns: 10` để cap.

### "Memory không update"
→ Check Gate 8 (memory_instructions). Body có nhắc subagent update MEMORY.md không? Add explicit instruction.

## Output format

Report là markdown — print thẳng vào chat. Không lưu file (user có thể copy nếu muốn).