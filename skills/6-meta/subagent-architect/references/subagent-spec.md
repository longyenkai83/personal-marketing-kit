# Subagent Frontmatter Spec — Condensed Reference

> Source: https://code.claude.com/docs/en/sub-agents (fetched 2026-04-25). Skill load file này khi run BUILD/AUDIT.

## Format

Subagent = file `.md` với YAML frontmatter + system prompt body:

```markdown
---
name: <kebab-case>
description: <when to delegate>
tools: <comma-list or array>
model: <alias or full ID>
---

You are <role>. <instructions>
```

Frontmatter chỉ `name` và `description` là **required**. Mọi field khác optional với default tốt.

## 16 fields

| Field | Required | Type | Default | Purpose |
|---|---|---|---|---|
| `name` | ✅ | string | — | Unique identifier, kebab-case (lowercase + hyphens) |
| `description` | ✅ | string | — | Khi nào Claude delegate. Add "Use proactively when..." để auto-trigger |
| `tools` | ❌ | string\|array | inherit all | Allowlist. Comma-separated string hoặc array. |
| `disallowedTools` | ❌ | string\|array | — | Denylist. Áp dụng trước `tools`. |
| `model` | ❌ | enum\|string | `inherit` | `sonnet` / `opus` / `haiku` / `inherit` / full ID (`claude-opus-4-7`) |
| `permissionMode` | ❌ | enum | `default` | `default` / `acceptEdits` / `auto` / `dontAsk` / `bypassPermissions` / `plan` |
| `maxTurns` | ❌ | integer | unlimited | Maximum agentic turns trước khi stop |
| `skills` | ❌ | array | — | Skill names load vào context tại startup. Subagent KHÔNG inherit skills từ parent. |
| `mcpServers` | ❌ | array | inherit | Inline server config hoặc string reference. Inline servers chỉ scope trong subagent. |
| `hooks` | ❌ | object | — | Lifecycle hooks (PreToolUse / PostToolUse / Stop). Cleanup khi subagent finishes. |
| `memory` | ❌ | enum | — | `user` / `project` / `local`. Bật persistent memory directory. |
| `background` | ❌ | bool | `false` | Luôn run background (concurrent with main thread) |
| `effort` | ❌ | enum | inherit | `low` / `medium` / `high` / `xhigh` / `max`. Override session effort. |
| `isolation` | ❌ | enum | — | `worktree` để run trong git worktree riêng |
| `color` | ❌ | enum | — | `red` / `blue` / `green` / `yellow` / `purple` / `orange` / `pink` / `cyan` |
| `initialPrompt` | ❌ | string | — | Auto-submit làm first user turn khi run as `--agent` main session |

## Tool resolution

1. Bắt đầu từ pool: tất cả tools của parent (incl. MCP)
2. Apply `disallowedTools` (remove)
3. Apply `tools` (filter to allowlist)
4. Tool list trong cả 2 → bị remove

`tools` syntax đặc biệt:
- `Agent` (no parens) → cho phép spawn bất kỳ subagent nào (chỉ áp dụng khi main thread chạy via `--agent`)
- `Agent(worker, researcher)` → allowlist subagent types được spawn
- Subagent thường KHÔNG spawn được subagent khác (built-in restriction)

## Model resolution order

1. `CLAUDE_CODE_SUBAGENT_MODEL` env var (nếu set)
2. Per-invocation `model` parameter (Claude pass khi delegate)
3. Subagent definition's `model` frontmatter
4. Main conversation's model

## Scope priority (cao → thấp)

| Location | Scope | Priority |
|---|---|---|
| Managed settings | Org-wide | 1 (cao nhất) |
| `--agents` CLI flag | Session hiện tại | 2 |
| `.claude/agents/` | Project | 3 |
| `~/.claude/agents/` | All your projects | 4 |
| Plugin's `agents/` | Where plugin enabled | 5 (thấp nhất) |

Trùng tên → priority cao thắng.

## Permission mode behavior

| Mode | Behavior |
|---|---|
| `default` | Standard prompts |
| `acceptEdits` | Auto-accept file edits + filesystem commands trong working dir |
| `auto` | Background classifier review commands |
| `dontAsk` | Auto-deny prompts (explicitly allowed tools vẫn work) |
| `bypassPermissions` | Skip prompts (NGUY HIỂM — chỉ cho safe agent) |
| `plan` | Read-only exploration (plan mode) |

⚠️ Parent dùng `bypassPermissions`/`acceptEdits`/`auto` → override subagent's mode.

## Memory directories

| Scope | Location |
|---|---|
| `user` | `~/.claude/agent-memory/<name>/` |
| `project` | `.claude/agent-memory/<name>/` |
| `local` | `.claude/agent-memory-local/<name>/` |

Khi `memory` set:
- System prompt tự include first 200 lines hoặc 25KB của `MEMORY.md`
- `Read`/`Write`/`Edit` tools auto-enabled (cho memory management)

## Built-in subagents (không cần tự build)

- **Explore** (Haiku, read-only) — file discovery, code search
- **Plan** (inherit, read-only) — plan mode research
- **general-purpose** (inherit, all tools) — multi-step tasks
- **statusline-setup**, **Claude Code Guide** — auto-invoked

Skill này tập trung vào CUSTOM subagents bạn tự build.

## Gotchas

- Subagent KHÔNG inherit skills — phải list trong `skills:` field
- Subagent KHÔNG spawn subagent khác (no nesting)
- Plugin subagents KHÔNG hỗ trợ `hooks`/`mcpServers`/`permissionMode` (security)
- File mới ghi → cần restart session HOẶC chạy `/agents` để load
- `cd` trong subagent KHÔNG persist giữa Bash calls (mỗi call là shell mới)
- Forked subagents (experimental) = inherit full conversation, dùng `/fork` thay vì named subagent — yêu cầu `CLAUDE_CODE_FORK_SUBAGENT=1`

## Frontmatter examples

### Minimal
```yaml
---
name: my-agent
description: Use proactively for X. Returns Y.
---
```

### Read-only researcher
```yaml
---
name: codebase-explorer
description: Use proactively for codebase research. Read-only.
tools: Read, Grep, Glob
model: haiku
permissionMode: plan
color: blue
---
```

### Code modifier with hooks
```yaml
---
name: refactor-agent
description: Refactors code following project conventions
tools: Read, Edit, Write, Grep, Glob, Bash
model: sonnet
permissionMode: acceptEdits
color: green
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---
```

### Memory-enabled reviewer
```yaml
---
name: pattern-tracker
description: Tracks patterns across reviews. Use after each PR.
tools: Read, Grep, Glob, Bash
model: sonnet
memory: project
color: purple
---
```