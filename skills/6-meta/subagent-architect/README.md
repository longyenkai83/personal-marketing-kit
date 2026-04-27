# Subagent Architect

> Skill nội bộ. Scaffold + audit Claude Code custom subagents nhanh — dựa trên [official spec](https://code.claude.com/docs/en/sub-agents).

## Bạn nhận được gì

```
[BUILD mode]
   IN  : 6 câu trả lời (tên / scope / read-only-or-modify / trigger / memory / anti-patterns)
   OUT : file .md ở ~/.claude/agents/<name>.md hoặc .claude/agents/<name>.md
        (frontmatter + system prompt structured đúng spec)

[AUDIT mode]
   IN  : đường dẫn file subagent .md
   OUT : markdown report — schema validation + 10 best-practice gates + recommendations
```

## Trigger phrases

Skill tự kích hoạt khi nói:
- "tạo subagent ..." / "build subagent ..."
- "scaffold agent cho ..."
- "audit subagent <path>" / "review subagent file <path>"
- "convert prompt này thành subagent"

Hoặc: `/subagent-architect`

## Cài đặt phụ thuộc

```bash
pip install pyyaml jsonschema
```

(Windows: prefix mọi `python` với `PYTHONIOENCODING=utf-8` để tránh lỗi VN/emoji.)

## Quick test

```bash
# Validate example mẫu
PYTHONIOENCODING=utf-8 python scripts/validate.py examples/readonly-researcher.md
```

Output mong đợi: schema valid + 10/10 gates passed.

## Khi vừa tạo subagent xong

Subagents được load tại session start. Sau khi BUILD ghi file mới:
1. Restart Claude Code session, HOẶC
2. Chạy `/agents` để load ngay (không cần restart)

## Folder structure

```
subagent-architect/
├── SKILL.md                          # entry point — Claude Code đọc trước
├── README.md                         # bạn đang đọc
├── references/
│   ├── subagent-spec.md              # 16 frontmatter fields condensed
│   ├── best-practices.md             # 10 gates + lý do
│   └── example-subagents.md          # 4 ví dụ từ official doc
├── templates/
│   ├── prompt-discover.md            # 6 câu hỏi BUILD Stage 1
│   ├── prompt-recommend.md           # mapping rules Stage 2
│   └── prompt-audit.md               # AUDIT checklist
├── schemas/
│   └── subagent.schema.json          # JSON schema cho frontmatter
├── scripts/
│   └── validate.py                   # YAML parse + schema + 10 gates
└── examples/
    └── readonly-researcher.md        # 1 ví dụ end-to-end
```

## 10 best-practice gates trong AUDIT

1. **description_clear** — ≥30 chars, đủ để Claude biết khi nào delegate
2. **tools_restricted** — `tools` hoặc `disallowedTools` set (không inherit hết)
3. **model_explicit** — `model` field set
4. **role_defined** — system prompt có "You are/Bạn là"
5. **procedure_present** — system prompt có numbered steps
6. **description_concise** — ≤500 chars (không phải copy paste cả doc)
7. **body_substantive** — system prompt ≥30 words
8. **memory_instructions** — nếu memory enabled, body có instructions update
9. **auto_trigger_signal** — info: "Use proactively" có/không trong description
10. **no_wildcard_misuse** — tools field không có `*` (không phải syntax đúng)

## Limitations

- Không tự ghi đè file đã có (sẽ cảnh báo + xin xác nhận)
- Không tạo plugin subagents (cần plugin manifest riêng)
- Không setup hooks/MCP servers — generate frontmatter có placeholder cho user fill
- VN-first, EN output cũng được nhưng prompt skill là VN