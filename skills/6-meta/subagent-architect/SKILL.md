---
name: subagent-architect
description: Build (scaffold) hoặc audit (review) custom Claude Code subagents theo spec chính thức tại https://code.claude.com/docs/en/sub-agents. BUILD mode hỏi 6 câu trong 1 message rồi sinh file .md đúng spec, ghi vào ~/.claude/agents/ hoặc .claude/agents/. AUDIT mode review file có sẵn theo 10 best-practice gate. Vietnamese-first. Use when user says "tạo subagent", "build subagent", "audit subagent file", "review my subagent", "scaffold agent for X", "convert prompt to subagent", or invokes /subagent-architect.
---

# Subagent Architect

Skill nội bộ scaffold + audit Claude Code custom subagents — không cần đọc 1000 dòng doc mỗi lần.

## 2 modes

| Mode | Trigger | Output |
|---|---|---|
| **BUILD** | "tạo subagent...", "build subagent...", "scaffold agent..." | File `.md` ở `~/.claude/agents/` hoặc `.claude/agents/` |
| **AUDIT** | "audit subagent <path>", "review subagent file <path>" | Markdown report với schema check + 10 gate |

Default = BUILD nếu không rõ mode.

## Required environment

- Python 3 + PyYAML + jsonschema: `pip install pyyaml jsonschema`
- Windows: prefix Python commands với `PYTHONIOENCODING=utf-8`
- Sau khi tạo file mới, restart Claude Code session HOẶC chạy `/agents` để load subagent vào memory

## BUILD mode workflow

### Stage 1 — Discover (6 questions, 1 message)

Read first: `templates/prompt-discover.md`. Hỏi user 6 câu trong **1 message duy nhất** (không back-forth):

1. **Tên + 1 câu mô tả** — kebab-case + 1 câu khi nào dùng (ex: "code-reviewer — review code chất lượng + security sau khi viết xong")
2. **Scope** — `project` (`.claude/agents/`, share team qua git) hay `user` (`~/.claude/agents/`, dùng across projects của bạn)?
3. **Read-only hay can modify?** — driver chính cho `tools` + `model`
4. **Auto-trigger hay explicit?** — auto thì description bắt đầu bằng "Use proactively when..."; explicit thì user phải @-mention
5. **Memory needed?** — nếu yes → scope nào (`user`/`project`/`local`)?
6. **Anti-patterns / guard rails** — subagent KHÔNG được làm gì? (ex: "không bao giờ chạy `git push`", "không edit file ngoài thư mục `src/`")

Nếu user trả lời thiếu, suy luận default theo `templates/prompt-recommend.md`.

### Stage 2 — Recommend config

Read first: `references/best-practices.md` + `templates/prompt-recommend.md`. Apply mapping rules:

- **Read-only research** → `tools: Read, Grep, Glob` + `model: haiku` + `permissionMode: plan` + `color: blue`
- **Read-only + bash queries** → `tools: Read, Grep, Glob, Bash` + `model: haiku` + `color: cyan`
- **Code modify** → `tools: Read, Edit, Write, Grep, Glob, Bash` + `model: sonnet` + `color: green`
- **Heavy reasoning / architecture** → `model: opus` + `color: purple`
- **Auto-trigger** → description prefix "Use proactively when..."
- **Memory** → `project` mặc định (share qua git); `user` nếu cross-project; `local` nếu private

### Stage 3 — Generate file

Read first: `references/subagent-spec.md` + `references/example-subagents.md`. Build file:

- Frontmatter chỉ điền **required + relevant optional fields** — không over-spec (mọi field optional bỏ qua sẽ dùng default tốt)
- Body system prompt theo cấu trúc 4 sections:
  1. **Role** — "You are X" / "Bạn là X"
  2. **When invoked** — numbered procedure (3-7 steps)
  3. **Output format** — cụ thể về cách trả về kết quả
  4. **Constraints** — guard rails từ Q6
- Show file content lên chat trước khi ghi disk
- Ghi vào path đúng theo scope chọn ở Q2

### Stage 4 — Validate + smoke test

```bash
PYTHONIOENCODING=utf-8 python scripts/validate.py <path-to-new-file.md>
```

Nếu schema fail hoặc <8/10 gate pass → fix và retry. Show user tóm tắt kết quả + lời khuyên restart session để Claude Code load subagent mới.

## AUDIT mode workflow

User cung cấp đường dẫn file `.md` (ex: `~/.claude/agents/foo.md`).

```bash
PYTHONIOENCODING=utf-8 python scripts/validate.py <path>
```

Skill đọc output của validate.py, parse, render thành report VN-friendly:

```markdown
# Audit: {agent-name}

## Schema validation
{✅ valid / ❌ errors with field path}

## Best practice gates (10)
{✅/⚠️ each with reason}

## Recommendations
- **Critical**: {fail gates}
- **Improvement**: {warning gates}
- **Optional**: {info gates}
```

## Files in this skill

```
subagent-architect/
├── SKILL.md                              # this file
├── README.md                             # cách dùng + cài đặt
├── references/
│   ├── subagent-spec.md                  # 16 frontmatter fields, gọn
│   ├── best-practices.md                 # 10 gates với lý do
│   └── example-subagents.md              # 4 examples từ official doc
├── templates/
│   ├── prompt-discover.md                # 6 câu hỏi Stage 1
│   ├── prompt-recommend.md               # mapping rules Stage 2
│   └── prompt-audit.md                   # checklist Stage AUDIT
├── schemas/
│   └── subagent.schema.json              # validate frontmatter
├── scripts/
│   └── validate.py                       # YAML + schema + 10 gates
└── examples/
    └── readonly-researcher.md            # full example
```

## Output language

VN cho mọi giao tiếp với user. Generated subagent file VN hay EN tùy user preference (mặc định VN cho user VN).

## Stage gate cứng

- BUILD: Stage 4 phải pass schema. <8/10 gate → cảnh báo nhưng cho phép user override.
- AUDIT: report luôn show, kể cả khi pass hết.

## Common patterns

- "Tạo subagent X cho task Y" → BUILD mode
- "Review file ~/.claude/agents/foo.md" → AUDIT mode
- "Convert prompt này thành subagent" → BUILD mode, parse prompt làm seed cho Q1+Q3
- "Subagent của tôi không trigger" → AUDIT mode, focus gate description_clear + auto_trigger_signal