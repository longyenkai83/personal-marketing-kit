---
name: kallaway-script-master
description: Viết kịch bản video viral (60s-15min) theo phương pháp Kallaway — kết hợp 6 Levels of Storytelling (Reporter→Artist), 4 Blockers (Research/Hook/Structure/Engagement), và 6 Story Locks (Naming/Embedded Truths/Thought Articulation/Negative Frames/Loop Openers/Contrast Words). Use when user wants to write/audit/improve full video script (>15s), kịch bản reels dài, kịch bản long-form, audit retention curve, viết kịch bản giữ chân người xem. Vietnamese-first. Triggers — "viết kịch bản", "script video", "kịch bản long-form", "audit script", "tăng retention", "story locks", "6 levels storytelling".
allowed-tools: Read, Grep, Glob
argument-hint: "[topic] [duration: 30s|60s|3min|10min] [emotion?]"
---

# Kallaway Script Master

Phương pháp viết kịch bản video full (60s → 15min) theo Kallaway. Complement với `kallaway-hook-master` (chuyên 3-5s đầu).

## When to invoke

VN trigger phrases:
- "viết kịch bản video / reel / short / tiktok"
- "viết script long-form"
- "audit kịch bản cũ"
- "tăng retention video"
- "kịch bản giữ chân người xem"
- "áp dụng 6 levels storytelling"
- "story locks kallaway"

User can also invoke `/kallaway-script-master` directly.

**Do NOT use for:**
- Hook < 5s standalone (dùng `kallaway-hook-master`)
- Caption text-only không có video (dùng `content-engine`)
- Email sequence (dùng `email-marketing-writer` khi có)

**Workflow chain**:
```
kallaway-hook-master (3-5s đầu) → kallaway-script-master (full 60s+) → kallaway-edit (optional, future skill)
```

## Required inputs (ask user if missing)

Hỏi 1 lần gộp:

1. **Topic** — chủ đề video
2. **Duration** — `30s` / `60s` / `3min` / `10min` / `15min+`
3. **Format** — `tiktok_reels` / `youtube_short` / `youtube_long` / `live_replay`
4. **Persona target** — đối tượng (default load từ niche-pack)
5. **Goal** — `awareness` / `lead` / `sale` / `educate` / `entertain`
6. **Cảm xúc mục tiêu** — bất ngờ / hào hứng / tức giận / vui vẻ / buồn / inspired (chỉ chọn 1 dominant)
7. **Hero Visual có sẵn?** — yes/no + mô tả
8. **CTA cuối** — hành động cụ thể audience làm

## 3 Frameworks chồng lớp

Skill này áp dụng **đồng thời** 3 framework Kallaway:

### Framework A — 6 Levels of Storytelling (Story Ladder)
> *Càng cao càng giữ chân — hầu hết creator mắc kẹt ở Level 1-2.*

| Level | Tên | Bản chất | Audit question |
|-------|-----|----------|----------------|
| 1 | **Reporter** | Liệt kê trình tự, dễ đoán | Có dễ đoán không? Boring không? |
| 2 | **Trickster** | Hooks + misdirection (mỗi 2-3 phút) | Có ≥1 hook/2-3 phút? |
| 3 | **Warrior** | Gắn pain/goal cụ thể | Audience có lý do để xem tiếp? |
| 4 | **Architect** | Beats + arcs (segments rõ) | Mỗi segment có: Chuyện gì? Tại sao? Ví dụ? Action? |
| 5 | **Translator** | Visual + analogy max comprehension | Audience hiểu 100% mỗi câu chưa? |
| 6 | **Artist** | Signature cá nhân | Có "DNA" riêng không? |

→ Chi tiết: `references/6-levels-storytelling.md`

### Framework B — Viral Script 4 Blockers
> *4 lý do video không viral — fix từng cái.*

| Blocker | Fix | Output |
|---------|-----|--------|
| **Interest Blocker** | Research 5-10 shock facts, score 1-100 | Top fact để đặt nền video |
| **Hook Blocker** | Chọn 1 trong 9 hook format, viết 3 variant | Hook script aligned 4 component |
| **Structure Blocker** | Chọn 1 trong 7 cấu trúc câu chuyện | Outline có chunks rõ |
| **Engagement Blocker** | Chọn 1 cảm xúc dominant, khuếch đại xuyên suốt | Script có "đường cong cảm xúc" |

→ Chi tiết: `references/viral-script-4-blockers.md`

### Framework C — 6 Story Locks (giữ chú ý dòng dòng)
> *Thay vài từ trong script = retention tăng vọt. Underlying = Contrast.*

| Lock | Áp dụng | Tâm lý học |
|------|---------|------------|
| **Naming** | Đặt tên 2-3 concept cốt lõi | Labeling Effect |
| **Embedded Truths** | Thay "nếu/có thể/có lẽ" → "khi/lý do tại sao" | Authority bias |
| **Thought Articulation** | Sau big claim, nói ra điều người xem nghĩ | Mind-reading effect |
| **Negative Frames** | Flip positive → negative framing | Negativity Bias |
| **Loop Openers** | Transition contrast mỗi 30-60s | Hourglass Attention Model |
| **Contrast Words** | "Nhưng / thay vì / tuy nhiên" tạo tension | Contrast Mechanism (foundation) |

→ Chi tiết: `references/6-story-locks.md`

## Methodology — 8-step Script Writing Workflow

### Step 1: Define inputs (8 question gộp ở trên)

### Step 2: Research — Find Top Shock Fact (Interest Blocker fix)
- Tìm 5-10 facts về topic
- Score 1-100 theo độ "shock" (100 = gần như không ai biết)
- Top fact → đặt làm nền video
- Prompt mẫu: *"Tìm 10 sự thật bất ngờ nhất về [topic] mà đa số không biết. Chấm shock 1-100."*

### Step 3: Hook (3-5s đầu) — Delegate to kallaway-hook-master
- Invoke `kallaway-hook-master` với top shock fact + Hero Visual
- Output: hook script + alignment check
- Skip nếu user đã có hook proven

### Step 4: Structure — Choose Story Architecture
Chọn 1 trong **7 structure chính**:

1. **Breakdown** — phá thứ phức tạp thành parts dễ hiểu
2. **List** — N reasons / N steps / N mistakes
3. **Problem-Solution** — pain → solution
4. **Tutorial** — step-by-step làm theo
5. **Case Study** — story 1 nhân vật cụ thể
6. **Compare-Contrast** — A vs B
7. **Hot Take** — opinion mạnh + back up

### Step 5: Apply 6 Levels Storytelling — Layer by Layer

**Bắt buộc Level 2 + 3** (most creators stuck here):
- **Level 2 Trickster**: Misdirection mỗi 2-3 phút (cho video >3min) hoặc 15-20s (cho short-form)
- **Level 3 Warrior**: Mở video bằng pain point cụ thể của persona

**Apply Level 4 cho video >60s**:
- Chia thành 3-5 segments
- Mỗi segment = 4 blocks: **Chuyện gì? Tại sao? Ví dụ? Action?**
- Story Navigation: audience pause bất kỳ lúc nào, tự biết mình đang ở đâu

**Apply Level 5 ở mọi câu**:
- Visual aid mỗi big claim
- Analogy thay số liệu khô (vd: "1/600" → "máy bay bay trên đường cao tốc")
- Self-check: "Có chỗ nào audience có thể bị confused không?"

**Level 6 Artist**: Chỉ áp dụng nếu user đã có signature riêng (vd: cách giải thích, catchphrase, edit style)

### Step 6: Apply 6 Story Locks (mỗi 30-60s)

Pass qua script vừa viết, scan & fix:
- ✅ Naming: 2-3 concept đã có tên độc đáo chưa?
- ✅ Embedded Truths: Đã thay "nếu/có thể" → "khi/lý do" chưa?
- ✅ Thought Articulation: Sau big claim đã nói "Bạn đang nghĩ X..." chưa?
- ✅ Negative Frames: Có 1-2 điểm flip negative chưa?
- ✅ Loop Openers: Mỗi 30-60s có "nhưng/tuy nhiên" để bridge chưa?
- ✅ Contrast Words: Transitions có tension không?

### Step 7: Engagement Check (Engagement Blocker fix)

- **Cảm xúc mục tiêu khuếch đại**: từ ngữ trong script có tăng cường cảm xúc dominant không?
- **Đường cong cảm xúc**: Có ít nhất 1 "chuyển hóa cảm xúc" lớn (vd: từ tức giận → giải tỏa, từ confused → clarity)?

### Step 7.5: CTA Selection (BẮT BUỘC — read `references/cta-library.md`)

**KHÔNG mặc định mọi video đều "comment X nhận DM Y"** — đây là anti-pattern lớn nhất.

**Workflow chọn CTA**:
1. Identify TOPIC TYPE (pháp lý / tutorial / mindset / viral / launch / brand / education)
2. Match với **Decision Tree** trong `cta-library.md` → suggest CTA type phù hợp
3. Check user's recent CTA history (nếu có) → tránh lặp pattern
4. Apply **70/20/10 rule**: 70% Educational+Reflection+Save / 20% Discussion+Share+Action / 10% Lead-gen+Follow
5. Generate CTA cụ thể (≤10s, actionable trong 24h)
6. **Nêu rõ CTA type chosen + lý do** trong Output

**Topic mapping nhanh**:
- Pháp lý/thuế/sức khỏe → **Educational + Save** (KHÔNG Lead-gen)
- Tutorial/how-to → **Action + Save**
- Mindset/transformation → **Reflection + Discussion**
- Viral fact/news → **Share/Tag + Discussion**
- Product launch → **Lead-gen** (chỉ khi có lead magnet xịn)
- Brand building → **No CTA** (insight cuối) + **Follow**
- Education/concept → **Save + Educational + Discussion**

### Step 8: Output script + audit report

Output Format (xem dưới).

## Output Format

```markdown
## Script — [Topic] ([Duration])

**Persona**: [tên]
**Goal**: [awareness/lead/sale/educate/entertain]
**Cảm xúc dominant**: [emotion]
**Cấu trúc chọn**: [1 trong 7 structures]
**Top shock fact**: [fact + score]

---

### 🎯 HOOK (0-5s) — delegated to kallaway-hook-master
**Spoken**: "[hook]"
**Text overlay**: "[≤7 từ]"
**Hero Visual**: [mô tả]

---

### 📖 BODY ([5s → end-15s])

#### Segment 1: [Title] (5-Xs)
**Chuyện gì?** [content]
**Tại sao quan trọng?** [content]
**Ví dụ?** [content]
**Action/Insight?** [content]

[Visual cue: ...]
[Loop opener trước segment 2: "Nhưng..."]

#### Segment 2: [Title]
... (lặp 2-4 segments)

---

### 🎬 CTA (last 15s)
**Lời thoại**: "[CTA]"
**Visual**: [end card / next video preview]

---

### ✅ AUDIT REPORT — 3 Frameworks Check

**6 Levels Storytelling**:
- Level 1 (Reporter): ❌ avoided
- Level 2 (Trickster): ✅ Misdirection at 0:15, 0:35, 0:50
- Level 3 (Warrior): ✅ Pain point opened: "[pain]"
- Level 4 (Architect): ✅ 3 segments, mỗi segment có 4 blocks
- Level 5 (Translator): ✅ 2 analogies + 1 visual aid
- Level 6 (Artist): ⏳ User signature TBD

**4 Blockers**:
- Interest: ✅ Top shock fact score [X]/100
- Hook: ✅ Aligned 4 component
- Structure: ✅ [structure name] chosen
- Engagement: ✅ Dominant emotion: [X], 1 emotional transition at [Xs]

**6 Story Locks**:
- Naming: ✅ 2 concepts named: "[name1]", "[name2]"
- Embedded Truths: ✅ 4 hesitation words replaced
- Thought Articulation: ✅ 2 "you're thinking..." moments
- Negative Frames: ✅ 1 flip applied at [moment]
- Loop Openers: ✅ 3 bridges with contrast words
- Contrast Words: ✅ 5 contrast transitions

---

### 📊 KPI Target
- 5-sec retention: ≥50%
- Average view duration: ≥60% of video length
- Saves: ≥1% of reach
- CTA conversion: track via [link/code/comment]
```

## Integration with other skills

| Skill | When to chain | How |
|-------|---------------|-----|
| `kallaway-hook-master` | TRƯỚC khi viết script | Tạo hook 3-5s đầu (Step 3) |
| `hook-swipe-library` | Nếu cần inspiration | Query 72-hook bank để remix |
| `content-engine` | SAU khi script ready | Stage 4 → gen caption + hashtag đi kèm |
| `fb-insight-miner` | TRƯỚC khi research | Lấy verbatim quote từ comment fanpage |

## Quality Standards

- ❌ KHÔNG bịa số liệu/testimonial → dùng `[stat_X_placeholder]` / `[testimonial_X_placeholder]`
- ❌ KHÔNG paraphrase verbatim quote khách
- ❌ KHÔNG output toàn script Level 1 (Reporter pure)
- ✅ Mọi script PHẢI ít nhất Level 2 + Level 3 (Trickster + Warrior)
- ✅ Mọi script >60s PHẢI có Level 4 (Architect — segments rõ)
- ✅ Apply ≥4/6 Story Locks vào script cuối
- ✅ Self-test 3 lần trước khi ship (silent / eyes closed / full)

## Failure modes

- **Retention curve dips at 15s** → Level 2 Trickster yếu, thêm misdirection sớm hơn
- **Audience drop sau 30s** → Story Locks chưa apply, đặc biệt Loop Openers
- **Comments confused** → Level 5 Translator yếu, audit từng câu, thêm analogy
- **Comments "OK but boring"** → Stuck Level 1-2, thiếu Level 3 (pain/goal cá nhân)
- **Generic, đụng đám đông** → Thiếu Level 6 (Artist signature), force ≥1 unique element

## Reference Files

- `references/6-levels-storytelling.md` — Story Ladder full
- `references/viral-script-4-blockers.md` — 4 Blockers + 9 Hook formats + 7 structures
- `references/6-story-locks.md` — Story Locks + tâm lý học underlying
- `references/cta-library.md` — **9 loại CTA** (Educational/Reflection/Save/Share/Discussion/Action/Lead-gen/Follow/No CTA) + Decision Tree + 70/20/10 rotation rule
- `templates/script-worksheet.md` — End-to-end worksheet 8-step

## Status

**v1.0** — built từ Kallaway materials Phase 2 (6 Levels Storytelling + How to Script Viral Videos 10x Faster + 6 Story Locks). Niche default: phụ nữ KD VN. Mở rộng qua thêm `niche-packs/` (future).
