# Subagent Best Practices — 10 Gates

> Áp dụng khi BUILD và check khi AUDIT. Mỗi gate đều có lý do gắn với official doc — không phải opinion.

## Tip cốt lõi từ doc

> - **Design focused subagents** — mỗi subagent excel ở 1 task duy nhất
> - **Write detailed descriptions** — Claude dùng description để decide khi nào delegate
> - **Limit tool access** — chỉ grant permissions cần thiết
> - **Check into version control** — share project subagents với team

10 gate dưới đây expand các nguyên tắc trên thành check cụ thể.

---

## Gate 1 — `description_clear`

**Yêu cầu:** `description` ≥ 30 ký tự, mô tả rõ KHI NÀO Claude nên delegate.

**Lý do:** Doc nói "Claude uses each subagent's description to decide when to delegate tasks. When you create a subagent, write a clear description so Claude knows when to use it." Description thiếu → Claude không bao giờ tự delegate, user phải @-mention thủ công.

**Pass examples:**
- "Expert code reviewer. Use proactively after code changes. Focuses on security + best practices."
- "Debugging specialist for errors and test failures. Use when stack trace appears."

**Fail examples:**
- "Helper agent" (quá generic)
- "Reviews stuff" (không rõ stuff là gì)

---

## Gate 2 — `tools_restricted`

**Yêu cầu:** Có 1 trong 2: `tools` (allowlist) HOẶC `disallowedTools` (denylist) trong frontmatter.

**Lý do:** Default = inherit ALL tools từ parent. An toàn + focus → restrict explicit. Doc: "Limit tool access: grant only necessary permissions for security and focus."

**Pass:** `tools: Read, Grep, Glob` (read-only researcher) hoặc `disallowedTools: Write, Edit` (no-edit policy).

**Fail:** Không có cả 2 field → subagent inherit Write/Edit/Bash kể cả khi không cần.

---

## Gate 3 — `model_explicit`

**Yêu cầu:** `model` field set (không để default).

**Lý do:** Default = `inherit`, dùng cùng model với main conversation. Nhưng:
- Subagent read-only → Haiku đủ (rẻ + nhanh hơn 4-5x)
- Subagent reasoning phức tạp → Opus tốt hơn
- Để inherit = bỏ qua cơ hội control cost. Doc: "Control costs by routing tasks to faster, cheaper models like Haiku."

**Pass:** `model: haiku` / `model: sonnet` / `model: opus` / `model: claude-opus-4-7`.

**Fail:** Không set field.

---

## Gate 4 — `role_defined`

**Yêu cầu:** System prompt body có "You are X" hoặc "Bạn là X" (role definition).

**Lý do:** Subagent receives ONLY system prompt + basic env (không có Claude Code base prompt). Không có role → subagent không biết identity của mình. Pattern này xuất hiện trong **mọi** example của doc.

**Pass:**
- "You are a senior code reviewer ensuring high standards..."
- "Bạn là chuyên gia debugger chuyên về root cause analysis..."

**Fail:** Bắt đầu thẳng bằng "When invoked..." mà không có role.

---

## Gate 5 — `procedure_present`

**Yêu cầu:** System prompt có **numbered procedure** (ít nhất 3 bước "1. ... 2. ... 3. ...").

**Lý do:** Doc's reference examples (code-reviewer, debugger, data-scientist) đều có "When invoked: 1. ... 2. ..." structure. Subagent fresh context → cần explicit roadmap. Không có procedure → subagent improvise → output không nhất quán.

**Pass:**
```
When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately
```

**Fail:** Body chỉ có description chung chung, không có "1. 2. 3." hoặc "When invoked:" / "Khi:".

---

## Gate 6 — `description_concise`

**Yêu cầu:** `description` ≤ 500 ký tự.

**Lý do:** Description hiển thị trong agent picker UI + Claude scan để decide delegation. Quá dài → noise → Claude khó đọc + UX kém. Examples trong doc đều ≤ 200 chars.

**Pass:** Description 1-3 câu súc tích.

**Fail:** Description copy-paste full instructions vào (đó là việc của system prompt body, không phải description).

---

## Gate 7 — `body_substantive`

**Yêu cầu:** System prompt body ≥ 30 từ.

**Lý do:** Subagent CHỈ có system prompt làm context. Body 1-2 câu → subagent không có hướng dẫn đủ → improvise → kết quả tệ.

**Pass:** Body có role + procedure + output format + constraints (≥ 50 từ thường tốt).

**Fail:** Body chỉ "You are a reviewer." rồi hết.

---

## Gate 8 — `memory_instructions` (conditional)

**Yêu cầu:** Nếu `memory` field set, body PHẢI có instructions về cách subagent update MEMORY.md.

**Lý do:** Doc khuyến cáo: "Include memory instructions directly in the subagent's markdown file so it proactively maintains its own knowledge base." Không có instructions → memory directory tồn tại nhưng subagent không update → memory rỗng vĩnh viễn.

**Pass example:**
```
Update your agent memory as you discover patterns, library locations,
and key architectural decisions. Write concise notes about what you found.
```

**Fail:** `memory: project` set nhưng body không nhắc đến memory/knowledge update.

---

## Gate 9 — `auto_trigger_signal` (info)

**Yêu cầu:** Nếu user muốn auto-delegate, description có cụm "Use proactively" / "automatically" / "use immediately when".

**Lý do:** Doc: "To encourage proactive delegation, include phrases like 'use proactively' in your subagent's description field." Không có cụm này → user phải @-mention thủ công.

**Note:** Đây là info gate — không fail. Một số subagent THÍCH explicit-only (không muốn auto-trigger), khi đó signal này không phù hợp.

---

## Gate 10 — `no_wildcard_misuse`

**Yêu cầu:** `tools` field KHÔNG có `*` (asterisk wildcard).

**Lý do:** Claude Code `tools` syntax không hỗ trợ `*`. Một số user copy syntax từ shell glob → invalid. Để inherit all → bỏ field. Để allowlist → list explicit.

**Fail examples:**
- `tools: *` (invalid — bỏ field nếu muốn inherit all)
- `tools: Read, Edit*, Bash` (invalid — không có wildcard giữa name)

---

## Anti-patterns thường gặp (KHÔNG là gate nhưng nên tránh)

### A1 — Multi-purpose subagent
"reviewer-and-debugger-and-test-runner" → fail principle "design focused subagents". Tách thành 3 subagent nhỏ.

### A2 — Description ngược nghĩa
"This subagent does X but only when Y. Actually sometimes Z..." → Claude khó parse. Mỗi description nên 1 use case rõ ràng.

### A3 — Permission mode bypass cho task không an toàn
`permissionMode: bypassPermissions` cho subagent chạy `git push` / DB writes / xóa file → không an toàn. Chỉ bypass cho subagent đọc + safe queries.

### A4 — Model = opus cho task đơn giản
File search dùng Opus = đốt tiền. Read-only research → Haiku đủ.

### A5 — Memory enabled cho one-shot task
Memory để build knowledge across conversations. One-shot reviewer không cần. Bỏ `memory` field.

### A6 — Hook block mọi thứ
Hook PreToolUse với regex quá khắt khe → subagent stuck. Test hook script kỹ trước khi commit.

### A7 — initialPrompt cho subagent
`initialPrompt` chỉ áp dụng khi agent run as MAIN session via `--agent`. Subagent thông thường (delegate qua Task tool) không dùng field này — bỏ qua.