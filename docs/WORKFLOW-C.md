# Workflow C — Audit Existing Script (15 phút)

> **Goal**: Improve reel/video script đã có theo Kallaway frameworks
> 
> **Best for**: Reels post nhưng retention thấp / không viral

---

## 🎯 Outcome target

Sau 15 phút:
- ✅ Audit script cũ theo 3 frameworks (6 Levels + 4 Blockers + 6 Story Locks)
- ✅ Identify gap nào (framework nào fail)
- ✅ Revised script applied fixes
- ✅ Specific changes documented (before vs after)

---

## ⚡ 3-Step Process

### Step 1: Paste script cũ (2 phút)

Open Claude Code → gõ:

```
Apply kallaway-script-master in AUDIT mode.

Script cũ của em:

[PASTE script video — toàn bộ lời thoại 60s]

Context:
- Topic: [chủ đề]
- Audience: [persona]
- Posted ngày: [date]
- Metrics: [retention %, comments, saves nếu có]

Audit theo 3 frameworks:
1. 6 Levels Storytelling — Pass/Fail per level
2. 4 Blockers — Identify which blocker đang chặn (Interest/Hook/Structure/Engagement)
3. 6 Story Locks — Pass/Fail per lock

Identify weakest 2-3 areas + suggest fix.
```

### Step 2: Review audit report (5 phút)

AI sẽ output report như sau:

```markdown
## AUDIT REPORT

### 6 Levels Storytelling
- ✅ Level 1 (Reporter avoid): PASS
- ⚠️ Level 2 (Trickster): PARTIAL — chỉ 1 misdirection ở 0:30, thiếu mid-script
- ✅ Level 3 (Warrior): PASS — pain point opened ở hook
- ❌ Level 4 (Architect): FAIL — không có segments rõ
- ⚠️ Level 5 (Translator): PARTIAL — 1 analogy "X" nhưng còn 2 câu confusing
- ⏳ Level 6 (Artist): N/A (signature optional)

→ Weakest: Level 4 (Architect) + Level 2 (Trickster mid-script)

### 4 Blockers
- ✅ Interest: PASS — fact mạnh ở hook
- ✅ Hook: PASS — Contrarian framework
- ❌ Structure: FAIL — flow lộn xộn, không có Story Navigation
- ⚠️ Engagement: PARTIAL — emotion dominant unclear

→ Critical: Structure Blocker

### 6 Story Locks
- ✅ Naming: PASS — concept "X System" có name
- ❌ Embedded Truths: FAIL — dùng 4 lần "có thể / có lẽ"
- ❌ Thought Articulation: FAIL — không có "Em đang nghĩ X"
- ⚠️ Negative Frames: 1 dùng nhưng yếu
- ❌ Loop Openers: FAIL — chỉ 1 transition "tiếp theo" nhạt
- ✅ Contrast Words: PASS — dùng "nhưng" 3 lần

→ Score: 2/6 PASS — cần fix 4 locks

## OVERALL
6 Levels: 2/6 PASS (target ≥4/6)
4 Blockers: 2/4 PASS
Story Locks: 2/6 PASS (target ≥4/6)

→ Script cần significant revision. Estimated impact: 40-60% retention boost với fixes.
```

### Step 3: Get revised script (8 phút)

Gõ tiếp:

```
Apply fixes cho script cũ:
1. Add Level 4 Architect: chia 3 segments rõ với 4-block (Chuyện gì? Tại sao? Ví dụ? Action?)
2. Add 2 misdirection mid-script (Level 2 Trickster)
3. Replace 4x "có thể / có lẽ" với "khi / lý do tại sao / thực ra" (Embedded Truths)
4. Add 1-2 "Em đang nghĩ X..." sau big claims (Thought Articulation)
5. Replace "tiếp theo" với "NHƯNG đây mới là điều shock thật sự" (Loop Openers)
6. Strengthen 1 Negative Frame

Output: revised script + before-after comparison + reasoning từng change.
```

→ AI sẽ output:
- Revised script ready-to-shoot
- Comparison table (before vs after)
- Reasoning per change

---

## 📊 Audit báo cáo template

Save audit reports trong file `audit-history.md` để track improvement:

```markdown
## Audit Log

### Reel "Topic X" — Date 2026-04-27

| Framework | Score Before | Score After | Notes |
|-----------|--------------|-------------|-------|
| 6 Levels | 2/6 | 5/6 | Added Architect + 2nd Trickster |
| 4 Blockers | 2/4 | 4/4 | Fixed Structure |
| 6 Story Locks | 2/6 | 5/6 | Embedded Truths + Loop Openers + Articulation |

### Result after re-shoot
- Retention 5s: 45% → 72% (+60%)
- Average view duration: 28s → 47s (+68%)
- Comments: 12 → 38 (+217%)
- Saves: 5 → 24 (+380%)
```

---

## 🎯 Common Audit Findings

### Finding 1: "Hook strong nhưng drop ở 15s"
**Diagnosis**: Level 2 Trickster only 1 hook ở opening, không có misdirection mid-script
**Fix**: Add Loop Openers mỗi 30-60s + 1-2 mini-hooks giữa script

### Finding 2: "Audience confused cuối video"
**Diagnosis**: Level 5 Translator weak — quá nhiều jargon / không có analogy
**Fix**: Audit từng câu — replace abstract terms với analogy/visual aid

### Finding 3: "Reel post 'OK but boring'"
**Diagnosis**: Stuck Level 1-2 (Reporter + light Trickster), thiếu Level 3 Warrior
**Fix**: Open script với pain point cụ thể của persona, cho audience reason to root

### Finding 4: "Comments confused về CTA"
**Diagnosis**: CTA mặc định "comment X nhận DM" cho topic không phù hợp
**Fix**: Apply CTA Library decision tree — chọn Educational/Save/Discussion theo topic type

### Finding 5: "Tone không match brand"
**Diagnosis**: Story Locks (especially Embedded Truths) yếu — quá do dự
**Fix**: Replace "có thể / có lẽ" → "khi / lý do tại sao" — sound chắc chắn = authority

### Finding 6: "Reel nào cũng pattern giống"
**Diagnosis**: Single hook framework dominant (vd: chỉ Teacher framework)
**Fix**: A/B test 11 frameworks — diversify Hook + Dream Outcome formats

---

## 🔄 Quarterly Audit Routine

Mỗi 3 tháng, audit 5-10 reel performing thấp nhất:

1. List 5-10 reels low-performing (low retention, low engagement)
2. Apply Workflow C cho mỗi reel
3. Identify pattern weak (vd: "Tất cả miss Story Locks 4 Negative Frames")
4. Update writing process: ensure framework đó luôn applied
5. Future reels: built-in fixed pattern → less low-performing reels

→ **Result**: Average reel quality grow theo time, không stuck plateau.

---

## 💡 Pro Tips

### Tip 1: Audit BEFORE shooting (best ROI)
Workflow B Step 5 self-check = light audit trước quay.
Workflow C = deep audit AFTER post (when have data).

### Tip 2: Compare top 10% vs bottom 10%
Audit 5 reel TOP performing + 5 reel BOTTOM performing.
Compare: pattern nào TOP có mà BOTTOM thiếu?
→ Identify YOUR signature winning formula.

### Tip 3: Don't over-fix
Audit có thể identify 8-10 issues — KHÔNG fix tất cả.
Pick top 2-3 critical issues mỗi reel revise.
Iterate: fix → measure → fix more.

### Tip 4: Audit cũng cho captions
Workflow C work cho FB/IG captions cũ:
- Apply content-engine audit logic
- Check formula structure (PAS/BAB/etc)
- Check hook line + CTA

---

## 🆘 Stuck?

| Issue | Action |
|-------|--------|
| AI audit too generic | Provide more context: persona + metrics + topic |
| Audit identify too many issues | Focus top 2-3 critical, ignore minor |
| Revised script lose original voice | Re-run với "preserve voice [creator name]" instruction |
| Don't agree with audit | Ask "Why is [Level X] failing? Show me specific lines" |

---

## ⏭ After Workflow C

- Iterate revised script — re-shoot when convenient
- Document audit pattern → update writing process
- Move to Workflow B (write new reel với pattern strong)
- Quarterly: Workflow D (research) để update niche-pack
