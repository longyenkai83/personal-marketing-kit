---
name: email-marketing-writer
description: Viết email marketing theo phương pháp Maria Wendt ($18M revenue, 30% open rate gấp đôi industry) — campaigns/launches/automations, 9-Word Email, subject line random-curiosity-driven, email-algorithm hacks (look-like-personal, reply-back). Use when user wants to write email sequence, welcome series, broadcast email, launch email, nurture email, pitch email, hoặc audit subject line. Vietnamese-first. Triggers — "viết email", "welcome sequence", "email marketing", "subject line", "email automation", "nurture email", "9 word email".
allowed-tools: Read, Grep, Glob
argument-hint: "[email type] [topic] [persona]"
---

# Email Marketing Writer — Maria Wendt Method

Phương pháp viết email marketing đã proven $18M doanh thu của Maria Wendt — adapt cho thị trường VN.

## When to invoke

VN trigger phrases:
- "viết welcome email sequence"
- "viết email broadcast / launch"
- "subject line cho email"
- "9 word email re-engage list cũ"
- "email nurture vs pitch"
- "email automation"
- "audit email cũ"

User can also invoke `/email-marketing-writer` directly.

**Do NOT use for:**
- Caption FB/IG (dùng `content-engine` hoặc `kallaway-hook-master`)
- Sales page copy (dùng `digital-product-builder` khi có)
- Cold outreach DM (cá nhân hơn — dùng tay)

## Required inputs (ask if missing)

1. **Email type** — chọn 1:
   - `campaign` (1 email cho toàn list, fixed time)
   - `launch` (multi-email cash spike sequence)
   - `welcome_automation` (5-email trigger sau opt-in)
   - `9_word_reengage` (Dean Jackson style cho list cũ)
   - `nurture` (build trust, story, vulnerability)
   - `pitch` (sales-focused)
   - `broadcast_random` (subject random + curiosity)
2. **Topic / hook** — chủ đề email
3. **Persona target** — đối tượng (default load từ niche-pack)
4. **CTA** — link click target (sales page, freebie, reply prompt)
5. **Brand voice notes** (optional) — tone, signature phrase
6. **Số email cần** — default 1 (sequence: 5 cho welcome, 5-7 cho launch)

## Triết lý cốt lõi (KHÔNG QUÊN)

> **Email marketing's job = MAKE MONEY.**
> 
> Không phải viết tiểu thuyết Mỹ vĩ đại. Không phải làm thơ.
> 
> Mọi email phải dẫn tới: **EMAIL OPENED → LINK CLICKED → SALE MADE**.

3-step funnel:
```
Subject line → Email open → CTA link click → Checkout → Sale
```

Lệch bất kỳ bước nào = không kiếm tiền. Skill này focus vào **maximize từng bước**.

## 3 loại email (Maria's classification)

| Loại | Tần suất | Mục đích | Note |
|------|----------|----------|------|
| **Campaigns** | Hằng ngày toàn list | Phần lớn revenue (Maria 90%) | Fixed time, miss → miss |
| **Launches** | 1/tháng | Cash spike $$$ | Có waitlist + VIP sequence (xem Cash Spike playbook) |
| **Automations** | Trigger-based | Welcome / Abandoned cart / 7-day course | Welcome Coupon kiếm **$50k/tháng** cho Maria |

## Frequency strategy (gây sốc nhưng PROVEN)

**Maria gửi 1-2 email/ngày**:
- Mon: 1 email
- Tue: 2 email (sáng + chiều)
- Wed: 1 email
- Thu: 2 email
- ...

**Insight từ founder $300M biz** (Maria học được):
> *"Họ unsubscribe và tức giận với rate tương tự — nên gửi nhiều hơn = kiếm nhiều hơn."*

**Workflow gradual scale**:
1. Tuần 1-2: 3-5 email/tuần (warm up)
2. Tháng 2: 1 email/ngày
3. Tháng 3+: Có thể 1-2/ngày

→ **Anti-pattern**: Sợ unsubscribe → gửi 1 email/tuần → revenue thấp + algo penalize.

## EMAIL ALGORITHM HACKS (CRITICAL — read `references/email-algorithm-hacks.md`)

> **Email phải LOOK LIKE FROM A REAL PERSON sending to ONE person.**
> 
> Không phải marketing template từ company.

### Visual rules
- ✅ Left-aligned text (như cách bạn gửi email cho bạn bè)
- ✅ Personal tone, "you/em/chị" thay "anh chị em ơi"
- ✅ 1 image OK (phải feel personal, không stock)
- ❌ KHÔNG header company logo to
- ❌ KHÔNG footer social media buttons
- ❌ KHÔNG nhiều graphic blocks
- ❌ KHÔNG layout columns

### Reply-back tactic (CỰC mạnh)
Insert "Reply back and let me know" mỗi 3-4 email:
- Trick algo nghĩ "2 người đang chat" → boost deliverability
- Boost open rate cho email tiếp theo
- Build relationship thật

### Tool stack
- **Active Campaign** (Maria's choice) — tốt cho deliverability + automation
- Tránh: tool quá generic (Mailchimp basic) → email bị xếp Promotions tab

## SUBJECT LINE — 5 Rules (đọc `references/subject-line-bank-and-rules.md`)

> **50% TIME** dành cho subject line. Quan trọng hơn nội dung.

### 5 Rules
1. **Audience cực chán** → email là "ngụm nước lạnh trong sa mạc"
2. **CÀNG RANDOM CÀNG TỐT** — càng ÍT liên quan business càng tốt
3. **Phải tạo curiosity gap** — "cái quái gì là [X]?"
4. **Specificity over generic** — số liệu, tên cụ thể
5. **Subject line viết TRƯỚC nội dung** (không phải sau)

### Maria's top examples (gold mine)
- "Bank account overdraft Maria"
- "Sketchy massage flyer"
- "Student stole my entire business model"
- "$10M thermometer"
- "Plumber and millionaire"
- "$54k credit card bill weekly"
- "Manipulating time"
- "Scary woman"
- "Porch Pirate"
- "Tupperware theory"
- "Potato and rock star"
- "We said I love you" (mysterious)

→ **Pattern**: Random nouns + curiosity hook + KHÔNG sound like marketing

### Preview Text = VP supporting Subject Line (President)
- Hỗ trợ subject line + tạo intrigue thêm
- HOẶC mâu thuẫn subject line → resolution need
- Vd: Subject "Plumber and millionaire" + Preview: "Why the plumber wins every time"

## 9-WORD EMAIL — Dean Jackson Method

> **Re-activate cold list bằng 9 từ. Mind không thể chống lại bí ẩn chưa giải.**

### Template
> *"[Tên], [bạn vẫn còn] [outcome cụ thể]?"*

### Examples
- EN: "Are you still looking for a home in Georgia?"
- EN: "Are you still planning a trip to Israel?"
- VN: "Chị Hương, chị vẫn còn muốn có 10 khách online đầu tiên không?"
- VN: "Em Lan, em vẫn còn muốn đóng gói khoá học của em không?"

### Rules
- GIỮ NGẮN — chống cám dỗ thêm chi tiết
- Specific outcome (không "muốn thành công" mà "10 khách online đầu tiên")
- Personal — dùng [first_name] merge field
- Question mark cuối → invite reply

### Khi dùng
- List cũ ≥ 90 ngày không gửi
- Re-engage subscriber lurker
- Test xem ai còn warm
- Pre-launch warmup (1 tuần trước launch)

## NURTURE vs PITCH balance

> **Most emails = NURTURE. Few = PITCH. Even pitches feel valuable.**

### Tỷ lệ Maria
- 70-80% nurture (build trust, story, vulnerability, education)
- 20-30% pitch (direct sale, mostly trong launch sequence)
- Mỗi pitch vẫn có 1 piece of value upfront

### Nurture email patterns
- Personal story (Maria cực vulnerable trong email — hơn IG/YouTube)
- Behind-the-scene
- Lesson learned (failure + recovery)
- Quick tip (1 actionable insight)
- Subtly mention product (không hard sell)

### Pitch email — Maria's method
- Mở bằng STORY/INSIGHT (5-7 câu nurture)
- Bridge sang offer ("Đó là lý do tôi build [product]")
- Concrete benefit (not features)
- Soft CTA (link 1 lần, không pressure)
- Optional: limited offer/deadline

### Anti-pattern
❌ Emotional whiplash: nurture-nurture-nurture-PITCH ĐẤM
✅ Pitch như tiếp nối nurture, value first

## Methodology — 5-step Email Writing Workflow

### Step 1: Define inputs
Dùng 6 câu hỏi ở trên.

### Step 2: Write SUBJECT LINE first (50% time)
- Brainstorm 10 random subject lines
- Test curiosity: "Audience phải biết [X] là cái quái gì?"
- Pick 3 strongest
- Score 1-10 cho random/curiosity/specificity
- Top 1 → use, top 2 → A/B test

### Step 3: Write PREVIEW TEXT (support/contradict subject)

### Step 4: Write EMAIL BODY
- Open với hook cá nhân (không "Xin chào anh/chị em")
- Story/value 70-80% length
- 1 CTA chính (link → checkout/freebie/landing)
- Optional: "Reply back and let me know" trigger

### Step 5: Self-check before send
- [ ] Subject line random + curiosity?
- [ ] Preview text support?
- [ ] Email LOOKS personal (left-aligned, no fancy header)?
- [ ] 1 CTA rõ?
- [ ] Reply-back prompt? (nếu chưa có gần đây)
- [ ] Tone match brand?
- [ ] No fake stat / no fake testimonial?

## Output Format

```markdown
## Email — [Type] · [Topic]

**Type**: [campaign/launch/welcome_automation/9_word/nurture/pitch]
**Persona**: [tên]
**CTA target**: [link]
**Send time**: [recommended slot]

---

### Subject Line (Top 3)
1. **A**: "[subject]" — Score: random [X]/10 · curiosity [Y]/10
2. **B**: "[subject]" — Score: ...
3. **C**: "[subject]" — Score: ...

→ **Pick**: A | A/B test A vs B

### Preview Text
"[≤90 chars supporting/contradicting subject]"

---

### Email Body

[Hook personal — opening line]

[Body — story/value, 150-300 từ]

[Bridge to CTA]

[CTA — 1 link, soft]

[Optional: reply-back prompt]

[Sign-off — personal, signature phrase nếu có]

---

### Self-Check
- ✅ Subject random + curiosity
- ✅ Looks personal (no template feel)
- ✅ 1 CTA clear
- ✅ Tone match brand
- [stat/testimonial verified or marked placeholder]
```

## Integration

- **Chained from**: `digital-product-builder` (gen launch email sequence cho new product)
- **Chained to**: `tripwire-builder` (thêm welcome coupon flow vào funnel)
- **Reference shared**: `kallaway-script-master/references/cta-library.md` (đa dạng CTA, không lúc nào cũng "comment X")

## Reference Files

- `references/email-algorithm-hacks.md` — Look-like-personal + reply-back + Active Campaign
- `references/subject-line-bank-and-rules.md` — 5 rules + 30 Maria examples + VN adaptation
- `references/9-word-email-method.md` — Dean Jackson template + VN examples
- `templates/welcome-5-email-sequence.md` — 5-email welcome automation ready-to-customize

## Failure modes

- **Open rate <15%** → Subject line generic. Re-do với random/curiosity test.
- **Click rate <2%** → CTA too vague hoặc value upfront thiếu. Strengthen body.
- **Unsubscribe spike** → Pitch quá nhiều, không nurture. Reframe: thường unsub không phải loss.
- **Email vào Promotions tab** → Layout quá template-y. Strip header/footer/buttons.
- **No replies** → Thêm "Reply back and let me know" vào 3-4 email.

## Status

**v1.0** — built từ Maria Wendt "Inbox to Income" course (Module 5 Foundations + Module 6 Writing + Module 8 Automations). Tools: Active Campaign primary.
