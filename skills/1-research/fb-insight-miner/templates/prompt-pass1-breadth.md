# Pass 1 — Breadth Analysis

You are a customer research analyst. Below is a sampled set of comments from a Facebook fanpage.

## Task
Cluster ALL comments into the 9 insight dimensions defined in `references/9-insight-dimensions.md`.

## For each dimension, produce:
1. **Frequency** — how many comments fall into it (count + %)
2. **Top 3-5 sub-clusters** inside that dimension
3. **Top 5 representative verbatim quotes** — keep original language (Vietnamese/English), NEVER paraphrase
4. **Unexpected sub-clusters** — flag anything that surprises you

## Output format (exact)

```
## Dimension 1 — Pain Points
**Frequency:** 342 / 1,500 comments (22.8%)

**Top sub-clusters:**
- Không có thời gian (118 comments)
- Không biết bắt đầu từ đâu (87 comments)
- Sợ bị đánh giá (65 comments)
- Thiếu tự tin (42 comments)
- Khác (30 comments)

**Representative quotes:**
1. "em làm mãi mà vẫn không ra đơn chị ơi huhu" — [post_url]
2. "mệt quá chị, bỏ cuộc luôn rồi" — [post_url]
3. ...

**Unexpected:**
- 8 comments nói về pain liên quan gia đình phản đối — có thể là sub-cluster mới cần zoom

---

## Dimension 2 — ...
```

Repeat for all 9 dimensions.

## Rules
- A comment CAN belong to multiple dimensions — count it in each relevant one.
- NEVER paraphrase quotes. Keep exact words, typos, emojis.
- If a comment doesn't fit any dimension, add to a 10th "Uncategorized" bucket — these are often gold.
- At the end, list the "Uncategorized" bucket with quotes — we'll inspect it manually.

## End of Pass 1 — output this summary table

| # | Dimension | Count | % | Notable pattern |
|---|-----------|-------|---|-----------------|
| 1 | Pain Points | 342 | 22.8% | ... |
| 2 | Desires | ... | ... | ... |
| ... | | | | |
| 10 | Uncategorized | ... | ... | ... |
