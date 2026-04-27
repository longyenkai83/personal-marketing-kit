# Stage 2 Prompt — Recommend Config (BUILD mode)

> Internal prompt Stage 2. Input = `discovered` block từ Stage 1. Output = recommended frontmatter values.

## Mapping rules

### Capability → tools + model + permissionMode

| `discovered.capability` | tools | model | permissionMode | color |
|---|---|---|---|---|
| `read-only` (file research only) | `Read, Grep, Glob` | `haiku` | `plan` | `blue` |
| `read-only` (+ bash queries) | `Read, Grep, Glob, Bash` | `haiku` | (default) | `cyan` |
| `modify` (code) | `Read, Edit, Write, Grep, Glob, Bash` | `sonnet` | `acceptEdits` | `green` |
| `modify` (with destructive ops) | `Read, Edit, Write, Grep, Glob, Bash` | `sonnet` | (default) — keep prompts | `yellow` |
| `reasoning-heavy` (architecture/security) | `Read, Grep, Glob, Bash` | `opus` | `plan` | `purple` |
| `specialty` (SQL/data/MCP-heavy) | tùy task — list explicit | `sonnet` | (default) | `cyan` |

### Trigger → description prefix

| `discovered.trigger` | Description style |
|---|---|
| `auto` | Bắt đầu bằng "Use proactively when..." hoặc "Automatically invoked when..." |
| `explicit` | Mô tả khả năng, không có "proactively" — user sẽ @-mention |

### Memory → memory + body instructions

Nếu `discovered.memory != "none"`:
- Set `memory: <scope>` trong frontmatter
- Add 2-3 dòng vào body: "Update your agent memory as you discover patterns, library locations, and key architectural decisions. Write concise notes to MEMORY.md."

### Anti-patterns → constraints section trong body

Mỗi anti-pattern → 1 dòng trong "## Constraints" section của system prompt:

```markdown
## Constraints
- Never <anti-pattern 1>
- Never <anti-pattern 2>
- If asked to <forbidden action>, decline and explain you're not authorized for that.
```

## Body structure (4 sections)

System prompt body luôn có 4 sections theo thứ tự:

```markdown
You are <role from one_line_purpose>.

## When invoked
1. <step 1>
2. <step 2>
3. <step 3>
...

## Output format
<cụ thể về cách trả về kết quả — markdown sections, fields, etc.>

## Constraints
- <guard rail từ anti_patterns>
- <other safety rules>
```

## Generate frontmatter — chỉ include relevant fields

⚠️ Nguyên tắc: chỉ điền field có ý nghĩa thay đổi behavior. Skip fields giữ default.

Required:
- `name` ← `discovered.name`
- `description` ← compose từ `one_line_purpose` + trigger style

Conditional:
- `tools` ← từ mapping table
- `model` ← từ mapping table
- `permissionMode` ← từ mapping table (chỉ set nếu khác `default`)
- `memory` ← chỉ nếu `discovered.memory != "none"`
- `color` ← từ mapping table (semantic)

Skip mặc định (chỉ thêm khi user yêu cầu cụ thể):
- `disallowedTools` (đã handle qua `tools` allowlist)
- `maxTurns` (default unlimited là tốt)
- `skills` (advanced — explicit only)
- `mcpServers` (advanced)
- `hooks` (advanced — chỉ thêm khi user yêu cầu validation)
- `background` (default false là tốt)
- `effort` (inherit là tốt)
- `isolation` (chỉ khi multi-task parallel)
- `initialPrompt` (chỉ cho `--agent` main session)

## Output sang Stage 3

Trước Stage 3, format:

```yaml
recommended:
  frontmatter:
    name: <name>
    description: <1-2 câu, có "Use proactively" nếu auto>
    tools: <comma-list>
    model: <alias>
    permissionMode: <mode>  # nếu khác default
    memory: <scope>          # nếu cần
    color: <color>
  body_outline:
    role: "You are <role>."
    procedure_steps: [step1, step2, step3, ...]
    output_format: <description>
    constraints: [c1, c2, ...]
```

Stage 3 sẽ render thành full markdown file.