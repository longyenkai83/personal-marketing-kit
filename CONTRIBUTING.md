# Contributing to Personal Marketing Kit

Cảm ơn anh chị đã quan tâm đóng góp! 🤍

Kit này MIT open source — welcome mọi contributions để kit ngày càng hữu ích cho phụ nữ KD VN.

---

## 🎯 Cách contribute

### 1. Báo bug / lỗi (Easiest)

Nếu chị thấy bug hoặc skill output sai:
1. Vào [Issues tab](https://github.com/longyenkai83/personal-marketing-kit/issues)
2. Click "New Issue"
3. Chọn template "Bug report"
4. Mô tả:
   - Skill nào bị lỗi
   - Input chị gõ vào Claude Code
   - Output expected vs actual
   - Screenshot nếu có

### 2. Đề xuất feature mới

Cho ý tưởng skill mới hoặc improvement:
1. Vào Issues → "New Issue" → "Feature request"
2. Mô tả:
   - Vấn đề chị gặp (mà kit chưa giải quyết)
   - Skill / feature đề xuất
   - Cách chị hình dung sẽ work

### 3. Improve existing skill (Pull Request)

Nếu chị muốn tự fix/improve skill:
1. Fork repo này
2. Clone về máy: `git clone https://github.com/[your-username]/personal-marketing-kit.git`
3. Tạo branch mới: `git checkout -b improve-[skill-name]`
4. Edit skill files
5. Commit + push: `git push origin improve-[skill-name]`
6. Open Pull Request

### 4. Add new niche-pack

Có ngách specific (vd: coach fitness, mom-preneur, freelancer designer) không có trong kit:
1. Copy template `shared/niche-packs/_universal.json`
2. Customize cho ngách của chị
3. Lưu thành `shared/niche-packs/[niche-name].json`
4. Open PR với:
   - Niche description (1 paragraph)
   - Verbatim quotes nếu có data thật từ FB insight miner
   - Sample output (1 hook + 1 caption test)

### 5. Add translation

Kit hiện Vietnamese-first. Welcome translations sang:
- English (full)
- Thai / Indonesian / Filipino (Southeast Asia neighbors)
- Chinese / Japanese / Korean (Asia)

→ Open PR với folder `i18n/[language-code]/` chứa translated SKILL.md files.

### 6. Build new skill

Nếu chị muốn add skill mới (vd: chatbot-flow-builder, vn-payment-setup):
1. Use `subagent-architect` skill để scaffold
2. Build SKILL.md + references/ + templates/
3. Test với 5-10 inputs
4. Open PR với:
   - SKILL.md frontmatter đúng spec (name, description, triggers)
   - At least 1 reference doc + 1 template
   - Example outputs trong PR description

---

## 📋 Contribution Standards

### Skill quality bar

Mỗi skill MUST có:
- ✅ `SKILL.md` frontmatter complete (name, description, triggers, allowed-tools)
- ✅ "When to use" + "When NOT to use" sections rõ
- ✅ At least 1 example output
- ✅ Anti-patterns section
- ✅ Failure modes documented

### Naming convention

- Skill folder: kebab-case (`kallaway-hook-master`, không `KallawayHookMaster`)
- Reference files: kebab-case `.md` (`6-hook-frameworks.md`)
- Template files: kebab-case `.md` (`hook-writing-worksheet.md`)
- JSON files: kebab-case `.json` (`women-biz-vn.json`)

### Vietnamese tone

Default output Vietnamese:
- Xưng "anh / chị / em" (peer-level warmth)
- KHÔNG dùng "ngài / quý khách / chúng tôi" (formal)
- Tone: truyền cảm hứng + tự tin + gần gũi (Maria Wendt style)

### Source citations

Nếu skill base trên methodology external:
- Cite source rõ (Maria Wendt course / Kallaway video / Dean Jackson method)
- KHÔNG copy-paste tài liệu Maria/Kallaway raw (copyright)
- Adapt + add value layer

### Anti-patterns to AVOID

- ❌ Skill output bịa số liệu / testimonial fake
- ❌ Skill mặc định CTA "Comment X nhận DM Y" cho mọi context
- ❌ Skill output English khi user Vietnamese
- ❌ Skill recommend tool không free/cheap (vd: $500/month enterprise tools)
- ❌ Skill require API key đắt mà không note rõ cost

---

## 🧪 Testing your contribution

### Local test (before PR)

1. Drop your modified skill vào `~/.claude/skills/`
2. Restart Claude Code
3. Test 3-5 typical inputs
4. Check output:
   - Quality (tone + content)
   - Consistency (multiple runs same prompt)
   - Anti-patterns avoided
5. Document test results trong PR description

### PR template

```markdown
## What this PR does
[Brief description]

## Skill changed/added
- Skill name:
- Category:

## Testing
- [ ] Tested with 5+ different inputs
- [ ] Output quality consistent
- [ ] No anti-patterns triggered
- [ ] Vietnamese tone correct

## Sample outputs
[Paste 1-2 sample outputs to demonstrate quality]

## Breaking changes
[Yes/No — if yes, explain migration]
```

---

## 🚀 Review process

1. PR opened → reviewer (maintainer) sẽ check trong 7-14 ngày
2. Feedback comments → chị adjust
3. Merge khi quality bar pass
4. Merged contributions → mention trong CHANGELOG.md + README contributors section

---

## 💚 Community values

### Be kind
Phụ nữ KD VN community small + supportive. Disagree với respect. No personal attacks.

### Vietnamese-first
This kit serves VN women. English contributions welcome BUT VN remains default.

### Open source spirit
Take + give back. Use kit free → contribute back when you can (bug report / feature suggest / niche-pack).

### Avoid spam
- ❌ PR chỉ thay đổi tag SEO không real value
- ❌ PR copy-paste skill từ kit khác mà không adapt
- ❌ Issue gửi tin nhắn quảng cáo
- ❌ Discussions promote service không liên quan

---

## 🆘 Cần help?

- Question về kit → [Issues](https://github.com/longyenkai83/personal-marketing-kit/issues) → tag "question"
- Question về contribute → email [@longyenkai83]
- Want to discuss methodology → Discussions tab

---

## 📜 License

By contributing, you agree your contribution will be MIT licensed (same as kit).

→ Full license: [`LICENSE`](LICENSE)

---

🤍 **Thank you for contributing — together we build better tools cho phụ nữ KD VN!**

— [@longyenkai83](https://github.com/longyenkai83)
