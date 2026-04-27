# Email Algorithm Hacks — Maria Wendt

> **Triết lý nền tảng**: Email phải LOOK LIKE PERSONAL email. KHÔNG phải marketing template từ company.
> 
> Algo (Gmail, Outlook, Apple Mail) ngày càng smart — chúng phân biệt được "personal" vs "marketing" và xếp marketing vào Promotions tab → reach giảm 80%.

## Tại sao quan trọng

Email funnel:
```
Subject open → Body read → CTA click → Sale
```

**Nếu email vào Promotions tab** → 80% audience không thấy → 0 open → không sale.

Maria từ chuyển Mailchimp → Active Campaign: deliverability TĂNG NGAY → revenue +30%.

---

## 🎨 RULE 1: VISUAL — Look Personal, Not Template

### ✅ DO

- **Left-aligned text** (như cách bạn gửi email cho bạn bè)
- **Plain text dominant** — paragraph + heading nhẹ
- **1 image OK** — nhưng phải feel personal (không stock)
- **Single column layout**
- **Personal sign-off**: "Maria 🤍" (chứ không "Best regards, The Team at Maria Wendt LLC")
- **Font default** (Arial, Helvetica) — không fancy

### ❌ DON'T

- Header company logo to với gradient background
- Footer dày với social media buttons (Facebook/Instagram/Twitter/LinkedIn)
- Multi-column layout
- Stock images photo người mẫu
- "Click here to unsubscribe" dày + privacy policy thừa
- Background colors / box borders

### Template comparison

❌ **Marketing template** (Macy's, Lululemon style):
```
[BIG LOGO HEADER WITH GRADIENT]
[HERO IMAGE BANNER]

WELCOME, VALUED CUSTOMER

[3-COLUMN PRODUCT GRID]

SHOP NOW [BIG BUTTON]

[FOOTER: 8 social icons + 12 links]
```
→ Algo nhận diện: "marketing template" → Promotions tab.

✅ **Personal style** (Maria):
```
Hey Sarah,

Hôm nay tôi muốn kể bạn nghe về một thứ điên rồ vừa xảy ra...

[2-3 đoạn story personal]

Đây là cái tôi học được: [insight]

Nếu bạn đang ở [tình huống tương tự], thử cái này:
[link soft]

Reply back và cho tôi biết bạn thấy sao nhé.

Maria 🤍
```
→ Algo nhận diện: "personal email" → Inbox tab.

---

## 💬 RULE 2: REPLY-BACK TACTIC (Cực Mạnh)

### Cơ chế

- Insert "**Reply back and let me know**" vào email
- Nếu 5-10% audience reply → algo nhận diện: "2 người chat" → boost deliverability
- **Boost open rate cho EMAIL TIẾP THEO** (không chỉ email có reply prompt)

### Implementation

**Mỗi 3-4 email**: thêm 1 reply prompt với câu hỏi cụ thể:

✅ Examples:
- "Reply back và cho tôi biết bạn đang ở stage nào trong [process X]?"
- "Trả lời lại với 1 trong 3 lựa chọn: A / B / C"
- "Reply 'YES' nếu bạn quan tâm — tôi sẽ gửi thêm chi tiết"
- "Câu hỏi nhanh: bạn đang struggle nhất với [pain Y] không? Reply yes/no"

❌ Anti-pattern:
- Reply prompt mỗi email → audience nhàm
- Câu hỏi quá generic ("share suy nghĩ với mình") → không actionable
- Reply prompt + KHÔNG reply lại audience → mất trust

### Bonus

Khi audience reply, REPLY LẠI (manual hoặc team):
- Build relationship thật
- Tăng "engagement signal" cho algo lần nữa
- Nhiều audience trả tiền 5-10x sau khi creator reply DM/email cá nhân

---

## 🛠 RULE 3: TOOL STACK MATTERS

### Maria's recommendation: **Active Campaign**

Lý do:
- Strong **deliverability** infrastructure
- Built-in automation builder (drag-drop, không code)
- Behavioral triggers (mở email X → gửi email Y)
- Email scoring (lead warm vs cold)
- Integration tốt với Sam Cart, Stripe, Manychat

### Alternatives (theo Maria)

| Tool | Pros | Cons | When |
|------|------|------|------|
| **Active Campaign** | Best deliverability, automation mạnh | Curve học hơi cao | ⭐ Recommended |
| **ConvertKit** | Creator-friendly UI | Deliverability OK, pricing scale cao | Nếu là creator solo |
| **Flodesk** | Đẹp UI, tone Maria-like | Limited automation | Brand visual heavy |
| **Mailchimp** (basic plan) | Free tier | **Deliverability YẾU**, vào Promotions | ❌ Avoid cho serious biz |
| **GetResponse** | Cheap | Less features | Budget-tight |

### VN tools tương đương

- **MailerLite** (acceptable, free tier OK)
- **Brevo** (formerly Sendinblue) — VN-friendly pricing
- **Email API**: Postmark, SendGrid (cho dev)

---

## 📊 RULE 4: LIST HYGIENE

### Unsubscribe = GOOD

> *"Email list của tôi unsub là cleansing. Người không quan tâm rời đi → list sạch hơn → open rate cao hơn → algo boost reach."*
> — Maria

### Numbers

- Industry avg open rate: 15-20%
- Maria: **30%** (gấp đôi)
- Lý do: list sạch + subject line strong + algo trick

### Workflow định kỳ

**Mỗi 90 ngày**:
1. Identify subscribers chưa mở email nào trong 90 ngày
2. Send re-engagement email (9-Word Email — xem `references/9-word-email-method.md`)
3. Nếu vẫn không mở sau 2 tuần → REMOVE
4. Result: list nhỏ hơn nhưng chất hơn

### Tâm lý

- KHÔNG personal khi unsub
- Algo signal: % người mở > 50% → email được prioritize
- Unsub = họ self-filter, bạn KHÔNG phải làm việc đó

---

## 🚫 ANTI-PATTERNS (Don't do)

### 1. Subject line CAPS LOCK + emoji rage
❌ "🔥🔥🔥 LAST CHANCE!!! BUY NOW BEFORE GONE 🔥🔥🔥"
→ Spam filter trigger. Promotions tab.

### 2. Big sale numbers in subject
❌ "50% OFF EVERYTHING TODAY ONLY"
→ Algo detect "promo" → Promotions tab.

### 3. "Click here" link spam
❌ Email có 10 link "click here / shop now / buy now"
→ Spam score tăng. Inbox khác.

### 4. Image-only email (no text)
❌ Toàn graphic, không có text
→ Algo không read content được → low priority.

### 5. Sender name = Brand name
❌ From: "Brand Name LLC"
✅ From: "Maria 🤍" hoặc "Maria from [Brand]"

→ Personal sender name → personal vibe → inbox tab.

### 6. Unsubscribe link giấu/khó tìm
- Phải có theo luật (CAN-SPAM, GDPR)
- Visible nhưng không hard-sell ("xin đừng đi 😭")
- Đơn giản: "Unsubscribe" link nhỏ ở footer

---

## ✅ Self-Check trước khi send

- [ ] Email LOOKS personal (left-aligned, no fancy header/footer)?
- [ ] Sender name personal (vd: "Maria") not company?
- [ ] Subject line không CAPS / không "FREE / SALE / BUY"?
- [ ] Có ≥1 image OK personal (không stock)?
- [ ] 1 CTA chính (không 5 link)?
- [ ] Reply-back prompt nếu chưa có gần đây?
- [ ] Tone match brand (personal, không corporate)?
- [ ] Sign-off với tên thật?

---

## 📈 KPI tracking

| Metric | Industry avg | Maria | Mục tiêu |
|--------|-------------|-------|----------|
| Open rate | 15-20% | **30%** | ≥25% |
| Click rate | 2-3% | 5-8% | ≥4% |
| Unsub rate | 0.2-0.5% | 0.3% | <0.5% acceptable |
| Spam complaint | <0.1% | <0.05% | <0.1% |
| Promotions tab rate | 30-50% | <10% | <20% |

→ Nếu Open <15% → check Subject line + Sender name
→ Nếu Click <2% → check CTA clarity + body value
→ Nếu Unsub spike >1% → check pitch frequency, không "đấm" sau nurture

---

## 🔗 Tools mentioned

- [Active Campaign](https://www.activecampaign.com) — Maria's primary
- [Sam Cart](https://www.samcart.com) — Checkout (integrates với AC)
- [Manychat](https://manychat.com) — DM → email collection (free list-building)
- [Hyros](https://hyros.com) — Tracking attribution (advanced)
