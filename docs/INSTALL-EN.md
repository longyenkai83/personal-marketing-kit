# 📦 Install Guide — English

> **5-minute install. No coding. No technical background needed.**
> 
> After this guide → you'll have 10 Claude AI skills running on your machine.

---

## ⚡ TL;DR — 4 steps

1. **Install Claude Code** (5 min)
2. **Download ZIP** from GitHub
3. **Drop folder** into `~/.claude/`
4. **Restart Claude Code** → verify

→ Done.

---

## 📋 Step 1 — Install Claude Code

### Windows / Mac / Linux

Download installer: https://claude.com/claude-code

- **Windows**: `.exe` installer → run → "Next" → "Install"
- **Mac**: `.dmg` → drag to Applications
- **Linux**: `curl -fsSL https://claude.ai/install.sh | sh`

Sign in via Anthropic account / Google.

✅ **Done step 1.**

---

## 📋 Step 2 — Download ZIP from GitHub

### Option A: Download ZIP (no git needed) ⭐

1. Go to: https://github.com/longyenkai83/personal-marketing-kit
2. Click green **"Code"** button
3. Click **"Download ZIP"**
4. File `personal-marketing-kit-main.zip` downloads

### Option B: GitHub Releases (versioned, stable)

1. https://github.com/longyenkai83/personal-marketing-kit/releases
2. Click **"Latest"** release
3. Download `personal-marketing-kit-v1.0.0.zip`

→ **Recommended Option B** for stable version.

### Option C: Git clone (advanced)

```bash
git clone https://github.com/longyenkai83/personal-marketing-kit.git
cd personal-marketing-kit
```

---

## 📋 Step 3 — Extract + Drop into `~/.claude/`

### Extract ZIP

| OS | How |
|----|-----|
| **Windows** | Right-click → "Extract All" |
| **Mac** | Double-click ZIP → auto-extract |
| **Linux** | `unzip personal-marketing-kit-main.zip` |

### Find `~/.claude/` folder

| OS | Path |
|----|------|
| **Windows** | `C:\Users\[YourUsername]\.claude\` |
| **Mac** | `/Users/[YourUsername]/.claude/` |
| **Linux** | `/home/[YourUsername]/.claude/` |

### Drop kit files

| Source | Destination |
|--------|-------------|
| `skills/` (entire folder) | `~/.claude/skills/` |
| `CLAUDE.md` | `~/.claude/CLAUDE.md` |
| `shared/` (optional) | `~/.claude/shared/` |

⚠️ **Important**: If you have existing `~/.claude/skills/` with custom skills → MERGE (don't replace).

---

## 📋 Step 4 — Restart Claude Code + Verify

### Restart

⚠️ **Required restart** for Claude Code to reload CLAUDE.md + skills.

1. Quit Claude Code completely (NOT minimize)
2. Open Claude Code again
3. Sign in if asked

### Verify install — 3 tests

#### Test 1: Hub loads

Type:

```
What skills do I have in this kit?
```

✅ **PASS** if Claude lists 10 skills (fb-insight-miner, kallaway-hook-master, kallaway-script-master, hook-swipe-library, content-engine, lead-magnet-factory, email-marketing-writer, tripwire-builder, digital-product-builder, subagent-architect)

#### Test 2: Skill auto-invoke

Type:

```
Write 5 viral hooks about "packaging expertise into digital products"
```

✅ **PASS** if Claude:
- Auto-invokes `kallaway-hook-master` skill
- Outputs 5 hooks across multiple frameworks
- Applies Kallaway 4-Component Alignment

#### Test 3: Decision Tree

Type:

```
I want to launch my first $97 course — where do I start?
```

✅ **PASS** if Claude:
- Mentions 3-Pillar test (Pique Curiosity + Specific + Unbelievable)
- Suggests `digital-product-builder` skill
- Mentions Maria Wendt sweet spot pricing
- Mentions tech stack: Kajabi + Sam Cart

🎉 **Pass all 3 → Kit is live and working!**

---

## 🚀 Quick Start

### Workflow B (recommended for beginners): Single reel + caption (30 min)

```
1. Open Claude Code
2. Type: "Write 5 hooks about [your expertise topic] using Kallaway"
3. Pick strongest hook
4. Type: "Write 60s script from this hook"
5. Type: "Write FB/IG caption to accompany"
6. Shoot reel + post
```

→ Detail: [`docs/WORKFLOW-B.md`](WORKFLOW-B.md)

---

## 🇻🇳 Vietnamese-First Note

**This kit is optimized for Vietnamese audience** (women in business niche). All skills:
- Output in Vietnamese by default (you can request English)
- Use "anh / chị / em" pronouns (Vietnamese peer-level warmth)
- Pricing in VND (you can request USD)
- Cultural context for Vietnamese market

**For English/international use**: skills work but may require explicit prompting like "Output in English with USD pricing."

---

## 🆘 Troubleshooting

See [`docs/INSTALL-VN.md`](INSTALL-VN.md) — Troubleshooting section (English-translated below):

### Issue 1: Claude doesn't list skills
- Check CLAUDE.md is at `~/.claude/CLAUDE.md`
- Restart Claude Code
- Still failing → [open issue](https://github.com/longyenkai83/personal-marketing-kit/issues)

### Issue 2: Skill doesn't trigger
- Check `skills/2-content/kallaway-hook-master/SKILL.md` exists
- Verify frontmatter `name: kallaway-hook-master` correct
- Restart + try explicit trigger: "Apply skill kallaway-hook-master for topic X"

### Issue 3: Slow output
- Check internet connection
- Verify Anthropic account balance
- Break large tasks into smaller steps

---

## 💬 Support

- **GitHub Issues**: [Report bug / ask question](https://github.com/longyenkai83/personal-marketing-kit/issues)
- **Star repo** to follow updates
- **Paid 1-1 support** (in Vietnamese): contact [@longyenkai83](https://github.com/longyenkai83)

---

## 📚 Reference Index

| Document | Purpose |
|----------|---------|
| [README.md](../README.md) | Kit overview |
| [CLAUDE.md](../CLAUDE.md) | Hub (auto-load) |
| [INSTALL-VN.md](INSTALL-VN.md) | Vietnamese install (with screenshots) |
| [WORKFLOW-A.md](WORKFLOW-A.md) | Build full launch |
| [WORKFLOW-B.md](WORKFLOW-B.md) | Single reel + caption |
| [WORKFLOW-C.md](WORKFLOW-C.md) | Audit existing script |
| [WORKFLOW-D.md](WORKFLOW-D.md) | Customer research |

---

🚀 **Welcome to Personal Marketing Kit!**

— [@longyenkai83](https://github.com/longyenkai83)
