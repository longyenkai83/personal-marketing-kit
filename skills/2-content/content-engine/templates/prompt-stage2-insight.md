# Stage 2 Prompt — Insight Mining

> Internal prompt the skill loads when running Stage 2. Reads `profile.json`, generates `insights.json` (10-25 insights).

## Inputs to load

1. `output/{persona_slug}/profile.json` — full content
2. `references/vpc-framework.md` Section 2.1 (field-to-asset mapping)
3. `references/storytelling-and-hooks.md` Section 3 (mapping tables — Insight type → Formula)
4. `schemas/insights.schema.json` — full schema

## Stage gate (HARD)

Before processing, check `profile.evidence_summary.ready_for_hook_stage`. If `false`, **STOP** with message:

> "Profile chưa đạt observed_pct ≥ 60%. Quay lại Stage 1 — chạy fb-insight-miner depth=deep hoặc bổ sung brief Q19 verbatim quotes. Stage 2 không chạy với profile thiếu evidence vì sẽ đẻ ra insight giả."

Override allowed ONLY if user explicitly says "skip gate, I accept lower quality."

## Instructions

You are generating customer insights for IG content. An insight is NOT a raw pain — it's a **reframing** that creates a useful angle for content.

### The 8 insight archetypes

| Type | Definition | Example (creator/coach niche) |
|---|---|---|
| `tension` | Customer feels pulled between 2 things they want | "Họ muốn đăng đều VÀ muốn có POV — nhưng đăng đều ép họ ăn theo trend" |
| `contradiction` | What they say vs. what data shows is true | "Khách bảo 'thiếu thời gian' nhưng thực ra dành 3h/ngày scroll IG" |
| `say_vs_do` | Stated intention vs. actual behavior | "Lưu carousel 'tips content' nhưng không bao giờ áp dụng" |
| `surprise_myth_bust` | Common belief that's wrong | "Đăng đều không quan trọng bằng đăng đúng 1 chủ đề" |
| `aspiration` | Identity/state they secretly want | "Muốn được nhìn như chuyên gia, không phải 'đứa làm content'" |
| `objection` | Reason they don't act despite wanting to | "Sợ học viên không có kết quả thì khoá mất uy tín" |
| `transformation` | Realistic before→after they could achieve | "Từ 1 bài/tuần kiệt sức → 4 bài/tuần dùng 3h" |
| `identity_shift` | Who they need to BECOME for offer to work | "Phải nhận mình là 'guide' không phải 'người đang học'" |

### Generation rules

**Rule 1 — Coverage:** Try to cover at least 5 of 8 archetypes. Don't over-index on `tension` or `objection`.

**Rule 2 — Source citation (mandatory):** Every insight MUST cite ≥1 verbatim quote from `profile.voice.verbatim_bank`. The quote grounds the insight in real customer voice.

**Rule 3 — Novelty scoring (1-5):**
- 5 = Original POV, would surprise even niche peers ("90% coach đang dùng 5 bước trong caption đều giết engagement")
- 4 = Sharp, specific reframe of common knowledge
- 3 = True but somewhat known
- 2 = Generic — appears in 100+ other posts
- 1 = Cliché ("hãy là chính bạn")

Drop any insight with novelty_score ≤ 2 unless it's the only insight in that archetype.

**Rule 4 — Hidden cost (for tension/objection insights):** Fill `hidden_cost` field with concrete cost of NOT solving — time, money, identity, opportunity.

**Rule 5 — Reframe angle:** For contradiction/surprise insights, fill `reframe_angle` with the new POV that flips the narrative. This is fuel for Hot Take and PAS Solution slot.

**Rule 6 — Auto-suggest formulas:** Use Table A from `storytelling-and-hooks.md` Section 3 to fill `recommended_formulas`. Only use v1 active set: `pas, bab, storybrand, hero, fourp, hot_take`.

**Rule 7 — Goal tagging:** Each insight tagged with `applicable_goals` (1-3 of awareness/lead/sale).

## Procedure

1. Load profile + references + schema.
2. Check stage gate.
3. For each of 8 archetypes, scan profile.pains, profile.gains, profile.jobs, profile.voice for fuel. Generate 1-3 candidate insights per archetype.
4. Score each candidate. Drop ≤2 unless last in archetype.
5. For surviving insights, fill hidden_cost / reframe_angle as applicable.
6. Auto-suggest formulas + goals via mapping tables.
7. Output 10-25 total insights.
8. Write `output/{persona_slug}/insights.json`.
9. Validate via `scripts/validate.py insights ...`.

## Output requirement

Strict JSON. After writing, print summary:
- Total count + archetype distribution
- Top 3 highest-novelty insights (title only)
- Any archetype with 0 insights (warn user)