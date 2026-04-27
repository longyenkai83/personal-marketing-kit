# 📖 Hướng Dẫn Sử Dụng — Personal Marketing Kit

> **Cho phụ nữ KD VN — không cần technical background.**
> 
> Đọc 30 phút → biết cách dùng 12 skill AI làm marketing thay anh chị.

---

## 🎯 Tổng quan

**Personal Marketing Kit** (gọi tắt: **Bộ Kit** hoặc **Bộ Trợ Lý AI**) là 12 "skill" AI build sẵn cho Claude Code.

Sau khi cài (5 phút), anh chị chỉ cần **gõ 1 câu yêu cầu** → AI tự động:
- Pick skill phù hợp
- Apply phương pháp Maria Wendt × Kallaway
- Output content / email / strategy theo tone "anh-chị-em" tiếng Việt

→ **KHÔNG cần code. KHÔNG cần học framework. KHÔNG cần thuê freelancer.**

---

## 🚀 BẮT ĐẦU — 4 BƯỚC (chỉ làm 1 LẦN)

### Bước 1: Cài Claude Code
→ Xem [docs/INSTALL-VN.md](docs/INSTALL-VN.md)

### Bước 2: Tải kit về máy + drop vào `~/.claude/`
→ Xem [docs/INSTALL-VN.md](docs/INSTALL-VN.md)

### Bước 3: Restart Claude Code

### Bước 4: Test
Gõ trong Claude Code:
```
Tôi có những skill nào trong kit?
```

✅ PASS nếu Claude liệt kê 10 skill → setup OK.

→ Detail: [docs/INSTALL-VN.md](docs/INSTALL-VN.md)

---

## 💡 NGUYÊN TẮC SỬ DỤNG

### Nguyên tắc 1: NÓI CHUYỆN VỚI AI NHƯ NÓI CHUYỆN VỚI BẠN BÈ

❌ Đừng gõ: *"Generate viral hook framework Kallaway 11 types"*
✅ Gõ: *"Viết 5 hook viral cho video về đóng gói chuyên môn"*

→ AI hiểu cả 2, nhưng cách 2 tự nhiên hơn + AI biết apply context VN tốt hơn.

### Nguyên tắc 2: CHO AI CONTEXT CỤ THỂ

❌ *"Viết caption"*
✅ *"Viết caption FB cho topic 'launch khoá pilates' — audience phụ nữ 30-40, mom-preneur, ngại lộ mặt"*

→ Context càng cụ thể → output càng đúng.

### Nguyên tắc 3: AI SẼ TỰ HỎI ANH CHỊ NẾU THIẾU INFO

Đừng cố gõ tất cả thông tin trong 1 câu. Cứ gõ ngắn → AI hỏi thêm:
- *"Persona target của chị là ai?"*
- *"Goal awareness / lead / sale?"*
- *"CTA gì?"*

→ Trả lời từng câu → AI build output đúng nhu cầu.

### Nguyên tắc 4: ĐỌC OUTPUT + CUSTOMIZE

AI output là **starting point**, KHÔNG phải final. Anh chị edit:
- Voice của chị (signature phrases)
- Số liệu thật (replace placeholder)
- Câu chuyện cá nhân (vulnerable touch)

→ AI làm 80% — chị làm 20% personalization.

### Nguyên tắc 5: TEST + ITERATE

First reel/email không cần perfect. Đăng → thu data → iterate.

→ Maria Wendt: *"Publish your rough first draft."*

---

## 🛠 12 SKILL — KHI NÀO DÙNG SKILL NÀO

### 🔍 NHÓM 1: NGHIÊN CỨU KHÁCH HÀNG

#### `fb-insight-miner`
**Khi dùng**: Muốn hiểu sâu pain/desire của audience từ FB fanpage thật

**Gõ**:
```
Đào insight fanpage [URL] cho ngách [X], depth standard
```

**Output**: 50-page customer insight report (~$4 cost)

**Ví dụ**:
```
Đào insight fanpage https://www.facebook.com/lphan
cho ngách phụ nữ KD đóng gói chuyên môn, depth standard
```

---

### 🎬 NHÓM 2: HOOK + SCRIPT VIDEO

#### `kallaway-hook-master`
**Khi dùng**: Cần hook 3-5 giây đầu video viral

**Gõ**:
```
Viết 5 hook viral cho topic [X] cho phụ nữ KD VN, theo Kallaway framework
```

**Output**: 5 hook đa framework (Fortune Teller, Contrarian, Investigator, etc) + alignment check

**Ví dụ**:
```
Viết 5 hook viral cho topic 'sản phẩm số đầu tiên' 
cho phụ nữ KD 30-40 đã có chuyên môn, temperature lạnh
```

---

#### `kallaway-script-master`
**Khi dùng**: Cần kịch bản full 60s+ video

**Gõ**:
```
Viết kịch bản 60s video cho topic [X], cảm xúc [Y], CTA [Z]
```

**Output**: Full script + shotlist + audit 3 frameworks (6 Levels + 4 Blockers + 6 Story Locks)

**Ví dụ**:
```
Viết kịch bản 60s video cho topic 'Welcome Coupon $50k/tháng', 
cảm xúc bất ngờ, CTA Educational + Save (KHÔNG comment X nhận DM)
```

---

#### `hook-swipe-library`
**Khi dùng**: Muốn lấy hook đã proven sẵn (không cần generate)

**Gõ**:
```
Tìm hook trong bank cho ngách [X], temperature [Y], framework [Z]
```

**Output**: 3-5 hook candidates từ 72-hook bank women-biz-vn

**Ví dụ**:
```
Tìm hook trong bank cho ngách phụ nữ KD đóng gói chuyên môn, 
temperature nóng, framework Case Study
```

---

#### `content-engine`
**Khi dùng**: Cần caption FB/IG bài bản (4-stage VPC pipeline)

**Gõ**:
```
Apply content-engine cho persona [X] với niche-pack [Y]
```

**Output**: Customer profile → insights → hooks → 12 captions ready-to-post

**Ví dụ**:
```
Apply content-engine cho persona 'phụ nữ KD 35 muốn launch mini-course $37'
với niche-pack women-biz-vn, generate 12 captions
```

---

### 🎁 NHÓM 3: LEAD MAGNET

#### `lead-magnet-factory`
**Khi dùng**: Cần build PDF freebie để capture email

**Gõ**:
```
Build lead magnet topic [X] cho persona [Y]
```

**Output**: 9-page outline + Canva-ready CSV

**Ví dụ**:
```
Build lead magnet topic '10 Câu Hỏi Trước Khi Đóng Gói Chuyên Môn'
cho persona phụ nữ KD VN có chuyên môn
```

---

### 📨 NHÓM 4: EMAIL MARKETING

#### `email-marketing-writer`
**Khi dùng**: Cần viết email (welcome / launch / nurture / pitch / 9-word)

**Gõ**:
```
Viết [type email] cho topic [X], persona [Y], CTA [Z]
```

**Email types**:
- `welcome_automation` — 5-email sequence sau opt-in
- `launch` — 5-7 email cash spike sequence
- `nurture` — story + value
- `pitch` — sales-focused
- `9_word_reengage` — re-activate cold list

**Ví dụ**:
```
Viết welcome 5-email sequence cho lead magnet '10 Câu Hỏi'
persona phụ nữ KD VN, tripwire offer 25k worksheet
```

```
Viết 9-word email re-activate cold list không nhận email 90 ngày
topic 'launch khoá đóng gói chuyên môn'
```

---

### 💰 NHÓM 5: TRIPWIRE + DIGITAL PRODUCT

#### `tripwire-builder`
**Khi dùng**: Build $1-7 entry funnel + Welcome Coupon flow

**Gõ**:
```
Build tripwire 25k topic [X] với mid-tier 890k là [Y]
```

**Output**: Tripwire content + Welcome Coupon 4-email flow + post-purchase 5-email

**Ví dụ**:
```
Build tripwire 25k worksheet 'Đóng gói chuyên môn 30 ngày'
với mid-tier 890k là 'Mini-course Personal Brand IG'
```

---

#### `digital-product-builder`
**Khi dùng**: Validate idea sản phẩm số / build / plan launch

**Gõ**:
```
Apply digital-product-builder cho idea [X]:
- Run 3-Pillar test
- Find expertise (3 questions)
- Suggest pricing + tech stack
```

**Ví dụ**:
```
Apply digital-product-builder cho idea 'Mini-course Personal Brand IG cho phụ nữ KD':
- Persona: phụ nữ 30-45, đã có chuyên môn coaching
- Stage: validate
- Pricing target: 890k

Run 3-Pillar test + find-your-expertise + ROI angles
```

---

### 🛠 NHÓM 6: META

#### `subagent-architect`
**Khi dùng**: Build skill mới hoặc audit skill cũ

**Gõ**:
```
Build subagent cho [task X] hoặc Audit subagent file [Y]
```

→ Advanced — chỉ dùng khi anh chị muốn extend kit.

---

## 🎯 4 WORKFLOW MẪU

### Workflow A: Build full launch (1-2 tuần)
→ [docs/WORKFLOW-A.md](docs/WORKFLOW-A.md) — chi tiết step-by-step

**Tóm tắt**:
1. Validate idea (`digital-product-builder`)
2. Build PDF freebie (`lead-magnet-factory`)
3. Setup tripwire (`tripwire-builder`)
4. Welcome email sequence (`email-marketing-writer`)
5. 5 reel scripts (`kallaway-hook-master` + `script-master`)
6. 30 caption batch (`content-engine`)

---

### Workflow B: Single reel + caption (30 phút)
→ [docs/WORKFLOW-B.md](docs/WORKFLOW-B.md) — chi tiết

**Tóm tắt**:
1. Pick topic (5 phút)
2. Generate hook (`kallaway-hook-master` — 5 phút)
3. Generate script (`kallaway-script-master` — 10 phút)
4. Generate caption (`content-engine` — 5 phút)
5. Self-check + ship (5 phút)

---

### Workflow C: Audit script cũ (15 phút)
→ [docs/WORKFLOW-C.md](docs/WORKFLOW-C.md)

**Tóm tắt**:
- Paste script cũ
- AI audit theo 6 Levels + 6 Story Locks + 4 Blockers
- Get revised script + reasoning

---

### Workflow D: Customer research (45 phút, ~$4)
→ [docs/WORKFLOW-D.md](docs/WORKFLOW-D.md)

**Tóm tắt**:
- Setup Apify MCP
- Run `fb-insight-miner` cho fanpage đối thủ
- Update niche-pack với verbatim mới
- Generate fresh hooks based on real data

---

## 🆘 TROUBLESHOOTING — LỖI HAY GẶP

### Lỗi 1: Claude không liệt kê được skill

**Triệu chứng**: Gõ "Tôi có skill nào" → Claude hỏi "kit nào?"

**Fix**:
1. Check file `~/.claude/CLAUDE.md` có tồn tại không
2. Restart Claude Code (đóng hoàn toàn → mở lại)

---

### Lỗi 2: Skill không trigger đúng

**Triệu chứng**: Gõ "viết hook" → Claude generic, không apply Kallaway

**Fix**:
1. Trigger explicit: *"Apply skill kallaway-hook-master cho topic X"*
2. Check folder `~/.claude/skills/2-content/kallaway-hook-master/SKILL.md` có tồn tại không

---

### Lỗi 3: Output xưng "bạn" thay vì "anh/chị/em"

**Fix**:
- Check CLAUDE.md có section "QUY ƯỚC TUYỆT ĐỐI" với rule xưng hô
- Restart Claude Code

---

### Lỗi 4: Output English thay vì Việt

**Fix**:
- Add vào câu hỏi: "Output bằng tiếng Việt"
- Hoặc check CLAUDE.md có rule "Vietnamese-first"

---

### Lỗi 5: Slow / timeout

**Fix**:
- Check internet
- Check Claude Pro subscription còn balance
- Break task lớn thành nhỏ (vd: thay vì "Apply content-engine 4 stages cùng lúc" → từng stage 1)

---

## 💡 PRO TIPS

### Tip 1: BATCH content theo tuần

Sunday session 3-4h:
- 5 reel scripts (Workflow B × 5)
- 30 captions (content-engine batch)
- 5 emails

→ Cả tuần có content đăng — không phải "ngồi nghĩ mỗi ngày".

### Tip 2: SAVE prompts hay dùng

Tạo file `~/my-prompts.md` lưu prompts proven:
```
1. "Viết 5 hook cho topic X persona phụ nữ KD VN"
2. "Build welcome 5-email sequence cho lead magnet Y"
3. "Audit script này theo Kallaway 6 Story Locks: [paste]"
```

→ Copy-paste tái sử dụng, không phải gõ từ đầu.

### Tip 3: COMBINE skills theo workflow

KHÔNG dùng từng skill riêng lẻ. Combine:
- Hook → Script → Caption (B workflow)
- Lead magnet → Email → Tripwire (full funnel)
- Insight miner → Niche pack update → Hook generate (research → action)

### Tip 4: TRACK kết quả

Tạo Notion / Sheet track:
| Date | Skill used | Output | Result (reach/sale) |
|------|-----------|--------|---------------------|
| ... | ... | ... | ... |

→ Sau 30 ngày → biết skill nào ROI cao nhất.

### Tip 5: CUSTOMIZE niche-pack riêng

Nếu ngách của chị KHÔNG match `women-biz-vn` default:
- Copy `~/.claude/shared/niche-packs/_universal.json`
- Save thành `[your-niche].json`
- Customize với data của chị
- Reference trong skill: "Apply skill X với niche-pack [your-niche]"

---

## 📊 KHI NÀO CẦN UPGRADE

Bộ kit FREE đủ cho 80% phụ nữ KD VN. Upgrade khi:

### 🎓 1-1 Onboarding (5tr)
**Khi nào**: Anh chị đã cài kit nhưng "không biết bắt đầu từ đâu"
**Em làm**: 60 phút Zoom call onboarding + customize kit cho business cụ thể

### 💎 VIP Cohort 4 weeks (15tr)
**Khi nào**: Anh chị muốn launch trong 4 tuần với pace + accountability
**Em làm**: Group coaching mỗi thứ 7 + private community + 1-1 review feed/script/email

### 👑 Done-For-You (50tr+)
**Khi nào**: Anh chị KHÔNG có thời gian execute, chỉ muốn ship
**Em làm**: Build kit fully customized + setup tech stack (Kajabi + Sam Cart + Active Campaign) + quay video walkthrough team chị

→ **Liên hệ**: [Contact link / DM] *(replace với contact thật của anh)*

---

## 📚 THAM KHẢO THÊM

| Tài liệu | Mục đích |
|----------|---------|
| [README.md](README.md) | Sales pitch overview + customer journey diagram |
| [CLAUDE.md](CLAUDE.md) | Hub auto-load (decision tree + 5 agent roles + tech stack) |
| [docs/INSTALL-VN.md](docs/INSTALL-VN.md) | Cài đặt step-by-step có ảnh |
| [docs/WORKFLOW-A.md](docs/WORKFLOW-A.md) | Build full launch (1-2 tuần) |
| [docs/WORKFLOW-B.md](docs/WORKFLOW-B.md) | Single reel + caption (30 phút) |
| [docs/WORKFLOW-C.md](docs/WORKFLOW-C.md) | Audit script cũ (15 phút) |
| [docs/WORKFLOW-D.md](docs/WORKFLOW-D.md) | Customer research (45 phút) |
| [CHANGELOG.md](CHANGELOG.md) | Version history + roadmap |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribute back to community |

---

## 🎯 30 NGÀY ĐẦU — CHECKLIST

Tuần 1:
- [ ] Cài Claude Code + drop kit (5 phút)
- [ ] Test 3 verify queries → all PASS
- [ ] Đọc CLAUDE.md hub (10 phút) — overview kit
- [ ] Đọc HUONG-DAN-SU-DUNG.md (file này) — biết khi nào dùng skill nào
- [ ] Run Workflow B 1 lần (Single reel + caption — 30 phút)
- [ ] Đăng 1 reel test → đo reach 48h

Tuần 2:
- [ ] Run Workflow A (full launch validate idea — `digital-product-builder`)
- [ ] Build lead magnet PDF (`lead-magnet-factory`)
- [ ] Setup welcome email (`email-marketing-writer`)
- [ ] Setup tripwire (`tripwire-builder`)

Tuần 3:
- [ ] Quay 5 reel theo Workflow B × 5 (batching session)
- [ ] Đăng 5 reel + track engagement
- [ ] Email broadcast 1-2/tuần

Tuần 4:
- [ ] Audit reel performing thấp nhất (Workflow C)
- [ ] Iterate dựa trên data
- [ ] Plan tháng 2 (scale paid ads / collab / etc)

→ Sau 30 ngày, anh chị nên có:
- ✅ 5+ reel đăng
- ✅ Lead magnet capturing email
- ✅ Welcome email automation chạy
- ✅ Tripwire $1-25k flow live
- ✅ First 5-10 paying customers
- ✅ First 10 triệu revenue

→ All ✅ = product validated. Scale paid ads + ramp tháng 2-3.

---

## 💚 LỜI CUỐI TỪ EM

Anh chị đang đầu tư vào CHÍNH MÌNH bằng cách dùng kit này.

Em đã đầu tư 200+ giờ build kit — Maria Wendt + Kallaway + Dean Jackson — adapt cho thị trường VN.

**Kit này KHÔNG MAGIC.** Anh chị vẫn phải:
- Đăng đều
- Reply DM nhanh
- Customize theo voice của mình
- Iterate dựa trên feedback

**Nhưng kit GIẢM 80% effort + tăng quality output 5-10x** — vs làm thủ công.

Phụ nữ KD VN xứng đáng có hệ thống chuẩn quốc tế (Maria $18M).
Kit này là cách em **dân chủ hoá** kiến thức đó cho ngách của chúng ta.

Best of luck với launch đầu tiên! 🚀

— [@longyenkai83](https://github.com/longyenkai83) 🤍

---

**P.S.** Nếu kit giúp anh chị → ⭐ star repo + share với 1 phụ nữ KD khác cần.

**P.P.S.** Có question / feedback / bug → [open issue](https://github.com/longyenkai83/personal-marketing-kit/issues) trên GitHub. Em reply trong 24h.
