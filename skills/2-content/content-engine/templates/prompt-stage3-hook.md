# Stage 3 Prompt — Hook Library

> Internal prompt for Stage 3. Reads `profile.json` + `insights.json`, generates 50-100 hooks.

## Inputs to load

1. `output/{persona_slug}/profile.json`
2. `output/{persona_slug}/insights.json`
3. `references/storytelling-and-hooks.md` Section 2 (8 hook types) + Section 3 Table B
4. `schemas/hooks.schema.json`

## Instructions

A hook is the first 1-2 lines that decide if reader keeps reading. It's NOT a tagline. It's a **3-second curiosity trigger** using customer's own vocabulary.

### The 8 hook archetypes

| Type | Pattern |
|---|---|
| `curiosity_gap` | Hint điều bất ngờ + giấu twist → buộc đọc tiếp |
| `contradiction` | "Unpopular opinion: [X]" — ngược niềm tin chung |
| `stat_led` | Mở bằng số gây sốc + nguồn (audit của bạn) |
| `question_led` | Câu hỏi trực diện chạm pain/aspiration |
| `story_open` | Cảnh in-medias-res, chưa giải thích bối cảnh |
| `callout` | "Bạn đang [hành vi cụ thể] — và đây là lý do" |
| `list` | "[N] điều/lý do/sai lầm về [X]" |
| `transformation` | "Từ [X] sang [Y] trong [thời gian]" |

### Generation rules

**Rule 1 — Variety per insight:** For each insight, generate **3-6 hook variants spanning ≥3 different hook types**. Don't ship 6 curiosity_gap hooks for the same insight.

**Rule 2 — Voice vocabulary mandate:** Each hook MUST use ≥1 word from `profile.voice.repeated_words` OR `profile.voice.self_labels`. Record the words in `uses_voice_words` field. This is the highest-leverage rule — hooks that sound like the customer's inner voice beat polished hooks every time.

**Rule 3 — Word limit:** ≤25 words. Reels hooks ideally ≤15 words (≤4 seconds reading).

**Rule 4 — Pair with formula:** Use Table A mapping. Each hook has 1 `paired_formula` (v1 active set: pas/bab/storybrand/hero/fourp/hot_take).

**Rule 5 — Goal balance:** Distribute hooks across awareness/lead/sale roughly matching user-requested ratio. Default: 30% awareness / 50% lead / 20% sale.

**Rule 6 — Format target:** Tag which formats each hook works for. Some hooks work everywhere, others are reels-specific (story_open often is) or caption-specific (long contradiction).

**Rule 7 — Reject failure modes:**
- Curiosity-gap hooks that don't deliver in body → "clickbait without payoff"
- Generic list hooks ("5 mẹo content tốt") — already in 200 other posts
- Stat hooks without source ("90% creator fail" with no audit basis)
- Yes/no question hooks — reader answers in head, scrolls

## Procedure

1. Load inputs.
2. For each insight in `insights.json`:
   a. Pick 3-6 hook types compatible with insight.type (use Section 2 "Pairs với insight" hints).
   b. For each, draft a hook using the insight's `statement_vi` + `reframe_angle` + `hidden_cost`.
   c. Inject ≥1 voice word.
   d. Set `paired_formula` from insight.recommended_formulas (or override if a different formula better fits the hook).
   e. Set `goal` matching insight.applicable_goals.
3. Aim for total 50-100 hooks (3-6 × 10-25 insights ≈ 30-150, target middle).
4. Write `output/{persona_slug}/hooks.json`.
5. Validate.

## Output requirement

Strict JSON. After writing, print summary:
- Total count
- Distribution by hook_type (warn if any type is 0)
- Distribution by paired_formula
- Distribution by goal
- Avg word count
- % hooks that pass voice-vocabulary rule (target 100%)