# Stage 1 Prompt — Discover (BUILD mode)

> Internal prompt skill load tại Stage 1 BUILD. Hỏi user 6 câu trong **1 message duy nhất**, không back-forth.

## Cách hỏi

Format câu hỏi cho user (gộp vào 1 message, không hỏi từng câu):

---

**Em cần 6 thông tin để scaffold subagent đúng spec:**

1. **Tên + 1 câu mô tả task** — kebab-case + 1 câu khi nào dùng
   *Ví dụ: "code-reviewer — review code chất lượng + security sau khi viết xong"*

2. **Scope** — chọn 1:
   - `project` (`.claude/agents/`) — share team qua git
   - `user` (`~/.claude/agents/`) — chỉ máy của bạn, dùng across mọi project

3. **Read-only hay can modify code?** — driver chính cho `tools` + `model`
   - Read-only research → tools restricted, model = haiku
   - Modify code → có Edit/Write, model = sonnet
   - Heavy reasoning (architecture/security) → model = opus

4. **Auto-trigger hay explicit?**
   - Auto: Claude tự delegate khi gặp task phù hợp (description có "Use proactively when...")
   - Explicit: chỉ run khi user @-mention hoặc nói rõ tên

5. **Memory needed?** — subagent có cần học qua nhiều conversation không?
   - No (default) — bỏ field
   - Yes → scope nào: `project` (share git) / `user` (cross-project) / `local` (private)

6. **Anti-patterns / guard rails** — subagent KHÔNG được làm gì?
   *Ví dụ: "không bao giờ chạy `git push`", "không edit file ngoài thư mục `src/`", "không gọi external API"*

---

## Defaults nếu user không trả lời

Apply defaults và thông báo cho user:

| Câu | Default |
|---|---|
| 1 (tên) | Suy luận từ task description |
| 2 (scope) | `user` |
| 3 (read/modify) | Read-only |
| 4 (trigger) | Auto-trigger ("Use proactively...") |
| 5 (memory) | No |
| 6 (anti-patterns) | "Subagent stays focused on stated task only" |

## Edge cases

- User trả lời gộp 2-3 ý vào 1 câu → parse ra từng field, không yêu cầu format chuẩn
- User nói "tạo subagent giống code-reviewer nhưng cho Vietnamese" → load Pattern 1 từ `references/example-subagents.md`, swap language only
- User cung cấp prompt sẵn → parse prompt làm seed cho Q1+Q3, hỏi 4 câu còn lại

## Output sang Stage 2

Trước khi sang Stage 2, summarize 6 câu trả lời thành 1 block:

```yaml
discovered:
  name: <kebab-case>
  one_line_purpose: <1 câu>
  scope: project | user
  capability: read-only | modify | reasoning-heavy
  trigger: auto | explicit
  memory: none | user | project | local
  anti_patterns: [<list các điều subagent không được làm>]
```