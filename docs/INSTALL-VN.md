# 📦 Install Guide — Tiếng Việt

> **Cài đặt 5 phút. Không cần coding. Không cần technical background.**
> 
> Sau khi đọc guide này → chị có 10 skill Claude AI chạy live trên máy.

---

## ⚡ TL;DR — 4 bước

1. **Cài Claude Code** (5 phút)
2. **Download ZIP kit** từ GitHub
3. **Drop folder** vào `~/.claude/`
4. **Restart Claude Code** → test

→ Done. Bắt đầu dùng.

---

## 📋 Bước 1 — Cài Claude Code

### Trên Windows

1. Truy cập: https://claude.com/claude-code
2. Download Windows installer (.exe)
3. Run installer → "Next" → "Install"
4. Mở "Claude Code" từ Start Menu
5. Sign in via Anthropic account / Google

### Trên Mac

1. Truy cập: https://claude.com/claude-code  
2. Download Mac installer (.dmg)
3. Mở .dmg → drag "Claude Code" vào Applications
4. Mở Launchpad → click "Claude Code"
5. Sign in

### Trên Linux

1. Terminal: `curl -fsSL https://claude.ai/install.sh | sh`
2. Run `claude` from terminal

✅ **Done bước 1.**

---

## 📋 Bước 2 — Download ZIP Kit từ GitHub

### Cách 1: Download ZIP (KHÔNG cần git knowledge) ⭐

1. Mở browser → vào https://github.com/longyenkai83/personal-marketing-kit
2. Click nút xanh **"Code"** (góc phải bảng repo)
3. Trong dropdown → click **"Download ZIP"**
4. File `personal-marketing-kit-main.zip` tải về máy chị

**[Screenshot: Code button + Download ZIP]**

### Cách 2: GitHub Releases (versioned, stable hơn)

1. Mở https://github.com/longyenkai83/personal-marketing-kit/releases
2. Click **"Latest"** release (vd: v1.0.0)
3. Tải file `personal-marketing-kit-v1.0.0.zip`

→ Khuyến nghị Cách 2 nếu chị muốn version đã test stable.

---

## 📋 Bước 3 — Giải nén + Drop vào `~/.claude/`

### Giải nén ZIP

| OS | Cách |
|----|------|
| **Windows** | Right-click → "Extract All" → chọn folder đích |
| **Mac** | Double-click ZIP → tự động giải nén |
| **Linux** | `unzip personal-marketing-kit-main.zip` |

→ Ra folder `personal-marketing-kit-main/` (hoặc `personal-marketing-kit-v1.0.0/`)

### Tìm folder `~/.claude/` trên máy chị

#### Trên Windows
1. Mở File Explorer
2. Address bar → gõ: `%USERPROFILE%\.claude\`
3. Enter → folder mở ra

(Nếu folder `.claude` chưa tồn tại → mở Claude Code lần đầu → tự động tạo)

(Nếu không thấy folder ẩn → bật "Show hidden files" trong View → Options)

#### Trên Mac
1. Mở Finder
2. ⌘ + Shift + G
3. Gõ: `~/.claude/`
4. Enter

(Hoặc Terminal: `open ~/.claude/`)

#### Trên Linux
- Terminal: `cd ~/.claude/` rồi `nautilus .` (hoặc file manager khác)

### Drop kit vào `~/.claude/`

Mở 2 cửa sổ song song:
- **Trái**: Folder `personal-marketing-kit-main/` (vừa giải nén)
- **Phải**: Folder `~/.claude/` (vừa tìm)

Drag/drop:

| File/Folder source | Vào đâu |
|-------------------|---------|
| `skills/` (toàn bộ) | `~/.claude/skills/` |
| `CLAUDE.md` | `~/.claude/CLAUDE.md` |
| `shared/` (optional) | `~/.claude/shared/` |

**[Screenshot: 2 cửa sổ song song với drag/drop arrow]**

### Trường hợp đã có file/folder cũ trong `~/.claude/`

| Tình huống | Action |
|------------|--------|
| Chưa có folder `skills/` | Drop nguyên folder skills/ vào |
| Đã có folder `skills/` (có skill cũ) | MERGE: copy từng folder skill mới vào skills/ |
| Đã có file `CLAUDE.md` cũ | BACKUP file cũ → thay bằng file mới |

⚠️ **Quan trọng**: KHÔNG xóa folder `~/.claude/skills/` cũ nếu chị có skill custom. MERGE thay vì REPLACE.

---

## 📋 Bước 4 — Restart Claude Code + Verify

### Restart

⚠️ **Bắt buộc restart** để Claude Code đọc lại CLAUDE.md + skills mới.

1. Đóng hoàn toàn Claude Code (Quit / Exit, KHÔNG phải minimize)
2. Mở lại Claude Code
3. Sign in nếu hỏi

### Verify install — 3 test

#### Test 1: Hub auto-load

Trong Claude Code, gõ:

```
Tôi có những skill nào trong kit?
```

✅ **PASS** nếu Claude liệt kê được 10 skill (fb-insight-miner, kallaway-hook-master, kallaway-script-master, hook-swipe-library, content-engine, lead-magnet-factory, email-marketing-writer, tripwire-builder, digital-product-builder, subagent-architect)

❌ **FAIL** nếu Claude hỏi "kit nào?" → CLAUDE.md chưa load → check vị trí file

#### Test 2: Skill auto-invoke

Gõ:

```
Viết 5 hook viral cho topic "đóng gói chuyên môn"
```

✅ **PASS** nếu Claude:
- Auto suggest invoke `kallaway-hook-master` skill
- Output 5 hook đa framework
- Apply Kallaway 4-Component Alignment
- Xưng "anh / chị / em"

#### Test 3: Decision Tree

Gõ:

```
Anh muốn launch khoá học $97 đầu tiên — bắt đầu từ đâu?
```

✅ **PASS** nếu Claude:
- Mention 3-Pillar test (Pique Curiosity + Specific + Unbelievable)
- Suggest `digital-product-builder` skill
- Pricing 890k-2.3tr (VND, không $97 USD)
- Mention tech: Kajabi + Sam Cart hoặc bootstrap

🎉 **Pass cả 3 test → Kit live + work đúng. Bắt đầu dùng!**

---

## 🚀 Bắt đầu dùng — Workflow đầu tiên

### Workflow đề xuất cho người mới: Single reel + caption (30 phút)

```
Step 1: Open Claude Code
Step 2: Gõ — "Viết 5 hook về [topic chuyên môn của chị] theo Kallaway"
Step 3: Pick 1 hook strongest
Step 4: Gõ — "Viết kịch bản 60s từ hook đó"
Step 5: Gõ — "Viết caption FB/IG đi kèm"
Step 6: Quay reel + đăng
```

→ Detail: [`docs/WORKFLOW-B.md`](WORKFLOW-B.md)

---

## 🆘 Troubleshooting

### Vấn đề 1: Claude không liệt kê được skill

**Triệu chứng**: Gõ "Tôi có skill nào" → Claude hỏi "kit nào?"

**Fix**:
1. Check CLAUDE.md có nằm đúng `~/.claude/CLAUDE.md` không
2. Restart Claude Code (đóng hoàn toàn + mở lại)
3. Vẫn fail → [open issue](https://github.com/longyenkai83/personal-marketing-kit/issues)

### Vấn đề 2: Skill không trigger

**Triệu chứng**: Gõ "viết hook" → Claude generic, không apply Kallaway

**Fix**:
1. Check folder `skills/2-content/kallaway-hook-master/` có file `SKILL.md` đúng không
2. Mở SKILL.md → đảm bảo frontmatter `name: kallaway-hook-master` đúng
3. Restart Claude Code
4. Trigger explicit: "Apply skill kallaway-hook-master cho topic [X]"

### Vấn đề 3: Output không xưng "anh/chị/em"

**Triệu chứng**: Claude xưng "bạn" / "quý khách" generic

**Fix**:
- Check `~/.claude/CLAUDE.md` có section "QUY ƯỚC TUYỆT ĐỐI" không
- Nếu KHÔNG có → file CLAUDE.md sai version → tải lại từ kit
- Nếu CÓ → restart Claude Code

### Vấn đề 4: VN encoding lỗi (chữ Việt thành ?)

**Triệu chứng**: Output Việt thành "?" hoặc box vuông

**Fix Windows**:
- Settings → Time & Language → Language → Region settings
- Administrative → Change system locale → Vietnamese
- Restart máy

**Fix Mac/Linux**: Hiếm gặp, terminal default UTF-8.

### Vấn đề 5: Slow output hoặc timeout

**Triệu chứng**: Claude phản hồi chậm hoặc timeout

**Fix**:
- Internet check (Claude Code cần internet kết nối Anthropic API)
- Check tài khoản Anthropic balance (nếu Pro plan)
- Reduce context: skill phức tạp như `content-engine` 4-stage có thể dài → break thành 2-3 step nhỏ

---

## 💬 Support

### Self-help
1. Đọc [`CLAUDE.md`](../CLAUDE.md) hub → có decision tree + reference paths
2. Đọc SKILL.md của skill cụ thể → có troubleshooting section
3. Search [Issues tab](https://github.com/longyenkai83/personal-marketing-kit/issues)

### Community support
- GitHub Issues: [Open new issue](https://github.com/longyenkai83/personal-marketing-kit/issues/new)
- Star repo để follow updates

### Direct support (paid)
Nếu chị cần 1-1 support:
- 🎓 1-1 Onboarding 60 phút Zoom: 5tr — [Liên hệ]
- 💎 VIP Cohort 4 tuần: 15tr — [Liên hệ]
- 👑 Done-For-You: 50tr+ — [Liên hệ]

---

## 📚 Reference Index

| Document | Purpose |
|----------|---------|
| [`README.md`](../README.md) | Overview kit + skill list + workflows |
| [`CLAUDE.md`](../CLAUDE.md) | Hub auto-load (12 skill index + decision tree) |
| [`docs/INSTALL-VN.md`](INSTALL-VN.md) | This file — Vietnamese install guide |
| [`docs/INSTALL-EN.md`](INSTALL-EN.md) | English install guide |
| [`docs/WORKFLOW-A.md`](WORKFLOW-A.md) | Workflow A — Build full launch |
| [`docs/WORKFLOW-B.md`](WORKFLOW-B.md) | Workflow B — Single reel + caption |
| [`docs/WORKFLOW-C.md`](WORKFLOW-C.md) | Workflow C — Audit script cũ |
| [`docs/WORKFLOW-D.md`](WORKFLOW-D.md) | Workflow D — Customer research |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Contribution rules |
| [`CHANGELOG.md`](../CHANGELOG.md) | Version history |
| [`registry.json`](../registry.json) | Machine-readable skill index |

---

## ✅ Success Checklist (sau 30 ngày)

- [ ] Cài đặt thành công, all 10 skill load
- [ ] Đăng ≥5 reel với Kallaway hook + script
- [ ] Build lead magnet PDF
- [ ] Setup welcome 5-email sequence
- [ ] Setup tripwire 25k flow
- [ ] First 5 paying customers
- [ ] First 100 email subscriber
- [ ] First 10tr revenue (cumulative)

→ Ai làm xong checklist này = product validated cho chị.

🚀 **Best of luck với launch đầu tiên của chị!**

— [@longyenkai83](https://github.com/longyenkai83) 🤍
