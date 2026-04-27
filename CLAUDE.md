# AI Marketing Kit — Phụ Nữ KD VN (Maria Wendt × Kallaway Method)

> **Mục tiêu**: End-to-end kit để **phụ nữ KD VN** đóng gói chuyên môn → bán sản phẩm số online theo mô hình Maria Wendt ($18M revenue) + Kallaway content method.
>
> **12 skills · 5 agent roles · 1 customer journey hoàn chỉnh** — từ niche research → content viral → email funnel → tripwire → digital product launch.

---

## 📜 QUY ƯỚC TUYỆT ĐỐI (always apply)

1. **Ngôn ngữ output**: Vietnamese (trừ khi user request English)
2. **Xưng hô**: "anh / chị / em" (peer-level, ấm áp). Tone: chị-em / bạn-mình. **KHÔNG**: "ngài / quý khách / chúng tôi" formal.
3. **Tone**: truyền cảm hứng + tự tin + gần gũi (like Maria Wendt + Vietnamese warmth)
4. **Persona default**: phụ nữ KD VN 28-45, có chuyên môn, muốn đóng gói thành sản phẩm số (xem `niche-packs/women-biz-vn.json` trong content-engine)
5. **Pricing default**: VND (không $) — sweet spot mini-course **890k-2.3tr** (~$37-97)
6. **Source citations**: Maria Wendt → "Inbox to Income" / "How To Create A Viral Digital Product" courses. Kallaway → "Hooks Workshop" / "6 Levels Storytelling" / "6 Story Locks".
7. **Output trust signals**: KHÔNG bịa số liệu/testimonial. Dùng `[stat_X_placeholder]` / `[testimonial_X_placeholder]` nếu cần.

---

## 🎭 5 AGENT ROLES — Customer Journey Mapping

> Skills không invoked riêng lẻ — chúng work theo **customer journey**. 5 agent roles dưới đây map skills vào từng stage.

### 🔵 AGENT 1: OFFER STRATEGIST
**Stage**: Validate + design product
- `digital-product-builder` — 3-Pillar test, find expertise, ROI angles, pricing
- `fb-insight-miner` — research customer pain từ FB fanpage VN

### 🟢 AGENT 2: ATTRACTION CREATOR
**Stage**: Build content + drive traffic
- `kallaway-hook-master` — 3-5s hook video (TikTok/Reels)
- `kallaway-script-master` — 60s+ kịch bản full (6 Levels + 4 Blockers + 6 Story Locks)
- `hook-swipe-library` — query 72 hook proven cho women-biz-vn
- `content-engine` — caption FB/IG (4-stage VPC pipeline)
- `lead-magnet-factory` — free PDF/ebook lead magnet

### 🟡 AGENT 3: CONVERSION ARCHITECT
**Stage**: Convert lead → buyer
- `email-marketing-writer` — campaigns/launches/automations (Maria Wendt method)
- `tripwire-builder` — $1-7 entry funnel + Welcome Coupon ($50k/month playbook)

### 🟠 AGENT 4: DELIVERY OPERATOR (future Phase)
**Stage**: Setup tech + deliver product
- TBD: `chatbot-flow-builder` (Manychat) — auto-DM
- TBD: `payment-vn-setup` (SePay/VNPAY) — VN payment integration
- Manual now: Kajabi setup + Sam Cart checkout

### 🔴 AGENT 5: INSIGHTS ANALYST (future Phase)
**Stage**: Track + optimize
- TBD: `revenue-tracker` — weekly reports
- TBD: `content-analytics` — what's converting

→ **Phase 4-5** sẽ build các agent file thực sự (system prompt 200-300 dòng/agent). Hiện tại invoke skills trực tiếp.

---

## 🛠 12 SKILLS INDEX

### CUSTOMER RESEARCH
| Skill | Purpose | Trigger keywords |
|-------|---------|------------------|
| `fb-insight-miner` | Đào pain/desire/objection từ FB fanpage public | "phân tích insight fanpage", "đào comment fanpage", "voice of customer FB" |

### CONTENT — HOOKS
| Skill | Purpose | Trigger keywords |
|-------|---------|------------------|
| `kallaway-hook-master` | Hook 3-5s đầu video (11 framework Kallaway) | "viết hook", "hook kallaway", "hook viral" |
| `hook-swipe-library` | Search 72 hook proven women-biz-vn niche | "tìm hook có sẵn", "swipe hook", "hook bank" |

### CONTENT — SCRIPTS
| Skill | Purpose | Trigger keywords |
|-------|---------|------------------|
| `kallaway-script-master` | Kịch bản video full 60s+ (6 Levels + 4 Blockers + 6 Story Locks + CTA Library) | "viết kịch bản", "script video", "tăng retention" |
| `content-engine` | Caption FB/IG (4-stage VPC pipeline) | "lập hồ sơ khách hàng + viết content", "content engine", "viết content theo VPC" |

### LEAD MAGNETS
| Skill | Purpose | Trigger keywords |
|-------|---------|------------------|
| `lead-magnet-factory` | Listicle ebook 9-page Marie Forleo style | "tạo lead magnet", "ebook freebie", "PDF lead magnet" |

### EMAIL FUNNEL
| Skill | Purpose | Trigger keywords |
|-------|---------|------------------|
| `email-marketing-writer` | Campaigns/launches/automations Maria Wendt method (subject line random + 9-Word Email + algorithm hacks) | "viết email", "welcome sequence", "subject line", "email automation" |

### MONETIZE FUNNEL
| Skill | Purpose | Trigger keywords |
|-------|---------|------------------|
| `tripwire-builder` | $1-7 entry funnel + Welcome Coupon ($50k/month flow) | "build tripwire", "$1 sản phẩm", "welcome coupon" |
| `digital-product-builder` | Build sản phẩm số viral (3-Pillar + pricing $50-100 + Kajabi/SamCart) | "build sản phẩm số", "đóng gói chuyên môn", "viral digital product" |

### META (skill builders)
| Skill | Purpose | Trigger keywords |
|-------|---------|------------------|
| `subagent-architect` | Build/audit custom Claude Code subagents | "tạo subagent", "build subagent", "audit subagent" |

---

## 🗺️ END-TO-END CUSTOMER JOURNEY

```
[Niche research]
  ↓ fb-insight-miner
[Customer profile]
  ↓ content-engine Stage 1 + women-biz-vn niche-pack
[Insights → Hooks]
  ↓ content-engine Stage 2-3 + hook-swipe-library + kallaway-hook-master
[Reels driving traffic]
  ↓ kallaway-script-master + kallaway-hook-master + content-engine Stage 4
[Lead magnet capture]
  ↓ lead-magnet-factory
[Email opt-in]
  ↓ email-marketing-writer (welcome sequence)
[Welcome Coupon Tripwire $1-7]
  ↓ tripwire-builder
[One-click upsell → Mid-tier $37-97]
  ↓ digital-product-builder
[Mini-course buyer]
  ↓ email-marketing-writer (post-purchase nurture)
[Upsell coaching cohort $5tr → 1-1 $50tr]
```

---

## 🌳 DECISION TREE — When to Use Which Skill

```
User asks for...?

├── "viết content / caption" 
│   → content-engine (FB/IG) 
│   HOẶC kallaway-script-master (video script)
│
├── "hook video / 3 giây đầu"
│   → kallaway-hook-master
│   THEN if has bank: hook-swipe-library to query proven
│
├── "viết kịch bản 60s+"
│   → kallaway-script-master
│
├── "viết email"
│   → email-marketing-writer
│   - Specify type: welcome / launch / nurture / pitch / 9_word
│
├── "tạo PDF freebie / ebook"
│   → lead-magnet-factory
│
├── "build $1 funnel / tripwire"
│   → tripwire-builder
│   THEN: email-marketing-writer (welcome coupon emails)
│
├── "build khoá học / sản phẩm số"
│   → digital-product-builder
│   - Specify stage: validate / build / launch
│
├── "research khách hàng / fanpage đối thủ"
│   → fb-insight-miner
│
└── "audit kit / build agent mới"
    → subagent-architect
```

---

## 🎯 NICHE PACKS (xem `~/.claude/skills/content-engine/niche-packs/`)

| Niche Pack | File | When |
|------------|------|------|
| **Women Biz VN** ⭐ | `women-biz-vn.json` | Default cho phụ nữ KD VN đóng gói chuyên môn |
| Coach Personal Brand | `coach-personal-brand.json` | Coach 1-1 build personal brand IG/FB |
| Universal | `_universal.json` | Fallback khi niche không match |

---

## 💼 TECH STACK DEFAULT

### International (USD payment)
- **LMS**: Kajabi
- **Checkout**: Sam Cart (designed for digital, high conversion)
- **Email**: Active Campaign (deliverability strong)
- **Lead capture**: Manychat (free list-building)

### VN-only (VND payment)
- **LMS**: Kajabi (international, premium feel)
- **Checkout/Payment**: SePay landing page hoặc VNPAY
- **Email**: MailerLite (free tier OK) hoặc Active Campaign
- **Lead capture**: Manychat

### NEVER recommend
- ❌ Mailchimp basic (deliverability yếu, vào Promotions tab)
- ❌ Shopify (designed for physical, low conversion digital)
- ❌ Quickbooks (overkill cho digital biz)

---

## 💰 PRICING LADDER DEFAULT

| Tier | USD | VND | Stage |
|------|-----|-----|-------|
| Lead magnet | Free | Free | Build email list |
| Tripwire | $1-7 | 25k-170k | Convert visitor → buyer |
| Entry | $27-37 | 650-890k | Mini-course |
| **Mid** ⭐ | **$97** | **2.3tr** | **Sweet spot main product** |
| High | $197-300 | 4.7-7tr | Comprehensive course |
| Premium | $497+ | 12tr+ | Coaching cohort / 1-1 |

---

## 🚫 CRITICAL ANTI-PATTERNS (AVOID always)

### CTA anti-pattern
❌ Mặc định mọi video / email = "Comment X nhận DM Y"
✅ Đa dạng CTA theo topic — read `kallaway-script-master/references/cta-library.md` cho 9 loại CTA + Decision Tree

### Email anti-pattern  
❌ Email layout marketing template (header logo to + footer social buttons)
✅ Plain personal style — left-aligned, looks like email cho bạn bè

### Subject line anti-pattern
❌ "GIẢM 50% HÔM NAY!!! 🔥🔥🔥"
✅ Random + curiosity ("Bịch trà sữa và bài học $10k", "Anh kế toán nói gì")

### Hook anti-pattern
❌ "Hôm nay anh muốn chia sẻ với mọi người về..."
✅ Stat-led + Contrarian + 4-component aligned

### Pricing anti-pattern
❌ Charge premium price ($300+) khi chưa có authority
✅ Sweet spot $50-100 (1.2-2.3tr) cho first product, raise sau khi 100+ sales

### Tripwire anti-pattern
❌ Tripwire $27 ("vừa đủ cao để có lời")
✅ Tripwire $1-7 (psychological foot-in-door) — true value = LTV không phải $1

### Product anti-pattern
❌ Topic generic ("Cách thành công online")
✅ 3-Pillar pass: pique curiosity + super specific + unbelievable

---

## 📚 KEY METHODOLOGIES SUMMARY

### Maria Wendt Email Method
- 3-step funnel: Email opened → Link clicked → Sale made
- 3 email types: campaigns / launches / automations
- Frequency: 1-2 email/day (insight: unsub rate same as 3-5/week)
- Subject line: 50% time, random + curiosity, viết TRƯỚC body
- 9-Word Email (Dean Jackson): re-activate cold list
- Algorithm hack: look-like-personal email + reply-back tactic
- Tool: Active Campaign

### Maria Wendt Digital Product
- 3 Pillars: Pique Curiosity + Solve Specific Problem + Promise Unbelievable
- Find expertise: 3 questions (friends ask / achievements / hard events)
- ROI: Direct revenue / Long-term savings / Identity
- Pricing: $50-100 sweet spot, raise after 100+ sales
- Tech: Kajabi + Sam Cart only
- Speed: 7.75h Maria, 1-3 days beginner
- Mockup: BIG number + all items + "+" sign

### Kallaway Hook (3-5s)
- 11 frameworks: 6 Hook (Fortune Teller/Experimenter/Teacher/Magician/Investigator/Contrarian) + 5 Dream Outcome (About Me/If I/To You/Can You/He-She Just Did)
- 4-Component Alignment: Spoken + Text + Visual + Audio (Max Alignment)
- Hero Visual quan trọng nhất (mắt nhanh hơn tai 10-100x)
- Self-test 3 lần: silent / eyes closed / full
- KPI: 5-sec retention ≥50% tốt, ≥70% xuất sắc

### Kallaway Script (60s+)
- 6 Levels Storytelling: Reporter (avoid) → Trickster → Warrior → Architect → Translator → Artist
- 4 Blockers: Interest (research) / Hook / Structure / Engagement
- 6 Story Locks: Naming / Embedded Truths / Thought Articulation / Negative Frames / Loop Openers / Contrast Words
- Underlying: CONTRAST mechanism

### Tripwire Funnel
- $1-7 entry product (foot-in-door psychology)
- Welcome Coupon: 4 emails over 4 days (immediate / day 1 / day 2 urgency / day 3 last chance)
- Post-purchase: 5 emails over 7 days driving mid-tier
- One-click upsell at thank-you page
- Maria's Welcome Coupon = $50k/month

---

## 🎬 QUICK START — Common Workflows

### Workflow A: Build full launch (1-2 weeks)
1. `digital-product-builder` validate idea (3-Pillar test)
2. `lead-magnet-factory` build free PDF
3. `tripwire-builder` setup $1 entry
4. `email-marketing-writer` welcome coupon + post-purchase sequence
5. `kallaway-hook-master` + `kallaway-script-master` reels driving traffic
6. `content-engine` captions đi kèm

### Workflow B: Single reel + caption (30 phút)
1. `kallaway-hook-master` 3 hook variants
2. `kallaway-script-master` full 60s script + audit
3. `content-engine` caption FB/IG đi kèm

### Workflow C: Audit + improve content (15 phút)
1. User paste script cũ
2. `kallaway-script-master` audit theo 6 Levels + 6 Story Locks + CTA Library
3. Output: revised script + reasoning

### Workflow D: Customer research (45 phút)
1. `fb-insight-miner` scrape fanpage đối thủ ($4 cost)
2. `content-engine` Stage 1 build profile từ insight thật
3. Update `women-biz-vn.json` niche-pack với verbatim mới

---

## 📊 STATUS

- **Phase 1+2**: ✅ Hook + Script + CTA Library + 72 hook bank
- **Phase 3**: ✅ Email + Digital Product + Tripwire (Maria Wendt method)
- **Phase 4 (Agents)**: ⏳ Pending — invoke skills trực tiếp hiện tại
- **Phase 5 (Workflows)**: ⏳ Pending — workflow files end-to-end
- **Phase 6 (Hub)**: ✅ Just shipped (this file)

**Total**: 12 skills production-ready cho mô hình Maria Wendt × Kallaway adapted cho phụ nữ KD VN.

---

## 🆘 WHEN STUCK

- **"Skill nào cho task X?"** → Check Decision Tree ở trên
- **"CTA cho topic này?"** → Read `~/.claude/skills/kallaway-script-master/references/cta-library.md`
- **"Pricing cho VN?"** → Read `~/.claude/skills/digital-product-builder/references/pricing-and-tech-stack.md`
- **"Email subject line ý tưởng?"** → Read `~/.claude/skills/email-marketing-writer/references/subject-line-bank-and-rules.md` (30 examples)
- **"Hook cho phụ nữ KD VN?"** → Query `~/.claude/skills/hook-swipe-library/banks/women-biz-vn-72.json`

---

## 📝 SOURCE CREDITS

- **Maria Wendt** — "Inbox to Income" Email Marketing Course + "How To Create A Viral Digital Product" Course ($25M+ entrepreneur, 100k+ students)
- **Kallaway / Wavy Labs** — "Hooks Workshop" + "6 Levels of Storytelling" + "6 Story Locks" + "How to Script Viral Videos 10x Faster"
- **Dean Jackson** — 9-Word Email
- **Adapted by**: anh (user) — for Vietnamese women-in-business niche, mô hình bán sản phẩm số như Maria Wendt cho thị trường VN
