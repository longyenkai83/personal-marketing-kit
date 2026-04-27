# Strategic Sampling Rules

KHÔNG phân tích hết toàn bộ comments. Filter & prioritize để tối ưu context window và giữ tín hiệu mạnh.

---

## Step 0 — Filter admin replies FIRST ⚠️ (critical)

**Exclude ALL comments where `profileName == page_owner_name`.**

Page owner thường reply dày trên posts của mình (9-15% tổng comments). Admin replies lẫn với user comments sẽ **làm skew toàn bộ analysis**:
- Admin ngôn ngữ khác user (teaching vs sharing pain)
- Admin đẩy link funnel → inflate promo signal
- Admin tag user → inflate tag-a-friend signal

**Cách xác định page_owner_name:**
- Scrape 1 post → lấy `author.name` của post owner
- Hoặc hỏi user confirm trước Phase 2

**Pipeline đã implement trong:** `scripts/sample.py` (param: `page_owner`)

⚠️ Admin replies KHÔNG nên vứt đi — lưu riêng để Phase 4 Enrichment decode admin voice.

## Step 1 — Loại noise (hard filter)

Exclude comments thỏa 1 trong các điều kiện:
- **Emoji-only** — không có text
- **<5 từ** — quá ngắn để có nội dung
- **Chỉ tag** — "@abc" không kèm text
- **Stickers-only**
- **Duplicate** — cùng author + cùng text trong 1 post (spam)
- **Obvious promo** — "DM em để mua", "Inbox shop X"
- **Bot-like** — pattern lặp lại

---

## Step 2 — Prioritize high-signal (keep 100%)

Giữ toàn bộ comments thỏa ÍT NHẤT 1 tiêu chí:

### 2.a — Top 5 posts by engagement
100% comments từ 5 posts có `commentsCount` cao nhất.
**Lý do:** Posts viral = content chạm nerve → comments ở đó có tín hiệu mạnh.

### 2.b — Comments dài (>15 từ)
Length là proxy cho emotional investment.
**Lý do:** Ai bỏ công viết dài = cái gì đó chạm thật.

### 2.c — Threaded replies depth ≥3
Reply của reply của reply.
**Lý do:** Tranh luận sâu = insight vàng. Bình thường chỉ reply 1 tầng.

### 2.d — Comments với >10 likes
Community đã vote giúp chị rằng insight này resonate.
**Lý do:** Social proof nội tại — comment hay → nhiều like.

### 2.e — Comments là câu hỏi (kết thúc `?`)
**Lý do:** FAQ pattern signal — mỗi ? có thể là 1 content idea.

---

## Step 3 — Random sample phần còn lại (10%)

Từ pool các comments không thỏa Step 2 (và đã qua Step 1 filter), lấy random 10% để giữ tính đại diện.

**Lý do:** Không bị bias 100% vào viral posts — vẫn nghe voice bình thường của ngách.

---

## Step 4 — Hard cap (context safety)

**Max 1,500 comments** cho phase 2 analysis (Claude context budget).

Nếu sau Step 1-3 vẫn > 1,500, áp priority:
1. Top engagement posts (100%)
2. Longest comments (desc)
3. Most-liked (desc)
4. Random fill đến đủ 1,500

---

## Step 5 — Report sampling stats cho user

Luôn in ra trước Phase 2:

```
📊 Sampling Report
Raw comments scraped: 4,235
Filtered out (Step 1): 1,820
  - Emoji-only: 340
  - <5 words: 890
  - Tags only: 210
  - Duplicates: 180
  - Promo/bot: 200
High-signal kept (Step 2): 1,250
  - Top 5 posts: 620
  - Long comments: 380
  - Threaded replies: 95
  - High-liked: 120
  - Questions: 35
Random sample (Step 3): 250
─────────────────────────
Total to analyze: 1,500 (capped)
Sampling confidence: HIGH

Estimated representativeness: ~88% of signal preserved, ~30% of volume
```

---

## Edge cases

- **Fanpage nhỏ (<500 raw comments):** Skip sampling, phân tích hết. Confidence = medium.
- **Fanpage ngoại ngữ:** Nhớ xét length threshold khác (tiếng Trung 5 ký tự ≠ 5 từ tiếng Việt).
- **Fanpage có nhiều spam comments:** Tighten Step 1 với keyword blocklist.
- **Post có >500 comments:** Cap 200/post để không bị 1 post lấn át data.
