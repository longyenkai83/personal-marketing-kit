# Stage 4 Prompt — Content Generation

> Internal prompt for Stage 4. Reads profile + insights + hooks, fills formula beat slots, produces N posts.

## Inputs to load

1. `output/{persona_slug}/profile.json`
2. `output/{persona_slug}/insights.json`
3. `output/{persona_slug}/hooks.json`
4. `references/storytelling-and-hooks.md` Section 1 (formula specs) + Section 4 (formula_spec.json template)
5. `schemas/content.schema.json`
6. User inputs: `format` (ig_caption/reels_30s/reels_60s/fb_post/multi), `n_posts` (default 12), `cta` (offer + keyword + link)

## Quality mode branching

- `economy`: Sonnet 4.6 single pass. No editorial revision.
- `pro`: Sonnet 4.6 first pass → Opus 4.7 editorial pass per post.

## Instructions

### Pick selection (Rule 1 — Goal mix)

If user requested `n_posts = 12` and goal balance not specified, default:
- 3 awareness posts (Hot Take, Hero formula)
- 6 lead posts (PAS, BAB, StoryBrand)
- 3 sale posts (4P, BAB)

For each "slot," pick a hook from `hooks.json` matching the goal + a unique `paired_insight_id` (no insight repeated within batch).

### Beat filling (Rule 2 — Formula adherence)

For each post:
1. Identify `paired_formula` from chosen hook.
2. Load formula spec from `references/storytelling-and-hooks.md` Section 1.
3. For each beat slot, fill from designated source:

**PAS beats:**
- `problem` ← insight.statement_vi (paraphrased into customer voice)
- `agitate` ← insight.hidden_cost (twist: cost/shame/future regret)
- `solution` ← profile-derived method/POV + cta.offer (1 sentence reframe)
- `cta` ← cta.text

**BAB beats:**
- `before` ← profile.pains (extreme severity, with verbatim feel)
- `after` ← profile.gains (required level, with measurable outcome if available)
- `bridge` ← user's method/process (numbered if possible)
- `cta` ← cta.text

**StoryBrand beats:**
- `hero_problem` ← profile.pains (target the reader using "Bạn là...")
- `guide_meets` ← user-as-guide + their plan
- `plan` ← 3 numbered steps
- `stakes` ← what happens if they don't act (success vs failure)
- `cta` ← cta.text

**Hero's Journey beats:**
- `ordinary_world` ← user's pre-shift state
- `call` ← inciting incident + refusal
- `threshold` ← decision moment
- `trial` ← struggle + insight discovered
- `return` ← who they are now + invitation
- `cta` ← cta.text

**4P beats:**
- `picture` ← future scene (use profile.gains.unexpected for vivid hook)
- `promise` ← cta.offer specific deliverables
- `proof` ← real numbers/testimonials (use placeholders if absent)
- `push` ← urgency + scarcity (real, not fake)
- `cta` ← cta.text

**Hot Take beats:**
- Beat 1 (use `body` label) — Tuyên bố ngược dòng
- Beat 2 — "Mọi người tin sai vì..."
- Beat 3 — "Đây là lý do thật" (proof from user observation)
- Beat 4 — Hệ quả thực tế (what to do differently)
- `cta` ← cta.text (soft, often "Đồng ý không? Cmt bên dưới")

### Word count enforcement (Rule 3)

| Format | Target words | Hard max |
|---|---|---|
| `ig_caption` | per formula spec (180-320) | 400 |
| `reels_30s` | 70-90 | 100 |
| `reels_60s` | 140-180 | 200 |
| `fb_post` | 200-400 | 600 |

Reels: also fill `body.beats[].duration_sec` so total ≤ format limit (30s = ~80 words spoken).

### Voice vocabulary (Rule 4 — HARD GATE)

Every post body MUST contain ≥2 words from `profile.voice.repeated_words` OR `profile.voice.self_labels`. Validate after generation. If fail, regenerate with explicit instruction.

### CTA injection (Rule 5)

Every post ends with CTA from user input. Don't invent new offers. Format:
- Caption: 1-2 lines + cmt keyword OR link bio
- Reels: ≤10 words, single line

### Hashtags (Rule 6)

Generate 10-12 hashtags per IG post:
- 3 broad (e.g., #personalbranding, #coach)
- 5 niche-specific (use profile.niche + voice words)
- 2 branded (user's own)
- 0-2 trending (only if relevant; don't force)

### No-fabrication rules (Rule 7)

- No fake statistics. If you don't have a real audit number, write qualitatively ("phần lớn coach mình review", not "73% coach...").
- No fake testimonials. Use `[testimonial_X_placeholder]` if needed.
- No fake screenshots/results.

## Editorial pass (pro mode only)

For each post, run Opus 4.7 editorial check:
- [ ] Hook within first line (≤25 words)?
- [ ] ≥2 voice words present?
- [ ] CTA aligns with user-provided offer?
- [ ] Word count in range?
- [ ] No fabricated stats/testimonials?
- [ ] Beat structure matches formula spec?
- [ ] Tone consistent with persona's life_stage + identity?

Fix issues in-place. Re-validate.

## Procedure

1. Load all inputs.
2. Pick N hooks per goal-mix rule.
3. For each pick, fill formula beats per Rule 2.
4. Apply Rules 3-7.
5. If `quality_mode = pro`: run editorial pass.
6. Compute `character_count`, `word_count`, `constraints_passed` per post.
7. Write `output/{persona_slug}/content.json`.
8. Validate.
9. Run `scripts/render_post.py output/{persona_slug}/content.json` to render `posts/*.md` for human review.

## Output requirement

Strict JSON. After writing, print summary:
- Posts generated by formula (3 PAS / 2 BAB / ...)
- Posts by goal (3 awareness / 6 lead / 3 sale)
- Avg word count by format
- % posts passing all `constraints_passed` checks (target 100%)
- Path to rendered markdown previews