# Tripwire Funnel Blueprint — End-to-End

> **Build trong 2 tuần**: Idea → Live tripwire funnel making first sales.

---

## 📋 BLUEPRINT INPUTS

| Field | Value |
|-------|-------|
| Niche / persona | (super specific) |
| Mid-tier product (upsell target) | [name + price] |
| Tripwire type chosen | worksheet / mini-course / 7-day email / audio |
| Tripwire price | $1 / $7 / $17 / $27 |
| Lead magnet (driving traffic) | [name + format] |
| Tech stack | Sam Cart + Active Campaign / Bootstrap |
| Timeline | 2 weeks / 4 weeks |

---

## 🎯 STEP 1 — VALIDATE TRIPWIRE IDEA

### Sub-version of mid-tier check
Tripwire phải là MICRO-VERSION of mid-tier's problem.

**Mid-tier**: ___________
**Tripwire**: ___________

→ Logical bridge? [Yes / No]

### Quick-win test
Tripwire deliver outcome trong < 30 phút?
[Yes / No]

### Specific outcome
Tripwire promise: "[outcome] trong [timeframe]"
___________

---

## 🎨 STEP 2 — BUILD TRIPWIRE CONTENT

### For Worksheet/Template ($1)
- [ ] List items (target 12-30)
- [ ] Canva templates (branded)
- [ ] PDF export + editable Canva link
- [ ] Cover page polished
- [ ] Test với 3 friends

### For Mini-course ($7-27)
- [ ] Outline 3-5 lessons (5-10 min each)
- [ ] Record videos (phone OK)
- [ ] Edit basic
- [ ] Upload to Kajabi
- [ ] Workbook PDF supplement (bonus)

### For 7-Day Email Course
- [ ] Outline 7 lessons
- [ ] Write all 7 emails in Active Campaign
- [ ] Each email: 200-400 words + 1 actionable
- [ ] Day 7 = soft pitch mid-tier

### For Audio
- [ ] Outline 5-10 audio files
- [ ] Record với phone voice memo
- [ ] Edit basic (trim silence)
- [ ] PDF transcripts as bonus

---

## 🛒 STEP 3 — SAM CART CHECKOUT PAGE

### Page elements (top to bottom)

```
┌──────────────────────────────────────┐
│ HERO SECTION                         │
│ - Big tripwire name                  │
│ - Tagline (3-pillar style)           │
│ - Mockup video (15-30s autoplay)     │
│                                      │
├──────────────────────────────────────┤
│ MOCKUP IMAGE (Maria-style)           │
│ - Big number ("12 Worksheets")       │
│ - All items shown                    │
│ - "+" hint of bonuses                │
│                                      │
├──────────────────────────────────────┤
│ PRICE                                │
│ ~~$27~~ → $1 today (anchored)        │
│                                      │
├──────────────────────────────────────┤
│ VALUE BULLETS (4-6)                  │
│ ✓ Quick win 1 (specific)             │
│ ✓ Quick win 2                        │
│ ✓ Bonus 1                            │
│ ✓ Bonus 2                            │
│                                      │
├──────────────────────────────────────┤
│ USE PROOF popup (bottom-left)        │
│ "Sarah from Hanoi just purchased"    │
│                                      │
├──────────────────────────────────────┤
│ CHECKOUT FORM                        │
│ - Email                              │
│ - Name                               │
│ - Card                               │
│ - Billing address (REQUIRED!)        │
│                                      │
├──────────────────────────────────────┤
│ "GET ACCESS NOW $1" button (red)     │
│                                      │
├──────────────────────────────────────┤
│ ORDER BUMP option                    │
│ ☐ "Add [Bonus Template] for $7 more" │
│                                      │
├──────────────────────────────────────┤
│ Trust signals: refund policy + secure│
└──────────────────────────────────────┘
```

### One-Click Upsell setup
- [ ] After purchase confirm → show next page
- [ ] Offer mid-tier with discount: "Add Mid-tier $97 → $77 today only"
- [ ] One-click button (already have payment info)
- [ ] Decline option visible (don't trap)

---

## 📧 STEP 4 — EMAIL AUTOMATIONS (Active Campaign)

### Automation A: Welcome Coupon (4 emails over 4 days)

**Trigger**: User opted in to lead magnet

**Sequence**:

| Day | Email | Purpose |
|-----|-------|---------|
| 0 (immediate) | Email 1 | Deliver freebie + intro tripwire ($1 with 48h coupon) |
| 1 | Email 2 | Story + soft re-mention coupon |
| 2 | Email 3 | Urgency: "24h cuối" |
| 3 | Email 4 | Last chance: "Tối nay" |

**Conditional logic**: If purchased anytime → exit Automation A → enter Automation B

### Automation B: Post-Purchase Upsell (5 emails over 7 days)

**Trigger**: User purchased tripwire

**Sequence**:

| Day | Email | Purpose |
|-----|-------|---------|
| 0 (immediate) | Email A | Welcome buyer + delivery + tease bonus |
| 1 | Email B | Encouragement to USE tripwire + quick tip |
| 3 | Email C | Story + bridge to mid-tier ("after [tripwire] many ask...") |
| 5 | Email D | Soft pitch mid-tier (with buyer-only discount) |
| 7 | Email E | Hard pitch + bonus stack ("expires tonight") |

→ See `welcome-coupon-automation.md` for full email templates.

---

## 🚀 STEP 5 — LEAD MAGNET DRIVING TRAFFIC

Tripwire không tự động có traffic. Cần lead magnet upstream.

### Choose lead magnet type

| Option | Best when |
|--------|-----------|
| **Free PDF guide** | Universal, broad appeal |
| **Free quiz** | Personality/diagnostic angle |
| **Free training** | Need to demonstrate teaching style |
| **Free Manychat freebie** | Building Manychat funnel free list-building |

### Lead magnet design
- Specific outcome (3-pillar test)
- Quick win < 15 min
- Branded design
- Easy opt-in (1 form field minimum)

### Connect to tripwire
- Opt-in landing page → user enters email → instant download + Welcome Coupon email triggered

→ See `lead-magnet-factory` skill for full lead magnet build.

---

## 📈 STEP 6 — SOFT LAUNCH (Test with existing list)

Before scaling traffic:
- [ ] Soft launch to 100-500 existing subscribers
- [ ] Measure conversion at each step
- [ ] Identify weakest link (low conversion %)
- [ ] Iterate before scaling ads

### Day 1-7 metrics to track

| Metric | Target | Day 7 actual |
|--------|--------|--------------|
| Lead magnet opt-in % | ≥50% | ___% |
| Opt-in → Tripwire purchase | ≥10% | ___% |
| Tripwire → One-click upsell | ≥25% | ___% |
| Tripwire → Mid-tier (7d) | ≥15% | ___% |
| Tripwire AOV (with upsell) | ≥$10 | $___ |
| Refund rate | <5% | ___% |

→ Pass = scale traffic. Fail = optimize step weakest first.

---

## 📊 STEP 7 — SCALE TRAFFIC

Once funnel proven:

### Option A: Free traffic (Manychat funnel)
- Reels/posts driving DM
- Manychat auto-DM "Comment '[KEYWORD]' to get [Lead Magnet]"
- DM → email capture → Welcome Coupon triggered
- Cost: $0 (Manychat free tier)

### Option B: Paid ads (Meta/TikTok)
- Ad → Lead magnet landing page
- Conversion campaign optimized
- Budget: start $20/day, scale to $100+/day if profitable
- Track CPM + cost per lead + cost per tripwire sale

### Option C: Hybrid
- Manychat for organic
- Paid ads for scaling
- Both funnel into same Welcome Coupon sequence

---

## 🔍 STEP 8 — ITERATE & OPTIMIZE

### Weekly review
- [ ] Lead opt-in % stable?
- [ ] Tripwire conversion %?
- [ ] Upsell take rate?
- [ ] Mid-tier conversion within 7d?

### A/B test ideas

| Test | Variant A | Variant B |
|------|-----------|-----------|
| Tripwire price | $1 | $7 |
| Coupon urgency | 48h | 72h |
| Email 1 subject | Random + curiosity | Direct benefit |
| One-click upsell price | $77 | $97 (no discount) |
| Mockup style | Big number | Bullet list |

→ Run each test 7-14 days, declare winner if >5% difference.

### 90-day review
- [ ] Total tripwire sales: ___
- [ ] Tripwire revenue: $___
- [ ] Mid-tier conversion from tripwire buyers: ___ sales × $97 = $___
- [ ] Total funnel revenue: $___
- [ ] Cost per acquisition (if paid ads): $___
- [ ] ROAS (Return on ad spend): ___x

---

## ✅ FINAL LAUNCH CHECKLIST

### Pre-launch
- [ ] Tripwire content finalized + tested
- [ ] Sam Cart checkout built (mockup, Use Proof, billing form, one-click upsell)
- [ ] Active Campaign 2 automations live (Welcome + Post-purchase)
- [ ] Lead magnet created + landing page live
- [ ] All 4 Welcome Coupon emails written + scheduled
- [ ] All 5 Post-purchase emails written + scheduled
- [ ] Test purchase flow end-to-end (yourself)
- [ ] Confirmation emails working
- [ ] Coupon expiry actually enforced
- [ ] Refund policy posted

### Soft launch (Week 1)
- [ ] Send to 100-500 existing list
- [ ] Track Day 1, 3, 7 metrics
- [ ] Identify weak link
- [ ] Iterate

### Scale (Week 2+)
- [ ] Manychat or ads driving lead magnet
- [ ] Daily metric tracking
- [ ] A/B testing pipeline
- [ ] 90-day review calendar reminder

---

## 🎁 EXAMPLE — Phụ nữ KD VN tripwire (women-biz-vn niche)

### Target
**Mid-tier**: "Email Marketing System for Women Biz" $97 (2.3tr)

### Tripwire idea
**"30 Email Subject Line Swipes for Vietnamese Women Biz" — $1**

### Lead magnet upstream
**"Free 5 Welcome Email Templates"** — opt-in driving to tripwire

### Welcome Coupon Email 1 (VN)
```
Subject: 5 Welcome Email Templates đây + 1 deal đặc biệt

Chào [first_name],

Đây là 5 Welcome Email Templates em hứa gửi:
👉 [DOWNLOAD]

Vì chị đã trust em đăng ký nhận email, em muốn tặng chị 
1 deal đặc biệt:

═══════════════════════════════
🎁 30 Email Subject Line Swipes
Chỉ 25k hôm nay (giá thường 690k)
═══════════════════════════════

✓ 30 subject line đã proven (Maria-style random + curiosity)
✓ Adapted cho thị trường VN (xưng "chị/em")
✓ Editable Notion/Canva
✓ Bonus: 5 preview text patterns

Coupon hết hạn sau 48h.

👉 [GET IT FOR 25K]

Reply lại nếu chị có question.

— Maria 🤍

P.S. Nếu chị chỉ muốn lấy 5 Welcome Templates miễn phí — 
totally ok. Coupon chỉ là bonus.
```

### Bridge to mid-tier
- Tripwire: 30 subject lines (1 component of email marketing)
- Mid-tier: Full email marketing system (subject + body + automation + funnel)
- Logical: subject lines = appetizer, full system = main course

---

## 📋 PASTE-AND-CUSTOMIZE SUMMARY

```
TRIPWIRE FUNNEL BLUEPRINT

Niche: ___________
Mid-tier upsell target: ___________ (price: ___tr)
Tripwire type: ___________
Tripwire price: ___ (___k VND)

Lead magnet: ___________ (free)
↓
Opt-in (Manychat or ads driving)
↓
Welcome Coupon Email 1 (immediate) — Tripwire offer
↓ (if NOT purchased)
Email 2 (day 1) → Email 3 (day 2 urgency) → Email 4 (day 3 last chance)
↓ (if PURCHASED)
Sam Cart One-Click Upsell to mid-tier
↓
Post-Purchase Sequence (5 emails / 7 days driving mid-tier)

Expected metrics:
- Lead → Tripwire: 15-20%
- Tripwire → Upsell click: 30-40%
- Tripwire → Mid-tier (7d): 15-25%
- AOV: $25-30 (~600k-720k VND per tripwire buyer)
```
