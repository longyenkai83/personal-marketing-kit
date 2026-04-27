# Workflow B — Single Reel + Caption (30 phút)

> **Quick win**: 1 reel video + caption FB/IG ready-to-shoot trong 30 phút
> 
> **Best for**: Weekly content batching, sau khi đã setup foundation từ Workflow A

---

## 🎯 Outcome target

Sau 30 phút:
- ✅ 1 reel script 60s với 11 framework Kallaway
- ✅ Hook 3-5s aligned 4 component (Spoken+Text+Visual+Audio)
- ✅ Shotlist quay được bằng iPhone
- ✅ Caption FB/IG đi kèm
- ✅ Hashtag set (3 broad + 5 niche + 2 branded)

---

## ⏱ 5-Step Process (30 phút)

### Step 1: Pick topic (5 phút)

**Sources** anh chị có thể pull topic từ:
- Hỏi mom/em/người KD trong network "Câu hỏi chị thường được hỏi nhất tháng này?"
- Comments trên reel cũ → pattern questions
- FB group target audience → trending discussions
- Maria Wendt subject line bank inspiration
- 72 hook bank (`shared/hook-banks/women-biz-vn-72.json`)

**Topic format**: SUPER SPECIFIC (không generic)

❌ "Cách build personal brand" (broad)
✅ "3 sai lầm phụ nữ KD mắc trong tuần đầu launch khoá học" (specific)

### Step 2: Generate hook (5 phút)

Open Claude Code → gõ:

```
Apply kallaway-hook-master.

Topic: [topic anh chị chọn]
Persona: phụ nữ KD VN [age range nếu specific]
Goal: [awareness / lead / sale / brand]
Temperature: [lanh / am / nong / banhang]
Format: video_60s

Output: 5 hook variants across 11 frameworks.
Apply 4-Component Alignment for each.
Recommend top 1 + lý do.
```

→ AI sẽ output 5 hook + recommendation. Pick 1 strongest.

**Optional fast track**: Query hook bank trước

```
Apply hook-swipe-library.
Filter: temperature = [chosen], framework = [Contrarian/Investigator/etc]
Return: 3-5 candidates from 72-hook bank
```

→ Nếu match → remix theo context, skip generate from scratch.

### Step 3: Generate full script (10 phút)

```
Apply kallaway-script-master.

Topic: [same as Step 1]
Hook: [paste hook chọn từ Step 2]
Duration: 60s
Cảm xúc dominant: [bất ngờ / hào hứng / inspired / etc]
CTA type: [theo cta-library decision tree — vd: Educational + Save cho topic pháp lý, Lead-gen cho launch announcement]
Persona: [same as Step 1]

Apply:
- 6 Levels Storytelling (Level 2 Trickster + Level 3 Warrior bắt buộc)
- 4 Blockers fix (Interest research, Hook delegated above, Structure pick 1 of 7, Engagement)
- 6 Story Locks (Naming, Embedded Truths, Thought Articulation, Negative Frames, Loop Openers, Contrast Words)

Output:
- Full 60s script with timestamps
- 3-5 segments breakdown
- Shotlist (visual cue per segment)
- CTA cuối với Educational + Save (or other from cta-library)
- Self-test 3 lần checklist (silent / nhắm mắt / full)
- Audit report 3 frameworks
```

→ AI sẽ output full script ready-to-shoot.

### Step 4: Generate caption (5 phút)

```
Apply content-engine Stage 4.

Generate caption FB/IG accompanying reel above.
Storytelling formula: [pick 1: PAS / BAB / StoryBrand / Hero / 4P / Hot Take]
Length: medium (200-400 từ)
Voice: women-biz-vn niche-pack tone (anh/chị/em, Maria warmth)

Hook in caption: same theme as reel
CTA: same as reel CTA (consistency)
Hashtag: 3 broad + 5 niche + 2 branded

Output: caption ready-to-paste.
```

### Step 5: Self-check + ship (5 phút)

**Pre-shoot checklist** (60 giây):

- [ ] Hook alignment 4-component test (Spoken/Text/Visual/Audio aligned?)
- [ ] Script audit: 6 Levels Storytelling pass ≥4/6?
- [ ] Story Locks pass ≥4/6?
- [ ] CTA NOT default "comment X nhận DM"?
- [ ] Tone "anh/chị/em" consistent?
- [ ] Caption hashtag 10 (3+5+2)?

→ All ✅ = ship. Quay reel + post.

---

## 📊 Productivity gain

| Activity | Without kit | With kit (Workflow B) |
|----------|-------------|---------------------|
| Topic ideation | 30-60 phút | 5 phút |
| Hook brainstorm | 30 phút | 5 phút |
| Script write | 1-2 giờ | 10 phút |
| Caption write | 30 phút | 5 phút |
| Self-check + audit | 0 (skip) | 5 phút |
| **Total** | **3-4 giờ** | **30 phút** |

→ **6-8x faster** với higher quality (built-in audit).

---

## 🎯 Apply Workflow B 5x/week (weekly content batching)

### Sunday batching session (3-4h)

Sit down 1 buổi → output 5 reel scripts cho cả tuần:

| Day of week | Reel topic | CTA type | Goal |
|-------------|-----------|----------|------|
| Mon 9pm | Educational tutorial | Save | Build trust |
| Tue 7am | Hot take controversial | Discussion | Engagement |
| Wed 9pm | Story personal | Reflection | Vulnerability |
| Fri 9pm | Tutorial quick win | Action | Practical |
| Sun 8pm | Lead magnet pitch | Lead-gen | Conversion |

→ **70% non-pitch + 30% engagement/pitch** = đúng quy tắc CTA Library 70/20/10.

### Monday: Quay all 5 reels (3-4h)

Setup phone vertical, natural light, mic, quay 5 reels back-to-back:
- Wear 1 outfit (consistent brand)
- 1 location (cafe, home office, etc)
- 5 takes mỗi reel, pick best
- Edit basic CapCut (cuts + text overlay) ~30 phút mỗi reel

### Mon-Fri: Auto-post via Meta Business / Buffer

Schedule 5 reels theo schedule trên. Engage manually (comment replies, DMs).

→ **Result**: 5 reels/tuần với 3-4h work tổng (chỉ 1 buổi sáng Sunday + 1 buổi quay Monday).

---

## 💡 Pro Tips

### Tip 1: Cache hook bank query
First Workflow B run → query hook-swipe-library lưu 20-30 candidates.
Future runs → reference candidates list, skip query lại.

### Tip 2: Batch theo topic cluster
Thay vì 5 topic random → pick 1 theme cho cả tuần (vd: "Email marketing week"):
- Mon: Reel intro email marketing importance
- Tue: Reel 5 sai lầm subject line
- Wed: Reel story chị Hà email funnel
- Fri: Reel tutorial quick win 9-Word Email
- Sun: Reel pitch lead magnet "5 Welcome Email Templates"

→ Audience absorb theme deep, more engaged.

### Tip 3: Repurpose 1 reel → 3 formats
- Reel video 60s (TikTok/Reels)
- Carousel 5-page (IG)
- Long-form FB post (FB)

→ Triple reach từ same content effort.

### Tip 4: Track which framework wins for your audience
Sau 30 days, review:
- Reel nào reach cao nhất?
- Hook framework nào được dùng?
- Topic group nào audience engage nhất?

→ Double down on winning patterns.

---

## 🆘 Stuck?

| Stuck at | Action |
|----------|--------|
| No topic ideas | Query hook-swipe-library 72 hooks for inspiration |
| Hook generic, weak | Re-run kallaway-hook-master với specific framework (Contrarian/Investigator) |
| Script flat, no tension | Apply 6 Story Locks (especially Loop Openers + Contrast Words) |
| CTA default lead-gen | Check cta-library.md decision tree, pick non-pitch type |
| Caption not flowing | Switch storytelling formula (try BAB instead of PAS) |
| Hashtag generic | Mix broad + niche + branded (don't all generic) |

---

## ⏭ Next workflow

After Workflow B becomes routine (1-2 weeks):
- **Workflow C**: Audit reels not performing → identify framework gaps
- **Workflow D**: Quarterly fb-insight-miner → update niche-pack with fresh verbatim
- **Workflow A**: Build NEW product launch (mid-tier $97 → high $300 → premium cohort)
