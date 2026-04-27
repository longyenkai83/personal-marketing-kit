---
name: content-engine
description: Commercial 4-stage pipeline that turns a customer profile into IG captions + Reels scripts. Stages — (1) Customer Profile via VPC framework, (2) Insight mining, (3) Hook library, (4) Content generation using 6 storytelling formulas (PAS/BAB/StoryBrand/Hero/4P/Hot Take). Vietnamese-first. Each stage outputs JSON artifact that buyer can edit between stages. Use when user wants to build a customer profile + generate content from it, build a content factory, or productize content workflow. Triggers — "lập hồ sơ khách hàng + viết content", "content engine", "viết content theo VPC", "bộ máy content", "factory content", "build customer profile to content".
---

# Content Engine — VPC × Storytelling Pipeline

Commercial pipeline để biến hồ sơ khách hàng (Value Proposition Canvas) thành post IG/Reels chất lượng. 4 stage độc lập — buyer có thể chạy full pipeline hoặc dừng/edit/rerun từng stage.

## When to invoke

VN trigger phrases:
- "lập hồ sơ khách hàng + viết content"
- "content engine"
- "build factory content"
- "viết content theo VPC"
- "tạo content từ insight khách hàng"

User can also invoke `/content-engine` directly.

**Do NOT use for:**
- Long-form blog/SEO articles (use other skill)
- Lead magnet ebooks (use `lead-magnet-factory`)
- Pure customer research without content output (use `fb-insight-miner` standalone)
- Non-Vietnamese content (skill is VN-only in v1)

## Required inputs (ask user if missing)

Ask in 1 consolidated question. Required:
1. **Persona/niche** — e.g., "beauty creator chuyển từ affiliate sang course"
2. **Data source** — chọn 1:
   - `fanpage_url` (FB fanpage public để scrape qua fb-insight-miner)
   - `brief` (điền form `templates/brief-form.md`)
   - `hybrid` (cả 2)
3. **Content goal trọng tâm** — `awareness` / `lead` / `sale` (có thể đa mục tiêu, default `lead`)
4. **Output format** — `ig_caption` / `reels_30s` / `reels_60s` / `fb_post` / `multi`
5. **Số bài cần generate** — default 12 (mix formula)
6. **CTA chính** — sản phẩm/offer skill sẽ điều hướng tới (ví dụ: "khoá Content POV 4 tuần — link bio")
7. **Brand voice notes** (optional) — tone, từ cấm, signature phrases
8. **Quality mode** — `economy` (default) hoặc `pro`:
   - `economy`: Sonnet 4.6 mọi stage, không có editorial pass. ~$0.80/run. Đủ chất lượng cho daily content.
   - `pro`: Sonnet 4.6 stage 1-3, Opus 4.7 stage 4 + editorial pass. ~$2.50/run. Dùng cho launch/sale post quan trọng.

## 4-stage workflow

Use TodoWrite to track each stage visibly.

### Stage 1 — Customer Profile (VPC)

**Goal:** sản xuất `output/{persona_slug}/profile.json` đạt schema `schemas/profile.schema.json`.

**Read first:** `references/vpc-framework.md`.

**Branching by data_source:**

- **fanpage_url** → invoke `fb-insight-miner` skill on the URL. After it produces an insight report, map:
  - Pain points → `pains[]`
  - Voice-of-customer phrases → `voice.verbatim_bank` + `voice.repeated_words`
  - Persona summary → `demographics`
  - Aspirations from comments → `gains[]`
  - "What they're trying to do" → `jobs[]`
- **brief** → load `templates/brief-form.md`, present to user, parse answers into the same fields.
- **hybrid** → run both; cross-reference; flag any field where brief contradicts scraped data.

**Quality gates** (from `references/vpc-framework.md` Section 3):
- jobs ≥ 3, pains ≥ 5, gains ≥ 5, verbatim_bank ≥ 5
- `evidence_summary.observed_pct ≥ 60` → set `ready_for_hook_stage = true`
- If gates fail → tell user explicitly, suggest re-running fb-insight-miner with deeper depth, OR ask user to fill brief gaps.

**Niche pack assist:** if user's niche matches a file in `niche-packs/` (e.g., `beauty-creator.json`), seed the profile with priors then verify each prior against actual data — never silently ship priors as observed.

Write `output/{persona_slug}/profile.json` and validate with `scripts/validate.py profile`.

### Stage 2 — Insight Mining

**Goal:** sản xuất `output/{persona_slug}/insights.json` (10-25 insight) đạt schema `schemas/insights.schema.json`.

**Read first:** `references/vpc-framework.md` Section 2.1 (field-to-asset mapping) + `references/storytelling-and-hooks.md` Section 3 (mapping tables).

**Procedure:**
1. Load `profile.json` into context.
2. For each of 8 insight types (tension / contradiction / say_vs_do / surprise_myth_bust / aspiration / objection / transformation / identity_shift), generate 1-3 candidate insights by combining pains/gains/voice. Insight = reframing, not raw pain.
3. Score each by `novelty_score` (1-5). Drop anything ≤ 2 unless it's the only insight in that category.
4. For each insight: cite ≥1 verbatim quote from `profile.voice.verbatim_bank`.
5. Auto-suggest `recommended_formulas` using Table A from storytelling-and-hooks.md.
6. Tag `applicable_goals`.

Write to `output/{persona_slug}/insights.json` and validate.

### Stage 3 — Hook Library

**Goal:** sản xuất `output/{persona_slug}/hooks.json` (50-100 hooks) đạt schema `schemas/hooks.schema.json`.

**Read first:** `references/storytelling-and-hooks.md` Section 2 (8 hook frameworks).

**🆕 Hook bank integration (added v1.1):**
- **Trước khi generate**, check niche của user → nếu match một bank trong `~/.claude/skills/hook-swipe-library/banks/`, load hooks từ bank làm seed:
  - `women-biz-vn` niche → load `women-biz-vn-72.json` (72 hook proven theo Kallaway 18-topic × 4-temperature)
  - Future banks: thêm vào `hook-swipe-library/banks/` khi có
- **Tỷ lệ trộn**: 30-50% hook từ bank (đã proven, chỉ cần remix theo voice persona) + 50-70% generated mới (theo profile.voice cụ thể)
- **Lý do**: bank = baseline an toàn; generated = customize sâu cho persona cụ thể.

**🆕 Methodology integration (added v1.1):**
Khi generate hook mới, follow `~/.claude/skills/kallaway-hook-master/` framework:
- **6 Hook Frameworks** (`references/6-hook-frameworks.md`): Fortune Teller / Experimenter / Teacher / Magician / Investigator / Contrarian
- **5 Dream Outcome Formats** (`references/5-dream-outcome-formats.md`): About Me / If I / To You / Can You / He-She Just Did
- **4-Component Alignment** (`references/4-component-alignment.md`): Spoken + Text + Visual + Audio cho format video

→ Mỗi hook output có thêm field `kallaway_framework` (1 trong 11 framework) và `temperature` (lanh/am/nong/banhang) để A/B test có hệ thống.

**Procedure:**
1. Load `profile.json` + `insights.json`.
2. **(NEW)** Check `hook-swipe-library/banks/` for matching niche → load seed hooks.
3. For each insight, generate 3-6 hook variants spanning ≥3 different hook types (curiosity_gap / contradiction / stat_led / question_led / story_open / callout / list / transformation) **HOẶC** dùng 1 trong 11 Kallaway frameworks (recommend cho video format).
4. Each hook MUST:
   - Use ≥1 word from `profile.voice.repeated_words` (record in `uses_voice_words`)
   - Be ≤25 words
   - Reference its `paired_insight_id`
   - Have a `paired_formula` (use Table A mapping)
   - Have a `goal`
   - **(NEW for video format)** Have `kallaway_framework` + `temperature` tags
5. Spread `goal` distribution across awareness/lead/sale roughly matching user's stated `content_goal`.
6. **(NEW)** Spread `temperature` distribution: ~30% lanh, ~30% am, ~30% nong, ~10% banhang (adjust theo content_goal).

Write + validate.

### Stage 4 — Content Generation

**Goal:** sản xuất `output/{persona_slug}/content.json` (N posts) đạt schema `schemas/content.schema.json`.

**Read first:** `references/storytelling-and-hooks.md` Section 1 (formula specs + word counts).

**Procedure:**
1. Load `profile.json` + `insights.json` + `hooks.json`.
2. Pick N hooks balanced across formulas + goals (default 12 posts: 3 awareness / 5 lead / 4 sale; varied formulas).
3. For each pick, fill the formula's beat slots using:
   - **Hook** → from `hooks.json` entry
   - **Body** → from paired insight's `statement_vi`, `hidden_cost`, `reframe_angle`
   - **Solution/Proof** → from `profile.gains` (required/expected) + user's `cta.offer`
   - **Voice** → use customer vocabulary from `profile.voice`
4. Respect word count from formula spec + format (ig_caption / reels_30s / reels_60s / fb_post).
5. Generate hashtags: 3 broad + 5 niche + 2 branded (do not exceed 12).
6. Validate via `scripts/validate.py content` — every post must pass:
   - word count in range
   - uses_voice_vocabulary = true
   - no fabricated stats
   - no fabricated testimonials (use `[testimonial_X_placeholder]` if needed)
   - hook within first line
   - cta present
7. Write per-post markdown files to `output/{persona_slug}/posts/{post_id}_{formula}.md` for human review.

## Directory layout

```
content-engine/
├── SKILL.md                          # this file
├── README.md                         # buyer-facing intro
├── schemas/
│   ├── profile.schema.json
│   ├── insights.schema.json
│   ├── hooks.schema.json
│   └── content.schema.json
├── references/
│   ├── vpc-framework.md              # Stage 1 reference
│   └── storytelling-and-hooks.md     # Stages 3+4 reference
├── templates/                        # (build after foundation approved)
│   ├── prompt-stage1-profile.md
│   ├── prompt-stage2-insight.md
│   ├── prompt-stage3-hook.md
│   ├── prompt-stage4-content.md
│   └── brief-form.md
├── niche-packs/                      # (build after foundation approved)
│   ├── _universal.json
│   ├── beauty-creator.json
│   ├── coach-online.json
│   └── ...                           # 10 niches total
├── scripts/
│   ├── validate.py                   # JSON schema validator
│   └── render_post.py                # content.json → markdown post files
├── examples/
│   └── linh-beauty-28/               # full sample run for buyers
│       ├── profile.json
│       ├── insights.json
│       ├── hooks.json
│       └── posts/
└── output/                           # per-run artifacts
    └── {persona_slug}/
        ├── profile.json
        ├── insights.json
        ├── hooks.json
        ├── content.json
        └── posts/
```

## Commercial reliability rules

1. **Never fabricate testimonials.** Use `[testimonial_N_placeholder]` placeholders.
2. **Never hallucinate stats.** If profile has no observed stat, write qualitatively.
3. **Never paraphrase verbatim quotes** in `profile.voice.verbatim_bank` — keep original spelling/typos.
4. **Stage gates are hard.** If `profile.evidence_summary.ready_for_hook_stage = false`, do NOT proceed to Stage 2 without explicit user override.
5. **Language lock.** v1 = Vietnamese only. No code-switching unless brand voice explicitly allows.
6. **Source traceability.** Every pain/gain/job entry must carry `source_ref` or be marked `confidence: "assumed"`.
7. **CTA consistency.** Every Stage 4 post's CTA must align with the user-provided `cta.offer` from inputs. No drift.

## Cost transparency

- **fb-insight-miner data path** — quote user the fb-insight-miner cost (depth-dependent: $2–$6).
- **Brief-only path** — ~free (just AI tokens).
- **Per-stage AI tokens** by quality_mode:

| Stage | Economy (Sonnet 4.6) | Pro (Sonnet 4.6 + Opus 4.7 editorial) |
|---|---|---|
| 1 (profile mapping) | ~5K in / ~3K out | same |
| 2 (insights) | ~8K in / ~5K out | same |
| 3 (hooks) | ~10K in / ~8K out | same |
| 4 (content, 12 posts) | ~15K in / ~20K out (Sonnet) | ~30K in / ~25K out (Opus 4.7 + editorial) |
| **Total** | **~$0.80/run** | **~$2.50/run** |

**Cost-cap (hard stop):** if a single run exceeds **$5** in token cost, stop and ask user to confirm before continuing. Show running total after each stage.

## Failure modes

- **Profile thin (gates fail)** → Stop Stage 1. Recommend deeper data collection. Don't fake the gates.
- **Insights all generic (novelty_score ≤ 2 across the board)** → Likely Stage 1 voice/vocab is shallow. Reload profile, focus on `voice.verbatim_bank`.
- **Hooks all sound the same** → Pin hook type distribution explicitly; force ≥3 different types per insight.
- **Posts use generic words instead of customer voice** → Validate fail on `uses_voice_vocabulary`. Re-generate with stricter prompt citing `profile.voice` block.
- **CTA drift in posts** → Validate fail on `cta_present` + voice. Inject CTA from user input at template level, not by hoping AI remembers.
- **Buyer wants English output** → v1 doesn't support; tell user explicitly.

## Output language

Vietnamese only in v1. All examples, prompts, and posts in VN.

## Files to load at each stage

| Stage | Reference files | Schema |
|---|---|---|
| 1 | `references/vpc-framework.md` | `profile.schema.json` |
| 2 | `vpc-framework.md` §2.1 + `storytelling-and-hooks.md` §3 | `insights.schema.json` |
| 3 | `storytelling-and-hooks.md` §2 | `hooks.schema.json` |
| 4 | `storytelling-and-hooks.md` §1 + §4 | `content.schema.json` |

## Status

**v1.0** — foundation + templates + scripts + niche pack (coach personal brand) + 1 full example shipped.