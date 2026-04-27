# Stage 1 Prompt — Customer Profile Generation

> Internal prompt the skill loads when running Stage 1. Claude reads this + reference files + data source, then writes `output/{persona_slug}/profile.json` conforming to `schemas/profile.schema.json`.

## Inputs to load (in order)

1. `references/vpc-framework.md` — full content
2. `schemas/profile.schema.json` — full schema
3. `niche-packs/{niche}.json` if exists, else `niche-packs/_universal.json` — priors only, must be verified
4. Data source (one of):
   - **fb_insight_miner output** — markdown report from a prior fb-insight-miner run
   - **brief-form answers** — filled `templates/brief-form.md` from user
   - **hybrid** — both above

## Instructions

You are building a Customer Profile (VPC-based) for a Vietnamese creator/coach. Follow these rules:

### Rule 1 — Verbatim is sacred
- Never paraphrase quotes from the data source. Copy exactly, including typos and slang ("em lú lắm chị" stays "em lú lắm chị").
- Every entry in `voice.verbatim_bank` must be a direct quote, not a summary.

### Rule 2 — Confidence tagging is mandatory
For every job/pain/gain entry, tag `confidence`:
- `observed` — heard the customer say this (have a verbatim quote OR specific source ref)
- `inferred` — derived from behavior pattern (no direct quote, but pattern is clear from data)
- `assumed` — hypothesis from niche pack or general knowledge

**Rule:** if `observed_pct < 60%` overall, set `evidence_summary.ready_for_hook_stage = false` and STOP — tell user to gather more data.

### Rule 3 — No generic pains
Run this filter: "Could this pain apply to a kế toán, developer, AND mẹ bỉm?" If yes, it's too generic. Examples to reject:
- "Không có thời gian"
- "Không biết bắt đầu từ đâu"
- "Sợ thất bại"

Replace with niche-specific phrasing. Use customer voice from `voice.repeated_words`.

### Rule 4 — Niche pack as priors only
If a niche pack matches, use its entries as **starting hypotheses**:
- Mark them `confidence: assumed`
- Verify each against actual data (fb_insight_miner output OR brief)
- Only promote to `inferred` or `observed` when verified

### Rule 5 — Sweet-spot counts
- jobs: 5-7 (mix functional/emotional/social)
- pains: 7-10 (mix obstacle/undesired_outcome/risk; ≥2 with severity_tag=extreme)
- gains: 7-10 (cover all 4 levels: required/expected/desired/unexpected)
- voice.verbatim_bank: 10-15
- voice.repeated_words: ≥5

If data source can't support these counts, ship what you have but lower `ready_for_hook_stage` flag if total < min thresholds.

### Rule 6 — Demographics filter
Only fill demographic fields that affect content. Skip vanity fields (gender if obvious from niche, education level, marital status unless it IS the identity).

## Procedure

1. Load all inputs.
2. Determine `data_source.method`.
3. If fb_insight_miner: extract verbatim quotes from the report's "verbatim quotes" sections + cluster pain/gain candidates from "9 dimensions" + "voice decoding" sections.
4. If brief: parse Q1-Q20 directly into schema fields.
5. If hybrid: scrape-first, brief overrides on conflict (user's stated priority wins).
6. Cross-check against niche pack if any.
7. Apply Rules 1-6.
8. Compute `evidence_summary` stats.
9. Write to `output/{persona_slug}/profile.json`.
10. Run `scripts/validate.py profile output/{persona_slug}/profile.json`.
11. If validation fails, fix and retry. If 3 retries fail, surface error to user.

## Output requirement

Strict JSON conforming to `schemas/profile.schema.json`. No markdown wrapping, no commentary in the JSON.

After writing, print 1-paragraph human-readable summary:
- Persona name + one_line
- Counts (jobs/pains/gains/quotes)
- `observed_pct`
- `ready_for_hook_stage` (true/false)
- If false: WHY + what to do next.