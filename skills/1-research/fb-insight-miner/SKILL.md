---
name: fb-insight-miner
description: Deep customer insight mining from public Facebook fanpage comments. Use when user wants to research customer pain points, desires, objections, voice-of-customer vocabulary, FAQ patterns, or silent signals from a Facebook fanpage (competitor or target niche). Scrapes posts+comments via Apify MCP then runs a 4-phase pipeline (preflight → collect → sample+analyze → enrich) to produce a Customer Insight Report in markdown. Vietnamese-output friendly. Triggers on phrases like "phân tích insight fanpage", "đào comment fanpage", "customer research FB", "pain points fanpage", "voice of customer FB".
---

# Facebook Fanpage Customer Insight Miner

## Purpose
Given a public Facebook fanpage URL, extract deep customer insights from comments to inform content strategy, copywriting, and offer design.

## When to trigger
Auto-trigger when user says (Vietnamese or English):
- "phân tích insight fanpage X"
- "đào comment fanpage X"
- "customer research fanpage FB"
- "pain points từ fanpage X"
- "voice of customer FB"
- Or user uses `/fb-insight-miner <url>` command

## Required environment
- **Apify MCP** connected (verify with `mcp__apify__*` tools available)
- **Python 3** installed (for scripts/ pipeline)
- Optional: Google Drive MCP (`mcp__claude_ai_Google_Drive__*`) if `output=gdrive`

### ⚠️ Windows environment note
When running Python scripts that print Vietnamese/emoji output, prefix with `PYTHONIOENCODING=utf-8`:
```bash
PYTHONIOENCODING=utf-8 python scripts/sample.py ...
```
Without this, script crashes on `UnicodeEncodeError` (cp1252 codec).

## Inputs needed from user (ask if missing)
1. **fanpage_url** — e.g. `https://www.facebook.com/brandname`
2. **depth** — default `standard`:
   - `light`: 20 posts, ~500 comments (~$2)
   - `standard`: 50 posts, ~1,500 comments (~$4)
   - `deep`: 80 posts, ~3,000+ comments (~$6)
3. **days** — time window, default `90`
4. **output** — `chat` | `file` | `gdrive`, default `chat`

## Workflow — Execute in order

### Phase 0 — Preflight (verify + cost transparency)

**0.1 — Verify URL is a public fanpage, not profile/group**
- Call WebFetch or Tavily extract on fanpage URL
- If response looks like personal profile (single name, "City" only, no page metadata) → STOP, ask user to confirm it's really a fanpage
- Apify fb-posts-scraper only works on public PAGES, not personal profiles

**0.2 — Cost estimate + confirmation**
Calculate based on depth:
- posts × $0.005 + comments × $0.0025 + 2 × $0.001 actor starts
Present to user and ask for go/no-go before burning credit.

### Phase 1 — Collect (Apify MCP)

**1.1 — Scrape posts**
- Actor: `apify/facebook-posts-scraper`
- Key input fields (verified from real runs):
  ```json
  {
    "startUrls": [{"url": "<fanpage_url>"}],
    "resultsLimit": <light=20 / standard=50 / deep=80>,
    "onlyPostsNewerThan": "<days> days",
    "captionText": false
  }
  ```
- Keep fields via `get-actor-output` with `fields="url,text,likes,comments,shares"` to minimize tokens.

**1.2 — Rank posts by engagement**
- Sort by `comments` (commentsCount) DESC.
- For `light`/`standard`/`deep`: keep top 20 posts → these give ~80%+ of total comment signal.
- Skip posts with 0 comments (no signal).

**1.3 — Scrape comments (top 20 posts)**
- Actor: `apify/facebook-comments-scraper`
- Input:
  ```json
  {
    "startUrls": [<top20_post_urls>],
    "resultsLimit": 1500,
    "includeNestedComments": true,
    "viewOption": "RANKED_UNFILTERED"
  }
  ```
- Store dataset ID — Apify output will be >25K tokens, use Python pipeline in Phase 2.

### Phase 2 — Sample + Compact (Python scripts)

Apify returns raw JSON often >25K tokens — cannot load directly. Use pipeline:

**2.1 — Apply sampling rules**
```bash
PYTHONIOENCODING=utf-8 python scripts/sample.py <raw.json> "<Page Owner Name>" <filtered.json>
```
- Page owner name = profile name of admin (scrape from profileName where posted by page)
- Outputs filtered JSON + prints sampling stats
- See `references/sampling-rules.md` for rule details

**2.2 — Convert to compact text**
```bash
PYTHONIOENCODING=utf-8 python scripts/compact.py <filtered.json> <compact.txt>
```
- Reduces token usage ~70%
- Groups by post, sorts comments by likes DESC
- Format: `[likes|replies|depth|signals] author — text`

### Phase 3 — Analyze (3-pass AI)

Read the `compact.txt` into context, then run passes **internally** (no need to write pass files — Claude does inline):

**Pass 1 — Breadth** — follow `templates/prompt-pass1-breadth.md`
Cluster into 9 dimensions (`references/9-insight-dimensions.md`), count frequency, representative quotes.

**Pass 2 — Depth** — follow `templates/prompt-pass2-depth.md`
Per-dimension sub-themes, ≥10 verbatim quotes each, language patterns.

**Pass 3 — Synthesis** — follow `templates/prompt-pass3-synthesis.md`
Cross-theme patterns, silent signals (`references/silent-signals-guide.md`), persona, temporal drift.

### Phase 4 — Enrichment (Python + Claude narrative)

**4.1 — Run enrichment script**
```bash
PYTHONIOENCODING=utf-8 python scripts/enrich.py <raw.json> "<Page Owner>" <enrichment.txt>
```
This produces 6 micro-reports:
1. Admin voice decoding (page owner's own replies)
2. Top commenters — DM outreach list
3. Deep thread conversations
4. N-gram analysis — repeat VoC phrases
5. Tag-a-friend mechanic detection
6. Emoji-emotion fingerprint per post

**4.2 — Synthesize novel findings**
Read enrichment.txt, identify insights NOT covered in Phase 3 report. Focus on:
- What repeat bigrams/trigrams reveal about VoC
- Superfans → DM outreach candidates
- Admin voice patterns (short vs teaching vs funnel)
- Tag-a-friend viral mechanics
- Emotional fingerprints per post type

### Phase 5 — Report

Use `templates/insight-report.md` structure, filled with outputs from Phase 3 + Phase 4.

Save per `output`:
- `chat`: print full report in conversation
- `file`: write to CWD as `fb-insight-<fanpage-slug>-<YYYYMMDD>.md`
- `gdrive`: base64 encode + call `mcp__claude_ai_Google_Drive__create_file`

## Cost transparency
- Always estimate before Phase 1
- Always report actual cost after Phase 1 (posts_count × $0.005 + comments_count × $0.0025 + actor_starts × $0.001)

## Failure modes & edge cases
- Fanpage private/deleted → stop, report to user
- URL is personal profile → stop (actor can't scrape profiles)
- Fanpage has <30 posts in window → suggest `depth=light` (avoid waste)
- <50 comments total scraped → warn insight will be shallow; proceed with degraded confidence
- Apify MCP not connected → explain how to connect
- Apify output >25K tokens (always) → use Python pipeline in Phase 2 (never Read raw JSON directly)
- Claude context near limit during Phase 3 → reduce sampling cap from 1500 to 800
- **⚠️ Adult/sensitive-content fanpage → posts scrape OK but comments return near-zero** (age-gated/adult-hint filtering). Detected in real run on sex-ed academy: 20 posts scraped fine, only 2/2000 comments returned from 2 different actors. **Detection heuristic:** if comment scrape returns <5% of expected comments on first 3 URLs → STOP and tell user. Niches that hit this: sexual wellness, dating-explicit, adult education. **Workaround:** none via public API. Need manual cookies-based scraper OR pivot to IG/TikTok where filtering differs.

## Output language
Default Vietnamese unless fanpage content is primarily English. Keep verbatim quotes in ORIGINAL language — NEVER translate them.

## Files in this skill
```
fb-insight-miner/
├── SKILL.md                        # This file
├── scripts/
│   ├── sample.py                   # Phase 2.1 — sampling rules
│   ├── compact.py                  # Phase 2.2 — JSON→text
│   └── enrich.py                   # Phase 4.1 — 6 micro-reports
├── templates/
│   ├── insight-report.md           # Phase 5 report structure
│   ├── prompt-pass1-breadth.md     # Phase 3 pass 1
│   ├── prompt-pass2-depth.md       # Phase 3 pass 2
│   └── prompt-pass3-synthesis.md   # Phase 3 pass 3
└── references/
    ├── 9-insight-dimensions.md     # 9-axis framework
    ├── sampling-rules.md           # Sampling logic details
    └── silent-signals-guide.md     # Advanced signals
```