---
name: lead-magnet-factory
description: Build commercial-grade listicle lead magnet ebooks (Marie Forleo style, 9-page format) end-to-end — from niche/topic input to Canva-ready CSV + Markdown preview. Use when user wants to create a lead magnet, make an ebook, build a PDF freebie, produce a listicle ebook, or generate a sales funnel lead magnet. Works for Vietnamese and English output.
---

# Lead Magnet Factory

Commercial pipeline that turns a niche + topic into a publishable 9-page listicle ebook, matching the Marie Forleo "12 Mistakes" format. Output is a Canva Bulk Create CSV + human-readable Markdown preview — user pastes CSV into their Canva template, reviews, exports PDF.

## When to invoke

User intent examples (trigger keywords in Vietnamese + English):
- "làm lead magnet" / "tạo ebook" / "làm ebook 12 điều"
- "make a lead magnet" / "create a listicle ebook"
- "build a PDF freebie for my course"
- Any request for a numbered-tips PDF ebook (9–12 items)

Do NOT use this skill for: long-form ebooks (>20 pages), fiction, technical whitepapers, academic content. Those need different pipelines.

## Required inputs (ask user if missing)

1. **Niche** — e.g., "personal branding coaching cho creator Việt"
2. **Topic/angle** — e.g., "12 sai lầm khi build IG personal brand"
3. **Target audience** — persona: demographic + pain point + aspiration
4. **Product CTA** — what course/coaching/product the ebook sells into
5. **Language** — `vi` or `en`
6. **Brand voice notes** (optional) — if missing, default to Marie Forleo style in `reference/style_guide.md`
7. **Author name + signature style** — for final page
8. **Photo asset inventory** (optional) — list of photo filenames user has (e.g., `portrait_laptop.jpg`, `standing_smile.jpg`) so visual brief maps to real assets

If user provides fewer than 4 inputs, ask ONE consolidated question to fill all gaps. Do not go back-and-forth.

## 7-phase workflow

Execute phases sequentially. Use TodoWrite to track progress visibly to user.

### Phase 1 — Market Research (Tavily MCP)

Goal: Surface 25–40 candidate pain points / mistakes / "stop doing X" items.

Actions:
1. Call `mcp__tavily__tavily_research` with queries in the target language:
   - `"{niche} common mistakes 2026"`
   - `"{target_audience} biggest struggles {topic}"`
   - `"{niche} complaints reddit quora"`
   - For Vietnamese: also search `"{niche} Vietnam"` to surface local context
2. If user already has Airtable base `appZgsckgOCllyYjW` with competitor intel, pull viral content + pain point data via Airtable MCP (`list_records` on `Pain_Points` or `Content` table)
3. Extract candidate items into `output/{slug}/research_raw.json`:
   ```json
   [{"candidate": "text", "source": "url", "frequency_signal": "high|med|low", "emotion": "fear|frustration|aspiration"}]
   ```

Quality gate: ≥ 20 candidates before proceeding. If fewer, run 2 more Tavily queries.

### Phase 2 — Angle Selection (Claude reasoning)

Goal: Pick exactly 12 items that form a coherent narrative arc.

Scoring rubric (apply to each candidate):
- **Pain intensity** (1–5): how much does the reader suffer from this?
- **Specificity** (1–5): is it a concrete "stop X" or vague?
- **CTA fit** (1–5): does solving this naturally lead to the product CTA?
- **Variety** (1–5): does it add new angle vs already-selected items?

Select top 12 by composite score. Ensure narrative flow: open with mindset items → middle with tactical items → close with transformation/bigger-picture items (match Marie Forleo arc).

Write selection + rationale to `output/{slug}/selection.md` for review traceability.

### Phase 3 — Outline & Schema

For each of 12 items, generate outline:
- `heading`: "Stop {verb} {object}." — imperative, < 8 words
- `hook_sentence`: one punchy line (the "reframe")
- `body_outline`: 2 paragraphs — paragraph 1 = expose the problem/myth, paragraph 2 = actionable reframe + CTA internal-link

Also outline:
- Cover title + subtitle + highlight words
- Intro hook (2 paragraphs)
- Offer page (title, description, 3 benefits)
- Testimonials placeholder (5 slots — user fills real testimonials later)
- Closing page (4 differentiators + final CTA + signature)

### Phase 4 — Drafting (Claude Sonnet 4.6)

Write full content following `reference/style_guide.md`:
- Imperative, punchy sentences
- "You"-focused address
- Mix short + medium sentences (avoid walls of text)
- Use emoji markers sparingly (`👉 💖 💼 🌍 💡`) per Marie Forleo pattern
- Each item body: 40–80 words total across 2 paragraphs (Canva cell constraint)
- Signature power phrases where natural (avoid cliché: no more than 1 "the truth is" per ebook)

Output conforms to `schema.json`. Write to `output/{slug}/content.json`.

### Phase 5 — Editorial Pass (Opus 4.7 1M context if available, else Sonnet 4.6)

Read entire JSON in one context. Check:
- [ ] No item heading repeats a verb/object combo from another item
- [ ] Voice consistent across all 12 items
- [ ] No hallucinated statistics or fake testimonials (testimonial slots must be placeholders like `[testimonial_1_placeholder]`)
- [ ] CTA threads through: intro hints at it, items 6/12 foreshadow, offer page delivers
- [ ] Word counts within bounds (see `scripts/validate.py`)
- [ ] Language consistency (all Vietnamese or all English, no code-switching unless intentional)

Fix issues in-place. Re-write `content.json` if edits made.

### Phase 6 — Visual Brief (image mapping)

For each of 9 pages, produce visual instruction:
- If user provided `photo_asset_inventory`: map each page to best-fit filename (e.g., page 2 hook → `portrait_laptop.jpg`)
- If not: generate AI image prompt for Ideogram v3 (infographic/text-in-image) or Flux 2 (photorealistic)
- For cover + closing: always portrait of author (user's own photo preferred)

Write to `output/{slug}/visual_brief.md` with format:
```markdown
## Page 1 — Cover
Asset: portrait_confident.jpg (or AI prompt if no asset)
Treatment: lime green stroke around figure, purple background card
Notes: title overlays with orange pill-highlight on key word
```

### Phase 7 — Export

Run scripts in order:
1. `python scripts/validate.py output/{slug}/content.json` — must pass all gates
2. `python scripts/to_canva_csv.py output/{slug}/content.json output/{slug}/canva_bulk.csv`
3. Generate human-readable `output/{slug}/preview.md` by formatting content.json into Markdown
4. If Airtable MCP available, upsert summary row to `Ebooks` table (create table if missing): `{slug, niche, topic, generated_at, status: "draft_ready"}`

Final message to user must include:
- Path to CSV for Canva Bulk Create
- Path to Markdown preview for review
- Path to visual brief
- Next-step instructions (3 steps max): open Canva template → Bulk Create → upload CSV

## Directory layout (per ebook run)

```
output/
  {slug}/                          # e.g., 12-sai-lam-ig-2026
    research_raw.json              # Phase 1
    selection.md                   # Phase 2
    content.json                   # Phase 3–5 (final structured)
    visual_brief.md                # Phase 6
    canva_bulk.csv                 # Phase 7 — UPLOAD THIS TO CANVA
    preview.md                     # Phase 7 — REVIEW THIS
```

## Commercial reliability rules

1. **Never fabricate testimonials.** Use placeholders `[testimonial_1_placeholder]` — user replaces with real ones before publishing.
2. **Never hallucinate statistics.** If Phase 1 research didn't surface a stat, don't invent one. Use qualitative language instead.
3. **Cite sources in `selection.md`** for every item that came from a specific research source.
4. **Language lock.** Do not code-switch between Vietnamese and English inside body text unless brand voice explicitly allows it.
5. **Copyright clean.** Headlines and phrasing must be original — do not copy Marie Forleo's exact wording; use her structural template only.
6. **Legal/health/finance disclaimer.** If niche touches health, finance, or legal — append a disclaimer line to the closing page.

## Cost budget per run

Expected token usage (Sonnet 4.6 for drafting, Opus 4.7 for final pass):
- Research: ~5K in, ~3K out
- Selection + Outline: ~3K in, ~4K out
- Drafting: ~5K in, ~3K out
- Editorial: ~10K in (full doc), ~3K out
- Visual brief: ~3K in, ~2K out

Total: ~26K input + 15K output ≈ $0.50–$1.00/ebook. Flag user if a run exceeds $2.

## Failure modes to watch

- **Tavily returns thin results** → widen queries, don't fabricate. If still thin, ask user for seed pain points.
- **Items 1–12 feel repetitive** → in Phase 5, detect and rewrite. Never ship with duplicate angles.
- **CTA doesn't thread** → rewrite offer page to match final item's handoff line.
- **Language/voice drift** → Phase 5 must catch this. If drift is systemic, re-run Phase 4 with stricter style guide citation.

## Reference files (read at invocation)

- `reference/style_guide.md` — voice, sentence patterns, emoji conventions
- `reference/canva_template_spec.md` — exact placeholder names expected by user's Canva template
- `schema.json` — strict output schema
- `examples/sample_output.json` — reference Vietnamese example

Load `reference/style_guide.md` into context at Phase 4 start. Load `schema.json` at Phase 3 start.
