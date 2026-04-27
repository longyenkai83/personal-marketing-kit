# Changelog

All notable changes to **Personal Marketing Kit** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-04-27

### 🎉 Initial Public Release

First public release của **Personal Marketing Kit** — 12 Claude Skills cho Vietnamese Women in Business.

### Added
- **10 production-ready Claude AI skills** organized into 6 categories:
  - **Stage 1 - Research**: `fb-insight-miner`
  - **Stage 2 - Content**: `kallaway-hook-master`, `kallaway-script-master`, `hook-swipe-library`, `content-engine`
  - **Stage 3 - Lead Magnet**: `lead-magnet-factory`
  - **Stage 4 - Email**: `email-marketing-writer`
  - **Stage 5 - Monetize**: `tripwire-builder`, `digital-product-builder`
  - **Stage 6 - Meta**: `subagent-architect`
- **CLAUDE.md hub** — auto-load 12 skills index + decision tree + 5 agent roles + tech stack defaults + anti-patterns
- **Shared resources**:
  - 3 niche-packs: `women-biz-vn.json` (default) + `coach-personal-brand.json` + `_universal.json`
  - 1 hook bank: `women-biz-vn-72.json` (72 proven hooks adapted from Kallaway 18-topic × 4-temperature framework)
  - 1 reference doc: `cta-library.md` (9 CTA types + Decision Tree + 70/20/10 rotation rule)
- **Documentation**:
  - `README.md` — sales-pitch overview với customer journey diagram
  - `docs/INSTALL-VN.md` — Vietnamese install guide step-by-step
  - `docs/INSTALL-EN.md` — English install guide
  - `docs/WORKFLOW-A.md` — Build full launch (1-2 weeks)
  - `docs/WORKFLOW-B.md` — Single reel + caption (30 min)
  - `docs/WORKFLOW-C.md` — Audit existing script (15 min)
  - `docs/WORKFLOW-D.md` — Customer research (45 min, ~$4)
  - `CONTRIBUTING.md` — Community contribution guide
  - `LICENSE` — MIT
- **Bootstrap prompt**: `prompts/bootstrap.md` — copy-paste cho ChatGPT/Gemini users
- **Registry**: `registry.json` — machine-readable skill index

### Source Methodologies (adapted)
- **Maria Wendt System** ($18M revenue):
  - 3-Pillar Viral Product (Pique Curiosity + Specific + Unbelievable)
  - Email funnel: campaigns / launches / automations
  - Welcome Coupon Email Automation ($50k/month playbook)
  - Subject line random + curiosity (50% time investment)
  - 9-Word Email (Dean Jackson) re-engagement
  - Look-personal email + reply-back algorithm hack
  - Pricing sweet spot $50-100 (1.2-2.3tr VN)
  - Tech stack minimal: Kajabi + Sam Cart only
- **Kallaway System** (viral video):
  - 6 Hook frameworks (Fortune Teller / Experimenter / Teacher / Magician / Investigator / Contrarian)
  - 5 Dream Outcome formats (About Me / If I / To You / Can You / He-She Just Did)
  - 4-Component Alignment (Spoken + Text + Visual + Audio)
  - 6 Levels Storytelling (Reporter → Trickster → Warrior → Architect → Translator → Artist)
  - 6 Story Locks (Naming / Embedded Truths / Thought Articulation / Negative Frames / Loop Openers / Contrast Words)
  - Underlying mechanism: CONTRAST

### Vietnamese Adaptations
- Persona default: phụ nữ KD VN 28-45 với chuyên môn (women in business)
- Pronoun convention: "anh / chị / em" (peer-level warmth)
- Pricing default: VND (25k-15tr range covered)
- Tone: truyền cảm hứng + tự tin + gần gũi (Maria Wendt + Vietnamese warmth)
- Niche pack `women-biz-vn.json` với 30+ verbatim quotes phụ nữ KD VN

### Distribution
- Public GitHub repo (MIT license)
- Download via "Code → Download ZIP" hoặc GitHub Releases
- Install vào `~/.claude/` (Claude Code default skill path)

### Known Limitations
- Optimized cho Vietnamese audience (English works but requires explicit prompting)
- Some skills require external tools (Kajabi/Sam Cart trial subscription)
- `fb-insight-miner` requires Apify MCP setup ($4 cost per scrape)
- VN-specific tech stack docs (SePay/VNPAY) chưa có (planned v1.1)

---

## Roadmap (Future versions)

### [1.1.0] — Planned Q3 2026

#### Planned additions
- **New skill**: `chatbot-flow-builder` — Manychat/Zalo OA auto-DM flows
- **New skill**: `vn-payment-setup` — SePay / VNPAY integration step-by-step
- **New niche-packs**: `mom-preneur.json`, `coach-fitness.json`, `freelancer-female.json`
- **Workflow file**: `docs/WORKFLOW-E-30-day-launch.md`
- **Video walkthrough**: 13-video series (5-10 min each) — link from README
- **Examples folder**: 5 case studies (chị Linh parenting, chị Hà dinh dưỡng, etc)

#### Planned improvements
- More Maria Wendt subject line examples (current: 30 → target: 100+)
- More hook bank variants (current: 72 women-biz-vn → target: 200+ across niches)
- Better English translations for international audience

### [2.0.0] — Planned 2027

#### Major features
- Full English version (parallel SKILL_EN.md alongside Vietnamese)
- Auto-install scripts (`install.sh` + `install.ps1`)
- Companion CLI tool (`pmk` command)
- Cohort program integration (private community + 1-1 review)

---

## Versioning Convention

This project follows [Semantic Versioning 2.0](https://semver.org/):
- **MAJOR** (X.0.0) — Breaking changes (skill renamed, restructured, removed)
- **MINOR** (1.X.0) — New skills, new features (backward compatible)
- **PATCH** (1.0.X) — Bug fixes, doc improvements (backward compatible)

---

## How to Update Your Local Kit

When new version released:

### Option 1: Download new ZIP
1. Vào https://github.com/longyenkai83/personal-marketing-kit/releases
2. Download latest ZIP
3. Extract + replace files trong `~/.claude/`
4. Restart Claude Code

### Option 2: Git pull (advanced)
```bash
cd /path/to/personal-marketing-kit
git pull origin main
# Then re-copy to ~/.claude/
```

→ Always check `CHANGELOG.md` cho breaking changes trước khi update.

---

## Credits

- **Maria Wendt** — *"Inbox to Income"* + *"How To Create A Viral Digital Product"* courses
- **Kallaway / Wavy Labs** — *"Hooks Workshop"* + *"6 Levels of Storytelling"* + *"6 Story Locks"*
- **Dean Jackson** — *9-Word Email* method
- **Adapted by** — [@longyenkai83](https://github.com/longyenkai83) for Vietnamese women-in-business niche
- **Anthropic Claude Code** — platform enabling this kit
- **Community contributors** — see GitHub Contributors page

---

🚀 **For contribution**: see [`CONTRIBUTING.md`](CONTRIBUTING.md)
