# Workflow D — Customer Research (45 phút, ~$4 cost)

> **Goal**: Đào REAL customer insight từ FB fanpage đối thủ → update niche-pack với verbatim mới
> 
> **Best for**: Quarterly refresh hoặc khi launch sản phẩm mới với niche khác

---

## 🎯 Outcome target

Sau 45 phút:
- ✅ 50-page Customer Insight Report từ 1 fanpage VN target
- ✅ 9 insight dimensions covered (pain / desire / objection / vocab / FAQ / etc)
- ✅ 30+ verbatim quotes (chữ thật của khách)
- ✅ Updated niche-pack với "observed" tags (thay vì "assumed")
- ✅ 5-10 hook ideas mới based on real pain points

---

## 💰 Cost transparency

| Item | Cost |
|------|------|
| Apify MCP API ($4 cho standard depth = 50 posts + 1500 comments) | $4 |
| Claude Code AI tokens (sample + analyze) | $0.50-1 |
| **Total** | **~$4-5** |

→ Ít hơn 1 buổi consult chuyên gia 2tr. Insight quality 10x.

---

## 📋 6-Phase Process

### Phase 0: Setup Apify MCP (one-time, 15 phút)

→ Skip nếu đã setup. Otherwise:

1. Tạo Apify account (free): https://apify.com
2. Get API token (Settings → Integrations)
3. Setup Apify MCP cho Claude Code:
   - Edit `~/.claude/settings.json` (hoặc IDE settings)
   - Add Apify MCP server config
   - Test connection: gõ "List my Apify actors" trong Claude Code

→ Detail setup: see `skills/1-research/fb-insight-miner/SKILL.md`

### Phase 1: Identify target fanpage (5 phút)

Pick 1 FB fanpage:
- ✅ Public (KHÔNG profile cá nhân)
- ✅ Active (≥30 posts trong 90 ngày qua)
- ✅ Match niche của anh chị (cùng audience target)
- ✅ Comments active (≥50 comments tổng)

**Examples cho phụ nữ KD VN niche**:
- Linh Phan (parenting/family)
- Phi Vân (business/career)
- Thái Vân Linh (business/leadership)
- Other coaches / KOLs trong ngành của anh chị

⚠️ **Avoid**: 
- Adult/sensitive niche (FB filter comments → ít data)
- Brand pages (less personal voice)

### Phase 2: Run fb-insight-miner (20-30 phút auto)

Open Claude Code → gõ:

```
Apply fb-insight-miner.

Fanpage URL: https://www.facebook.com/[fanpage-slug]
Depth: standard (50 posts, 1500 comments, ~$4)
Days window: 90 days
Output: chat (or 'file' to save markdown)
```

AI sẽ run 5-phase pipeline tự động:
1. **Preflight** — verify URL + cost confirmation
2. **Phase 1 Collect** — Apify scrape posts + top 20 posts + comments
3. **Phase 2 Sample** — Python pipeline filter + compact JSON
4. **Phase 3 Analyze** — 3-pass AI (breadth + depth + synthesis)
5. **Phase 4 Enrich** — 6 micro-reports
6. **Phase 5 Report** — final markdown

→ AI sẽ ask confirm cost trước Phase 1 → anh chị OK → proceed.

### Phase 3: Review insight report (5 phút)

AI output 50-page markdown report covering:

#### 9 Insight Dimensions
1. **Pain points** (functional / emotional / social) với severity tags
2. **Desires** (required / expected / desired / unexpected)
3. **Objections** (price / time / trust / etc)
4. **FAQ patterns** (questions audience hay hỏi)
5. **Vocabulary** (verbatim words, phrases, slang)
6. **Self-labels** (cách audience tự gọi mình)
7. **Metaphors** (analogies họ hay dùng)
8. **Emotional triggers** (gì làm họ engage)
9. **Silent signals** (tag-a-friend patterns, save patterns, etc)

#### 6 Bonus Micro-Reports
1. Admin voice decoding (page owner's reply patterns)
2. Top commenters → DM outreach list
3. Deep thread conversations
4. N-gram analysis — repeat VoC phrases
5. Tag-a-friend mechanic detection
6. Emoji-emotion fingerprint per post

### Phase 4: Extract verbatim (5 phút)

From report, extract:
- 20-30 verbatim quotes (chữ thật của khách)
- 10-20 self-labels (cách họ gọi mình)
- 10-15 repeated words/phrases (vocab)
- 5-10 metaphors (cách họ ví von)

→ Save vào working doc.

### Phase 5: Update niche-pack (5 phút)

Open `~/.claude/shared/niche-packs/women-biz-vn.json` (hoặc niche pack relevant).

Update:
- `voice.verbatim_bank` — add 10-20 quotes mới
- `voice.repeated_words` — add 5-10 words mới
- `voice.self_labels` — add 5 labels mới
- `pains_priors` — promote some from `confidence: assumed` → `confidence: observed` (with `source_ref` = fanpage URL)
- `gains_priors` — promote where applicable

Save updated JSON.

### Phase 6: Generate fresh hooks (5 phút)

```
Apply kallaway-hook-master.

Use updated niche-pack women-biz-vn.json (verbatim bank vừa update).
Generate 10 hook variants targeting top 3 pain points discovered.

For each hook:
- Embed ≥1 verbatim quote OR vocab word từ verbatim bank
- Apply 11 framework Kallaway
- Output ready-to-shoot
```

→ Output 10 hook FRESH với data thật từ market — much higher quality vs hook generic.

---

## 📊 ROI Math

### Without Workflow D (assume only)
- Niche-pack `assumed` priors → hook generic
- Engagement rate ~2%
- 10 reels/tháng × 1k reach = 200 engagements

### With Workflow D (verbatim observed)
- Niche-pack `observed` priors with real verbatim
- Hook resonate stronger → engagement rate 4-6%
- 10 reels/tháng × 1k reach = 400-600 engagements

→ **2-3x engagement** với same effort + 1 quarterly research.

→ **Cost-effective**: $4 quarterly = $16/year for 2-3x engagement boost.

---

## 🎯 Quarterly Schedule

| Quarter | Action |
|---------|--------|
| Q1 (Jan-Mar) | Run fb-insight-miner cho fanpage chính. Update niche-pack v1.1. |
| Q2 (Apr-Jun) | Run cho fanpage đối thủ #2. Cross-check với Q1 patterns. |
| Q3 (Jul-Sep) | Run cho fanpage Maria-style international (translation buffer). |
| Q4 (Oct-Dec) | Run cho fanpage emerging trend. Update niche-pack v1.2. |

→ **Total cost/year**: ~$16 (4 × $4) for full year of fresh customer insight.

---

## 💡 Pro Tips

### Tip 1: Pick fanpage smaller fast-grow over big-old
- Big fanpage (100k+ followers): comments diluted, lots of fan/spam
- Small fast-grow (5-20k followers, growing 20%+ monthly): comments concentrated, real engaged audience
→ Better insight signal trong small fanpage.

### Tip 2: Cross-reference 2-3 fanpages
1 fanpage = 1 perspective. 3 fanpages cùng niche = pattern emerge.
- Nếu pain "yếu công nghệ" xuất hiện ở 3/3 fanpages → STRONG signal
- Nếu chỉ 1/3 → có thể niche-specific hoặc anomaly

### Tip 3: Save raw data
fb-insight-miner output JSON sẽ rất rich. Save backup:
- `~/.claude/skills/1-research/fb-insight-miner/output/[fanpage-slug]-[date]/`
- Re-run analysis sau với context khác (vd: pre-launch vs post-launch comparison)

### Tip 4: Use insights in MULTIPLE skills
Updated niche-pack feeds vào:
- `content-engine` (Stage 1 profile build)
- `kallaway-hook-master` (hook with real verbatim)
- `email-marketing-writer` (subject lines with VoC)
- `lead-magnet-factory` (PDF topics matching pain)
- `digital-product-builder` (product topic validation)

→ 1 research session → improve 5+ skills output quality.

### Tip 5: Combine với community feedback
fb-insight-miner = competitor research.
Add: survey OWN audience (Google Form, IG poll) → triangulate.
Best insights come from 3 sources cross-validated.

---

## 🚫 Anti-patterns

### 1. Run fb-insight-miner on competitor để copy strategy
❌ "Em copy chiến thuật chị Hà 100%"
✅ Use insights to UNDERSTAND audience, build OWN strategy

### 2. Ignore verbatim, paraphrase everything
❌ Update niche-pack với chữ generic
✅ Keep verbatim ORIGINAL (kể cả typo) — đây là magic ingredient

### 3. Run cho 10 fanpages trong 1 tuần
❌ Overload data, không digest
✅ 1 fanpage / quarter, deep analysis

### 4. Skip review report, jump straight to hook
❌ Generate hook không update niche-pack first
✅ Niche-pack update FIRST, hook generate AFTER (with fresh data)

### 5. Run cho personal profile (not page)
❌ Apify can't scrape personal profiles
✅ Verify URL is PUBLIC PAGE before run

---

## 🆘 Troubleshooting

### Issue 1: Apify MCP not connected
**Fix**: 
- Check `~/.claude/settings.json` Apify config correct
- Re-authenticate Apify token
- Test: `mcp__apify__*` tools available?

### Issue 2: Adult/sensitive niche → comments return zero
**Symptom**: 20 posts scrape OK but only 2/2000 comments returned
**Cause**: FB age-gate filtering
**Fix**: Pivot to IG/TikTok where filtering differs

### Issue 3: Apify cost spike unexpectedly
**Fix**: 
- Check fb-insight-miner skill SKILL.md cost transparency section
- Set hard cap: depth=light ($2) instead of standard ($4)
- Cap top 20 posts only (skill default)

### Issue 4: Insight report too generic
**Cause**: Fanpage chosen audience too broad
**Fix**: Pick more specific niche fanpage. Vd: "Phụ nữ kinh doanh" → "Coach parenting toddler" specific.

---

## ⏭ After Workflow D

1. **Workflow A**: Use fresh insights to validate NEW product idea
2. **Workflow B**: Generate 10-20 reels với hook based on real verbatim
3. **Workflow C**: Audit existing reels — many may need update with fresh insights
4. **Repeat Workflow D** quarterly for continuous insight refresh

---

## 📚 Reference

- Skill detail: `skills/1-research/fb-insight-miner/SKILL.md`
- 9 Insight dimensions: `skills/1-research/fb-insight-miner/references/9-insight-dimensions.md`
- Sampling rules: `skills/1-research/fb-insight-miner/references/sampling-rules.md`
- Silent signals guide: `skills/1-research/fb-insight-miner/references/silent-signals-guide.md`
