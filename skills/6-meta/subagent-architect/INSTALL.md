# Cài đặt Subagent Architect skill

## Yêu cầu môi trường
- Claude Code (CLI / VSCode extension / JetBrains extension / desktop app)
- Python 3.8+
- pip

## Bước 1 — Giải nén vào thư mục skill

Giải nén `subagent-architect.zip` sao cho thư mục `subagent-architect/` nằm bên trong **một trong hai** vị trí:

| Vị trí | Scope | Khi nào dùng |
|---|---|---|
| `~/.claude/skills/subagent-architect/` | **User** | Dùng được trên mọi project của bạn |
| `<your-project>/.claude/skills/subagent-architect/` | **Project** | Chỉ dùng trong project này, share team qua git |

**Windows path tương đương:**
- User: `C:\Users\<username>\.claude\skills\subagent-architect\`
- Project: `<project>\.claude\skills\subagent-architect\`

Cấu trúc cuối cùng phải là:
```
.claude/skills/subagent-architect/
├── SKILL.md
├── README.md
├── INSTALL.md
├── requirements.txt
├── references/
├── templates/
├── schemas/
├── scripts/
└── examples/
```

## Bước 2 — Cài Python deps

```bash
cd ~/.claude/skills/subagent-architect
pip install -r requirements.txt
```

Hoặc cài thẳng:
```bash
pip install pyyaml jsonschema
```

## Bước 3 — Reload skills trong Claude Code

Có 2 cách:
- **Restart** Claude Code session, HOẶC
- Gõ `/skills` trong session đang chạy (skill sẽ load mới ngay)

## Bước 4 — Smoke test

Trong Claude Code session, gõ:
```
audit subagent file ~/.claude/skills/subagent-architect/examples/readonly-researcher.md
```

Skill sẽ chạy và trả về report `8/8 gates passed` + verdict `Production-ready`. Nếu thấy report → cài đặt thành công.

Hoặc test thủ công:
```bash
cd ~/.claude/skills/subagent-architect
PYTHONIOENCODING=utf-8 python scripts/validate.py examples/readonly-researcher.md
```

## Bước 5 — Sử dụng

| Mode | Trigger |
|---|---|
| **BUILD** (tạo subagent mới) | "tạo subagent code-reviewer cho ..." / "build subagent X" |
| **AUDIT** (review file có sẵn) | "audit subagent file <path>" / "review subagent <path>" |

Xem `README.md` + `SKILL.md` để biết chi tiết.

---

## English quick install

1. **Extract** `subagent-architect.zip` so `subagent-architect/` ends up inside `~/.claude/skills/` (user scope) or `<project>/.claude/skills/` (project scope).
2. **Install** Python deps: `pip install pyyaml jsonschema`
3. **Reload** Claude Code: restart session OR run `/skills`.
4. **Test** by saying: `"audit subagent file ~/.claude/skills/subagent-architect/examples/readonly-researcher.md"`.
5. **Trigger** the skill: "tạo subagent ..." (Vietnamese) or "build subagent ..." (English) for BUILD mode; "audit subagent file <path>" for AUDIT mode.

## Troubleshooting

- **Skill không tự kích hoạt** → Restart session HOẶC chạy `/skills`. Verify `SKILL.md` có YAML frontmatter `name: subagent-architect` đúng.
- **`ModuleNotFoundError: pyyaml`** → `pip install pyyaml jsonschema` chưa chạy, hoặc Python interpreter Claude Code dùng khác với pip bạn vừa chạy. Tìm interpreter Claude Code dùng + cài đúng vào đó.
- **Lỗi encoding VN trên Windows** → Prefix mọi `python` command với `PYTHONIOENCODING=utf-8`.
- **Subagent vừa tạo bằng skill nhưng Claude Code không thấy** → Sau khi BUILD ghi file mới vào `~/.claude/agents/` hoặc `.claude/agents/`, restart session HOẶC gõ `/agents` để load.

## Uninstall

Xóa thư mục:
```bash
rm -rf ~/.claude/skills/subagent-architect
```

Hoặc trên Windows: xóa folder `C:\Users\<username>\.claude\skills\subagent-architect\` trong File Explorer.

## Source

Skill này build dựa trên [Claude Code official subagent docs](https://code.claude.com/docs/en/sub-agents). Khi spec thay đổi, file `references/subagent-spec.md` cần update tương ứng.