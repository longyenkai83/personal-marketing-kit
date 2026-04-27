---
name: kallaway-hook-master
description: Viết hook video ngắn (TikTok/Reels/Shorts) + caption FB/IG theo phương pháp Kallaway — 6 Hook Frameworks (Fortune Teller/Experimenter/Teacher/Magician/Investigator/Contrarian) × 5 Dream Outcome Formats (About Me/If I/To You/Can You/He-She Just Did) × 4 Component Alignment (Spoken+Text+Visual+Audio). Use when user wants to write hook for short-form video, viết hook video, viết caption mở đầu, brainstorm hook viral, audit hook cũ, hoặc apply Kallaway framework. Vietnamese-first. Triggers — "viết hook", "hook kallaway", "kịch bản reels", "hook viral", "audit hook video".
allowed-tools: Read, Grep, Glob
argument-hint: "[topic] [framework?] [temperature?]"
---

# Kallaway Hook Master

Phương pháp viết hook video ngắn theo Kallaway — đã proven cho thị trường VN qua dự án "Phụ Nữ Đóng Gói Chuyên Môn Bán Internet".

## When to invoke

VN trigger phrases:
- "viết hook cho video / reel / short / tiktok"
- "hook kallaway"
- "viết hook viral"
- "brainstorm hook"
- "audit hook video cũ"
- "kịch bản 5 giây đầu"

User can also invoke `/kallaway-hook-master` directly.

**Do NOT use for:**
- Caption dài không có video (dùng `content-engine`)
- Email subject line (dùng `email-marketing-writer` khi có)
- Sales letter (dùng `digital-product-launch` khi có)

## Required inputs (ask user if missing)

Hỏi 1 lần gộp các câu sau:

1. **Topic** — chủ đề hook (vd: "đóng gói chuyên môn bán online")
2. **Goal** — `awareness` / `lead` / `sale` / `brand` (default: `lead`)
3. **Market temperature** — chọn 1:
   - `lanh` (lạnh — thị trường chưa biết đến anh) → ưu tiên Contrarian/Investigator
   - `am` (ấm — đã follow nhưng chưa tin) → ưu tiên Teacher/Experimenter
   - `nong` (nóng — đã engage, chuẩn bị mua) → ưu tiên Fortune Teller/Case Study
   - `banhang` (bán hàng — sẵn sàng convert) → Direct Offer
4. **Format** — `video_30s` / `video_60s` / `caption_only` / `multi`
5. **Hero Visual có sẵn?** — yes/no + mô tả ngắn nếu có
6. **Number of variants** — default 5 (đủ để A/B test)
7. **Persona/audience** — đối tượng mục tiêu (default load từ niche-pack nếu có)

## Methodology — 5-step Kallaway Framework

### Step 0: Hero Visual First (nếu có footage sẵn)
- Bắt đầu từ visual mạnh nhất → viết spoken hook MATCH với visual
- Nguyên lý: mắt xử lý nhanh hơn tai 10-100x → visual quyết định attention

### Step 1: Spoken Hook
Chọn 1 trong **6 Hook Frameworks** (chi tiết: `references/6-hook-frameworks.md`):
| # | Framework | Format gốc | Khi dùng |
|---|-----------|-----------|----------|
| 1 | Fortune Teller 🔮 | "[X] này sẽ thay đổi cách bạn [Y]" | Future contrast |
| 2 | Experimenter 🧪 | "Tôi vừa thử [X] — đây là kết quả" | Demo/POV |
| 3 | Teacher 📚 | "Tôi từng [sai], giờ tôi dạy [đúng]" | Bài học rút ra |
| 4 | Magician ⚡ | Pattern interrupt + 1 framework khác | Combo wildcard |
| 5 | Investigator 🔍 | "Có 1 thứ ít người biết — đây là..." | Bí mật/insight |
| 6 | Contrarian ⚔️ | "Mọi người nghĩ X — thực ra Y" | Phá niềm tin sai |

HOẶC chọn 1 trong **5 Dream Outcome Formats** (chi tiết: `references/5-dream-outcome-formats.md`):
| # | Format | Template | Mạnh nhất khi |
|---|--------|----------|---------------|
| 1 | About Me | "Tôi vừa [kết quả] bằng cách [Y]" | Có case study thật |
| 2 | If I | "Nếu tôi muốn [kết quả], tôi sẽ làm [Y] từ ngày 1" | Chia sẻ chiến lược |
| 3 | To You | "Nếu bạn muốn [kết quả], hãy [Y]" | Thị trường lạnh |
| 4 | Can You | "Có thể bạn [kết quả] trong [hoàn cảnh]?" | Phá rào cản niềm tin |
| 5 | He/She Just Did | "[Nhân vật] vừa [kết quả] bằng [Y]" | Có testimonial |

→ Tổng 11 framework. AI tự chọn theo `temperature` hoặc user chỉ định.

### Step 2: Visual Hook
Đề xuất visual để MATCH với spoken hook:
- B-roll quay bằng điện thoại
- Hình ảnh từ internet (specific, không generic)
- A-roll: creator nói thẳng vào camera (thêm movement)

### Step 3: Text Hook (overlay trên video)
- Ngắn nhất có thể (≤7 từ ưu tiên)
- Tạo contrast hoặc emotional trigger
- Đặt gần mắt creator (nếu creator on screen)
- **Text được xử lý trước voice** vì mắt đọc nhanh hơn tai

### Step 4: Quay video

### Step 5: Self-Test 3 lần (chi tiết: `references/4-component-alignment.md`)
- **Im lặng** (visual + text only): rõ topic & curiosity chưa?
- **Nhắm mắt** (audio only): rõ topic & curiosity chưa?
- **Đầy đủ**: 4 thành phần (Spoken + Text + Visual + Audio) aligned chưa?

KPI: 5-second retention >50% = tốt | >70% = xuất sắc

## Hook Rules (cứng)

Mỗi hook MUST:
- ≤25 từ (caption mở đầu) hoặc ≤2-4 câu (script video)
- Có **Curiosity Loop** = contrast giữa expectation vs reality (gap càng lớn càng mạnh)
- Specificity (con số/tên cụ thể) > Generic
- Dùng "bạn/em/chị" thay "tôi/mình" (Relatability)
- Không bắt đầu bằng "Hôm nay" / "Mình muốn chia sẻ" / "Xin chào"
- Hook ở dòng 1 / 3 giây đầu video

## Output Format

```markdown
## Hook Set — [Topic]

**Persona target**: [tên persona]
**Temperature**: [lanh/am/nong/banhang]
**Goal**: [awareness/lead/sale]

### Hook 1 — [Framework name]
**Spoken**: "[hook script 2-4 câu]"
**Text overlay**: "[≤7 từ]"
**Hero Visual**: [mô tả visual cần quay/tìm]
**Audio**: [SFX/nhạc gợi ý]
**Alignment check**:
- ✅ Visual ↔ Spoken
- ✅ Text ↔ curiosity
- ✅ Audio ↔ tone
**Use when**: [tình huống đăng phù hợp]
**CTA**: [comment X / nhắn Y / link bio]

### Hook 2 — [Framework name]
... (lặp 5 variants)

## A/B Test Recommendation
Đăng 2 hook khác framework cùng tuần (cách nhau 2-3 ngày).
So sánh: Reach / Comment / Save / Inbox
→ Nhân đôi format thắng trong tháng tiếp theo.
```

## Integration

- **Auto-call hook bank**: Đọc `hook-swipe-library/banks/women-biz-vn-72.json` (nếu user thuộc niche này) → có 72 hook proven sẵn để remix thay vì viết từ 0
- **Chained skill** (sau khi có hook):
  - **`kallaway-script-master`** ⭐ — gen full kịch bản 60s+ với 6 Levels Storytelling + 4 Blockers + 6 Story Locks. Hook này feed vào Step 3 của script-master.
  - **`content-engine`** Stage 4 — gen full caption FB/IG + body text đi kèm hook
  - **`hook-swipe-library`** — query bank để có thêm variants tương tự

## Reference Files

- `references/6-hook-frameworks.md` — 6 framework chính + ví dụ
- `references/5-dream-outcome-formats.md` — 5 format Dream Outcome (Bài Tập 12)
- `references/4-component-alignment.md` — Spoken + Text + Visual + Audio alignment
- `templates/hook-writing-worksheet.md` — worksheet 5-step để viết 1 hook hoàn chỉnh

**Shared reference (từ kallaway-script-master)**:
- `~/.claude/skills/kallaway-script-master/references/cta-library.md` — **9 loại CTA** (Educational/Reflection/Save/Share/Discussion/Action/Lead-gen/Follow/No CTA). Khi hook đi kèm caption hoặc full reel có CTA cuối, READ file này để chọn CTA phù hợp topic, KHÔNG mặc định "comment X nhận DM Y".

## Quality Standards

- ❌ Không bịa số liệu/testimonial → dùng `[testimonial_X_placeholder]`
- ❌ Không paraphrase verbatim quote khách (giữ nguyên typo)
- ❌ Không dịch thẳng hook EN → VN (mất nuance) — phải remix theo voice VN
- ✅ Mỗi hook chỉ 1 framework rõ (không trộn lung tung)
- ✅ Mỗi hook có CTA đo được (comment X, nhắn Y, không "tham khảo nhé")

## Failure modes

- **Hook generic, đụng đám đông** → load thêm verbatim từ `voice.repeated_words` của persona, force ≥1 từ vocab khách vào hook
- **Hook quá dài** → cắt còn ≤25 từ, ưu tiên Specificity > tính từ
- **Visual không có sẵn** → đề xuất: (a) quay A-roll talking head + text overlay mạnh, hoặc (b) đổi sang Investigator/Contrarian (text-heavy frameworks)
- **Audience reject** (reach thấp) → check Alignment 4 thành phần, có thể spoken/visual/text không match nhau

## Status

**v1.0** — built từ Kallaway materials (Hooks Workshop + 100 Viral Hooks + Bài Tập 12 Dream Outcome + Bài Tập 9 18-topic). Niche default: phụ nữ KD VN. Mở rộng niche khác qua thêm bank vào `hook-swipe-library/banks/`.
