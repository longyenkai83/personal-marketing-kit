# Viral Script — 4 Blockers Framework (Kallaway)

Nguồn: "How to Script Viral Videos 10x Faster (Nobody Teaches This)"

## Tại sao 4 Blockers?

> Mỗi video không viral đều bị 1 trong 4 BLOCKER chặn. Identify đúng blocker → fix → viral.

| Blocker | Triệu chứng | Fix |
|---------|-------------|-----|
| **Interest** | Audience không quan tâm topic | Research shock facts |
| **Hook** | Drop sau 3-5s | Hook 4 component aligned |
| **Structure** | Drop giữa video | Cấu trúc câu chuyện rõ |
| **Engagement** | Xem xong không action | Cảm xúc dominant + transformation |

---

## 🔍 BLOCKER 1: INTEREST — Research

**Vấn đề**: Topic quá quen thuộc → không ai care.

**Fix**: Tìm **5-10 SHOCK FACTS** về topic — facts mà 90%+ audience không biết.

### Process

1. **Brainstorm 10 facts** về topic
2. **Score mỗi fact 1-100** theo độ shock:
   - 100 = gần như không ai biết, cực kỳ bất ngờ
   - 70-90 = nhiều người không biết, surprising
   - 40-70 = một số biết, mildly interesting
   - <40 = phổ biến, bored

3. **Top fact** (score cao nhất) = NỀN cho video

### Prompt mẫu (Claude/GPT)

> *"Tôi đang làm video về [topic]. Hãy tìm 10 sự thật bất ngờ nhất về chủ đề này mà đa số người không biết. Chấm điểm mỗi fact từ 1-100 theo độ shock (100 = gần như không ai biết, cực kỳ bất ngờ). Sắp xếp từ cao đến thấp. Format: [Score] | [Fact] | [Source nếu có]"*

### Ví dụ — Topic "Email Marketing"

| Score | Fact |
|-------|------|
| 95 | Email có ROI $42 cho mỗi $1 spent — cao gấp 2x mọi kênh khác |
| 85 | 81% người dùng smartphone check email NGAY khi thức dậy — trước cả social |
| 70 | Subject line ≤7 từ có open rate cao hơn 21% so với dài |
| 50 | Tuesday 10am là thời điểm gửi email best practice |
| 30 | Email cần subject line (ai cũng biết) |

→ Top facts (95 + 85) = nền cho video. Skip facts <50.

### Common mistake

❌ Skip step research, viết script luôn → topic generic
✅ Đầu tư 30 phút research → tìm 1-2 fact "wow" → toàn bộ video xoay quanh

---

## 🎣 BLOCKER 2: HOOK — 9 Hook Formats

**Vấn đề**: Audience xem 2-3s đầu rồi scroll.

**Fix**: Hook đúng format, aligned 4 component (Spoken + Text + Visual + Audio).

→ Chi tiết hook viết bằng `kallaway-hook-master` skill (delegate).

### 9 Hook Formats Kallaway

Tổng hợp từ 6 frameworks chính + 3 dạng phụ:

| # | Format | Template VN |
|---|--------|-------------|
| 1 | **Secret Reveal** | "Có 1 [bí mật] mà ít ai biết — đây là..." |
| 2 | **Case Study** | "[Tên] vừa [kết quả] bằng [Y]" |
| 3 | **Question** | "[Câu hỏi tạo curiosity]?" |
| 4 | **Contrarian** | "Mọi người nghĩ X — thực ra Y" |
| 5 | **Problem** | "Nếu bạn đang [pain] — đây là..." |
| 6 | **Fortune Teller** | "[X] này sẽ thay đổi cách bạn [Y]" |
| 7 | **Experimenter** | "Tôi vừa thử [X] — đây là kết quả" |
| 8 | **Teacher** | "Tôi từng [sai], đây là [N] thứ học được" |
| 9 | **Magician** | Pattern interrupt + 1 trong 8 trên |

### Workflow

1. **Nghiên cứu 5 video viral trong niche** — xác định Hook format nào xuất hiện nhiều nhất
2. **Mỗi niche có 1-2 format hoạt động tốt nhất** — đừng đoán mò, follow data
3. **Viết 3 phiên bản hook** theo 3 format khác nhau
4. **A/B test** → chọn cái hook mạnh nhất

### Tool

- **sortfeed.com** — sort videos theo views để find winning hooks trong niche
- **kallaway-hook-master** skill — generate hook + alignment check
- **hook-swipe-library** skill — query 72 proven hooks

---

## 🏗 BLOCKER 3: STRUCTURE — 7 Story Architectures

**Vấn đề**: Audience drop giữa video — không biết đang xem gì, đi về đâu.

**Fix**: Chọn 1 trong 7 cấu trúc phù hợp niche.

### 7 Cấu Trúc Câu Chuyện

#### 1. BREAKDOWN (Phân Rã)

**Khi dùng**: Topic phức tạp cần explain
**Cấu trúc**:
```
Hook → Topic là gì? → Chia thành N parts → Part 1 → Part 2 → Part 3 → Synthesis → CTA
```
**Ví dụ**: "Cách viral video hoạt động" → 4 parts (Hook + Story + Loop + CTA)

#### 2. LIST (Danh Sách)

**Khi dùng**: Curiosity + memorability
**Cấu trúc**:
```
Hook (N reasons/steps/mistakes) → #1 → #2 → ... → #N (best at end) → CTA
```
**Ví dụ**: "5 sai lầm khi launch khoá học — #5 sẽ làm bạn shock"

#### 3. PROBLEM-SOLUTION

**Khi dùng**: Pain point rõ + giải pháp cụ thể
**Cấu trúc**:
```
Hook (pain) → Pain detail → Tại sao pain tồn tại → Solution → How to apply → CTA
```
**Ví dụ**: "Fanpage im lặng → vì 3 lý do → fix bằng hệ thống X → 30 ngày làm theo"

#### 4. TUTORIAL (Hướng Dẫn)

**Khi dùng**: Step-by-step làm theo
**Cấu trúc**:
```
Hook (kết quả mơ ước) → Bước 1 → Bước 2 → ... → Bước N → Result demo → CTA
```
**Ví dụ**: "Cách build email funnel trong 60 phút — 5 bước"

#### 5. CASE STUDY

**Khi dùng**: Có testimonial/transformation thật
**Cấu trúc**:
```
Hook (kết quả nhân vật) → Background nhân vật → Pain trước → Action → Result sau → Lesson + CTA
```
**Ví dụ**: "Chị Lan từ 0 đến 30tr/tháng — đây là chính xác chị làm gì"

#### 6. COMPARE-CONTRAST

**Khi dùng**: A vs B, old way vs new way
**Cấu trúc**:
```
Hook (A vs B) → A là gì → B là gì → 3-5 điểm khác → Verdict → CTA
```
**Ví dụ**: "Bán khoá $37 vs $300 — cái nào ra nhiều tiền hơn?"

#### 7. HOT TAKE (Quan Điểm Mạnh)

**Khi dùng**: Personal brand, thought leader
**Cấu trúc**:
```
Hook (claim mạnh) → Tại sao mọi người sai → Tại sao tôi đúng → 3 evidence → CTA
```
**Ví dụ**: "Đừng bao giờ chạy ads cho khoá học $37 — đây là lý do"

### Chọn structure theo goal

| Goal | Structure khuyến nghị |
|------|------------------------|
| Awareness | Breakdown / Hot Take |
| Education | Tutorial / List |
| Lead generation | Problem-Solution / Case Study |
| Sale | Case Study / Compare-Contrast |
| Brand building | Hot Take / Case Study |

### Workflow

1. **Phân tích 5 video viral** trong niche → xác định structure nào dominant
2. **Chọn structure phù hợp goal**
3. **Điền top shock fact** (từ Blocker 1) vào outline
4. **Layer thêm** 6 Levels Storytelling + 6 Story Locks (xem reference khác)

---

## 💓 BLOCKER 4: ENGAGEMENT — Emotion Curve

**Vấn đề**: Xem xong audience không action — comment, save, share, click.

**Fix**: 1 cảm xúc DOMINANT + đường cong cảm xúc rõ.

### 5 Cảm Xúc Dominant (chọn 1 cho mỗi video)

| Emotion | Khi dùng | Ngôn ngữ | Action audience |
|---------|----------|----------|-----------------|
| **Bất ngờ** | Topic mới, insight độc quyền | "không ai nói cho bạn biết...", "thực ra..." | Save, share |
| **Hào hứng** | Tutorial, transformation | "bạn sẽ...", "imagine if...", "đây là cách" | Try it, comment |
| **Tức giận** | Hot take, callout | "đừng tin...", "họ đã lừa bạn..." | Share to vent |
| **Vui vẻ** | Entertainment, story | Humor, twist, funny analogy | Share to laugh |
| **Inspired** | Personal story, success | "tôi từng...", "bạn cũng có thể..." | Save, follow |
| **Buồn/empathy** | Vulnerability, relatable struggle | "tôi hiểu cảm giác...", "đã có lúc..." | Comment "same" |

### Đường Cong Cảm Xúc (Emotion Curve)

> **Video viral = có ít nhất 1 "chuyển hoá cảm xúc" lớn.**
>
> Vd: Tức giận (đầu) → Giải tỏa (cuối). Confused (đầu) → Clarity (cuối). Buồn (đầu) → Hopeful (cuối).

### Cách khuếch đại cảm xúc

#### Bất ngờ
- Câu mở: "Có 1 sự thật mà 99% người không biết..."
- Reveal: "Nhưng đây mới là điều shock thật sự..."
- Emoji ngầm: "..." trước reveal

#### Hào hứng
- Pace nhanh, câu ngắn
- "Imagine if...", "Bạn có thể..."
- Visual: success montage, before/after

#### Tức giận
- Callout cụ thể: "Họ đang lừa bạn vì..."
- Số liệu shock: "1 năm bạn đã mất X triệu vì..."
- Visual: red, fast cuts

#### Vui vẻ
- Twist bất ngờ
- Analogy hài hước
- Visual: meme, funny B-roll

#### Inspired
- Personal vulnerability mở
- Transformation story
- Visual: warm tone, slow zoom

### Engagement Check (cuối script)

- [ ] Cảm xúc dominant đã chọn từ đầu chưa?
- [ ] Ngôn từ trong script có khuếch đại cảm xúc đó xuyên suốt không?
- [ ] Có ít nhất 1 "chuyển hoá cảm xúc" lớn (đầu vs cuối khác emotion)?
- [ ] CTA cuối có khớp với cảm xúc dominant không?

### Common mistake

❌ Mix nhiều cảm xúc → audience confused về tone
✅ 1 dominant + 1 secondary tối đa

---

## 📋 4-Blocker Audit Worksheet (cho mỗi script)

```
SCRIPT: [tên]

BLOCKER 1 — INTEREST
Top shock fact: ___________ (score: ___/100)
Pass nếu top fact ≥70.

BLOCKER 2 — HOOK
Hook format: ___________ (1 trong 9)
3 variants written: [ ] Yes [ ] No
A/B test plan: ___________
Pass nếu aligned 4 component (delegate kallaway-hook-master).

BLOCKER 3 — STRUCTURE
Structure chọn: ___________ (1 trong 7)
Outline filled: [ ] Yes [ ] No
Story Navigation rõ: [ ] Yes [ ] No
Pass nếu segment có thể pause + biết đang ở đâu.

BLOCKER 4 — ENGAGEMENT
Cảm xúc dominant: ___________
Emotion curve: [đầu] → [cuối]
Ngôn từ khuếch đại cảm xúc: [ ] Yes [ ] No
Pass nếu có 1+ emotional transformation.
```

→ 4/4 Pass = ship.
→ <4/4 Pass = identify blocker, quay lại fix.

---

## 🛠 Tool

- **Sandcastles.ai** — AI áp dụng cả 4 blockers tự động
- **Claude prompt mẫu**: *"Apply 4 Blockers Framework Kallaway cho topic [X], output: shock facts list (scored), 3 hook variants, structure outline, emotion plan."*
