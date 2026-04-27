---
name: hook-swipe-library
description: Search and remix proven viral hooks from curated banks (currently 72 Vietnamese hooks for women-biz-vn niche, sourced from Kallaway 18-topic × 4-temperature framework). Use when user needs to quickly find a hook by niche/topic/temperature/framework, remix existing hooks, or feed hook bank into content-engine Stage 3. Triggers — "tìm hook có sẵn", "swipe hook", "hook bank", "remix hook", "lấy hook viral".
allowed-tools: Read, Grep, Glob
argument-hint: "[niche] [filter: topic|temperature|framework]"
---

# Hook Swipe Library

Kho hook đã proven, organize theo niche → filter theo nhiều tag → quick remix cho dự án mới.

## When to invoke

VN trigger phrases:
- "tìm hook cho ngách [X]"
- "swipe hook viral"
- "lấy hook bank"
- "hook có sẵn cho [topic]"
- "remix hook"

User can also invoke `/hook-swipe-library` directly.

## Available banks (v1)

| Bank | Hooks | Niche | Source |
|------|-------|-------|--------|
| `women-biz-vn-72` | **72** | Phụ nữ KD VN đóng gói chuyên môn bán internet | Kallaway Bài Tập 9 — 18 topic × 4 temperature |

> **Roadmap mở rộng**: thêm bank khi có nguồn proven khác (vd: Maria Wendt 365 reel scripts, English viral hooks bundle, niche-specific banks).

## How to query

### Filter dimensions

Mỗi hook trong bank được tag theo 4 chiều:

| Dimension | Values |
|-----------|--------|
| **Topic group** | Nhận thức / Tâm lý / Hướng dẫn / Hành động |
| **Topic ID** | T1 → T18 (Bài Tập 9 numbering) |
| **Temperature** | lanh / am / nong / banhang |
| **Framework** | Contrarian / Investigator / Teacher / Experimenter / Fortune Teller / Case Study / Direct Offer |

### Query patterns

**Lấy theo niche + temperature**:
```
Đọc women-biz-vn-72.json → filter `temperature == "lanh"` → return all matching hooks
```

**Lấy theo topic group**:
```
Filter `topic_group == "Nhận thức"` → return 6 topics × 4 hooks = 24 hooks
```

**Lấy theo framework**:
```
Filter `framework == "Contrarian"` → return all Contrarian hooks across topics
```

**Combo filter**:
```
temperature=nong AND framework=Case Study → strongest social-proof hooks
```

## Workflow — Quick Remix

### Step 1: User specifies need
- Niche: women-biz-vn (default cho v1)
- Filter: vd "thị trường lạnh + nhóm Tâm lý"

### Step 2: Em query bank
- Đọc `banks/{bank-name}.json`
- Filter theo tag user cung cấp
- Return list candidate hooks

### Step 3: Present 3-5 candidates
- Format markdown dễ đọc
- Show topic, framework, full hook text, CTA
- Highlight tại sao mỗi hook phù hợp request

### Step 4: User chọn hook → em remix
- Giữ nguyên cấu trúc framework
- Thay variable theo context user (sản phẩm cụ thể, persona cụ thể)
- Trả về hook đã remix + explanation

### Step 5: Optional — feed vào content-engine
- Chuyển hook vào Stage 3 của `content-engine` để generate full caption + body
- Hoặc chuyển vào `kallaway-hook-master` worksheet để build full video plan

## Output Format

```markdown
## Hook Candidates — [filter description]

Bank: women-biz-vn-72 | Filtered: [N] hooks matched

### Candidate 1
**Topic**: T[X] — [topic title]
**Group**: [Nhận thức/Tâm lý/Hướng dẫn/Hành động]
**Temperature**: [lanh/am/nong/banhang]
**Framework**: [name]
**Hook**:
> "[full hook text]"

**CTA**: [original CTA]
**Use case**: [khi nào dùng phù hợp]

### Candidate 2
... (lặp 3-5 candidates)

## Em đề xuất

Hook [#X] phù hợp nhất vì [lý do].

Anh muốn:
- [ ] Remix hook này theo context cụ thể của anh
- [ ] Feed vào content-engine để gen full caption
- [ ] Feed vào kallaway-hook-master để gen video plan
```

## Integration

- **Called by**: `kallaway-hook-master` (khi cần inspiration), `content-engine` Stage 3 (khi cần seed hook bank)
- **Calls**: nothing (read-only skill)

## Bank Schema

Mỗi entry trong `banks/{name}.json` follow schema này:

```json
{
  "id": "wbiz_T1_lanh_contrarian",
  "topic_id": "T1",
  "topic_title": "Bạn giỏi nhưng chưa kiếm được tiền vì thiếu điều này",
  "topic_group": "Nhận thức",
  "temperature": "lanh",
  "framework": "Contrarian",
  "hook_text": "Bạn học nhiều, làm việc chăm chỉ...",
  "cta": "Comment 'THIẾU GÌ' để tôi chỉ cho bạn",
  "tags": ["chuyên môn", "monetize", "kiến thức"],
  "source": "Kallaway Bài Tập 9",
  "verified": true
}
```

## Adding new banks

Khi user bring tài liệu mới (vd: Maria Wendt's reel scripts, English hook bundle):

1. Em parse tài liệu → extract hooks individual
2. Tag theo schema (niche + temperature + framework + topic)
3. Save thành `banks/{niche-name}-{count}.json`
4. Update README/SKILL.md với bank mới

## Failure modes

- **Query không match hook nào** → suggest filter rộng hơn (drop 1 dimension)
- **Bank thiếu** cho niche user cần → recommend `kallaway-hook-master` để generate from scratch
- **Hook đã outdated** (vd: ref tool/trend cũ) → flag với `verified=false` trong JSON

## Status

**v1.0** — 1 bank (women-biz-vn-72) shipped. Mở rộng theo demand.
