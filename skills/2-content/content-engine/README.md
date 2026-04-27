# Content Engine

> Bộ máy 4 stage biến hồ sơ khách hàng thành post IG/Reels chất lượng — dành cho coach + creator VN xây thương hiệu cá nhân trên IG/FB.

## Bạn nhận được gì

```
Stage 1 — Customer Profile (VPC)
   IN  : niche + nguồn data (fanpage / brief / cả hai)
   OUT : profile.json — Jobs / Pains / Gains / Demographics / Voice / Vocabulary
        (đầy đủ verbatim quotes của khách hàng thật)

Stage 2 — Insight Mining
   IN  : profile.json
   OUT : insights.json — 10-25 insights (tension, contradiction, "say vs do",
        surprise, aspiration, objection, transformation, identity-shift)

Stage 3 — Hook Library
   IN  : profile.json + insights.json
   OUT : hooks.json — 30-100 hooks (8 type) đã ánh xạ insight + công thức

Stage 4 — Content Generation
   IN  : profile.json + insights.json + hooks.json
   OUT : content.json + posts/*.md (post hoàn chỉnh theo công thức
        PAS / BAB / StoryBrand / Hero / 4P / Hot Take)
```

Mỗi stage lưu artifact JSON riêng. Bạn có thể edit tay giữa chừng, rerun stage sau mà không mất data trước.

## Trigger phrases

Skill tự kích hoạt khi bạn nói (Vietnamese hoặc English):
- "lập hồ sơ khách hàng + viết content"
- "content engine"
- "viết content theo VPC"
- "bộ máy content"
- "factory content"

Hoặc: `/content-engine`

## Inputs cần chuẩn bị

1. **Persona/niche** — ví dụ "coach 1-1 chuyển sang cohort", "beauty creator pivot mini-course"
2. **Data source** — chọn 1:
   - `fanpage_url` — FB fanpage public của competitor/đối thủ → skill scrape qua `fb-insight-miner`
   - `brief` — điền form 20 câu trong `templates/brief-form.md`
   - `hybrid` — cả 2 (recommend nếu muốn confidence cao)
3. **Content goal** — `awareness` / `lead` / `sale` (default: lead)
4. **Output format** — `ig_caption` / `reels_30s` / `reels_60s` / `fb_post` / `multi`
5. **Số bài cần** — default 12
6. **CTA chính** — sản phẩm/offer (vd: "Cohort Lab tháng 5 — link bio")
7. **Quality mode** — `economy` (default, ~$0.80/run) hoặc `pro` (~$2.50/run, thêm editorial pass Opus 4.7)

## Quy trình điển hình

```bash
# Bước 1: kích hoạt skill
"Bộ máy content cho persona coach mới ra nghề muốn launch cohort"

# Skill sẽ hỏi data source. Nếu fanpage:
# → tự gọi fb-insight-miner trên URL bạn cung cấp
# → ~$2-6 tuỳ depth

# Stage 1: profile.json sẽ được tạo, bạn review trong VSCode
# Stage 2: insights.json (10-25 insights)
# Stage 3: hooks.json (30-100 hooks)
# Stage 4: content.json + posts/*.md (12 posts mặc định)

# Bạn cũng có thể chạy validate độc lập:
PYTHONIOENCODING=utf-8 python scripts/validate.py profile output/{slug}/profile.json
PYTHONIOENCODING=utf-8 python scripts/render_post.py output/{slug}/content.json
```

## Folder structure

```
content-engine/
├── SKILL.md                          # entry point — Claude reads first
├── README.md                         # bạn đang đọc
├── schemas/
│   ├── profile.schema.json           # Stage 1 output spec
│   ├── insights.schema.json          # Stage 2
│   ├── hooks.schema.json             # Stage 3
│   └── content.schema.json           # Stage 4
├── references/
│   ├── vpc-framework.md              # VPC chi tiết, VN-friendly
│   └── storytelling-and-hooks.md     # 8 storytelling formulas + 8 hook types
├── templates/
│   ├── brief-form.md                 # form 20 câu (path không có fanpage)
│   └── prompt-stage{1,2,3,4}-*.md   # prompt internal cho từng stage
├── niche-packs/
│   ├── _universal.json               # fallback priors
│   └── coach-personal-brand.json     # priors cho niche coach VN
├── scripts/
│   ├── validate.py                   # JSON schema validator
│   └── render_post.py                # content.json → posts/*.md
├── examples/
│   └── mai-coach/                    # full pipeline demo (Linh persona)
│       ├── profile.json
│       ├── insights.json
│       ├── hooks.json
│       ├── content.json
│       └── posts/
│           ├── post_001_hot_take.md  # Awareness post
│           ├── post_002_pas.md       # Lead post
│           ├── post_003_bab.md       # Sale post
│           └── post_004_hero.md      # Reels 30s
└── output/                           # mỗi run của bạn ghi vào đây
    └── {persona_slug}/
```

## Commercial reliability rules

Skill được thiết kế để bán — nên có 7 rule cứng:

1. **Không bịa testimonial.** Dùng `[testimonial_X_placeholder]`.
2. **Không bịa số liệu.** Không có thì viết qualitative.
3. **Không paraphrase verbatim quotes** — giữ nguyên typo và slang.
4. **Stage gates cứng** — profile thiếu `observed_pct ≥ 60%` thì block Stage 2.
5. **Language lock** — v1 chỉ Vietnamese.
6. **Source traceability** — mỗi entry phải có source_ref hoặc đánh dấu `assumed`.
7. **CTA không drift** — CTA mỗi post phải khớp offer bạn nhập, không tự sinh ra offer mới.

## Cost budget per run

| Stage | Economy (Sonnet 4.6) | Pro (+ Opus 4.7 editorial) |
|---|---|---|
| 1 (profile) | ~5K in / ~3K out | same |
| 2 (insights) | ~8K in / ~5K out | same |
| 3 (hooks) | ~10K in / ~8K out | same |
| 4 (12 posts) | ~15K in / ~20K out | ~30K in / ~25K out |
| **Total** | **~$0.80/run** | **~$2.50/run** |

**Cost cap:** nếu một run vượt $5 → skill dừng và xin xác nhận.

(Cộng thêm chi phí `fb-insight-miner` $2-6 nếu chọn data path fanpage.)

## Yêu cầu môi trường

- **Claude Code** — skill này chạy trong Claude Code (Cursor/VSCode/CLI).
- **Python 3** + `jsonschema` package: `pip install jsonschema` (cho `scripts/validate.py`).
- **Apify MCP** — chỉ cần nếu bạn muốn dùng path `fanpage_url` (data scrape).
- **Windows**: prefix Python commands với `PYTHONIOENCODING=utf-8` để tránh lỗi mã hoá VN/emoji.

## Niche packs (v1)

- `coach-personal-brand.json` — coach VN xây thương hiệu cá nhân (life / leadership / wellness / mindset)
- `_universal.json` — fallback minimum priors (dùng khi niche chưa có pack)

Niche packs là **starting priors**, không phải observed data. Skill sẽ verify mỗi entry trong niche pack với data thật trước khi promote sang `inferred` hoặc `observed`.

## Limitations v1

- ✅ IG caption + Reels 30s/60s + FB post
- ❌ TikTok script (sắp có)
- ❌ Email / blog (cần skill khác)
- ❌ English output (sắp có)
- ❌ Long-form sales page (cần skill khác)

## Câu hỏi thường gặp

**Q: Skill có viết được content cho bất kỳ niche nào không?**
A: Có. Nếu niche không có pack riêng, skill dùng `_universal.json` + brief 20 câu của bạn để fill profile.

**Q: Tôi không có fanpage để scrape thì sao?**
A: Dùng path `brief` — điền `templates/brief-form.md` 20 câu. Phù hợp cho coach chưa có competitor rõ ràng.

**Q: Output có thể edit tay không?**
A: Có. JSON 4 artifact đều human-readable. Edit bằng VSCode rồi rerun stage sau — không mất data trước.

**Q: Skill có gửi data ra ngoài không?**
A: Chỉ gửi tới Apify (nếu chọn path fanpage scrape). Brief data và output đều ở local máy bạn.

**Q: Tôi có thể bán content này không?**
A: Có. Output là của bạn. Skill chỉ là công cụ.

## Demo example

Xem `examples/mai-coach/` — một run đầy đủ với persona "Linh — coach 1-1 muốn launch cohort":

- `profile.json` — 8 jobs, 8 pains, 8 gains, 13 verbatim quotes, observed_pct 70%
- `insights.json` — 10 insights spanning 6 archetypes
- `hooks.json` — 30 hooks spanning 8 hook types
- `content.json` + `posts/` — 4 posts (1 awareness, 1 lead, 1 sale, 1 reels)

Mở `posts/post_001_hot_take.md` để xem ví dụ Hot Take awareness post điển hình.

## Status

**v1.0** — foundation + templates + scripts + niche pack (coach personal brand) + 1 full example.

**Roadmap v1.1** (tương lai):
- Niche packs cho beauty creator, mom & baby, F&B, real-estate
- TikTok script format
- English output
- Editorial pass Opus 4.7 cho `pro` mode (hiện đã có schema, chưa wire vào prompt)