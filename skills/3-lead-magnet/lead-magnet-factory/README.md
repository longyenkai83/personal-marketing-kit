# Lead Magnet Factory Skill

Quick-start hướng dẫn (Vietnamese). Agent workflow end-to-end: ý tưởng → ebook lead magnet 9 trang dạng listicle → Canva-ready CSV.

## Đây là gì?

Một Claude Skill chạy trong Claude Code. Khi em gõ "làm lead magnet" hoặc "tạo ebook listicle", Claude tự động load skill này và orchestrate 7 pha:

1. **Research** thị trường qua Tavily MCP
2. **Chọn 12 items** theo scoring rubric
3. **Outline** theo schema
4. **Viết** theo style guide Marie Forleo (vi hoặc en)
5. **Biên tập** pass cuối (check AI-giveaway, lặp ý, word count)
6. **Visual brief** map ảnh hoặc sinh AI prompt
7. **Export** CSV + Markdown preview

Output: CSV upload vào Canva Bulk Create → 1 click ra PDF 9 trang.

## Cách gọi

Mở Claude Code trong bất kỳ folder nào, gõ:

```
Dùng skill lead-magnet-factory để làm ebook.
Niche: [niche của em]
Topic: [chủ đề cụ thể]
Audience: [ai đọc cái này]
CTA: [em bán gì]
Language: vi
```

Claude sẽ load skill, hỏi các input còn thiếu, rồi chạy 7 pha tự động.

## Setup 1 lần (trước lần chạy đầu)

### 1. Install dependency cho validation script

```bash
pip install jsonschema
```

Không bắt buộc — skill vẫn chạy nếu thiếu, chỉ mất phần schema validation.

### 2. Tạo Canva template (quan trọng nhất)

Mở `reference/canva_template_spec.md` — làm theo:
- Design 9-page template trong Canva Pro
- Dùng design tokens (lavender + cream + lime + coral) hoặc brand em
- Đặt placeholder text với tên **chính xác** như spec (ví dụ `{{cover_title_part1}}`)
- Connect text to data qua **Apps → Bulk Create**

Gợi ý tiết kiệm thời gian: commission designer Fiverr $100–150 cho template custom. Mua 1 lần dùng mãi.

### 3. Verify CSV ↔ template handshake

```bash
cd ~/.claude/skills/lead-magnet-factory
python scripts/to_canva_csv.py examples/sample_output.json /tmp/test.csv
```

Upload `/tmp/test.csv` vào Canva Bulk Create để test. Nếu field name không map đúng → rename trong Canva hoặc edit `to_canva_csv.py`.

## Workflow mỗi lần làm ebook (20 phút)

1. Prompt Claude với niche + topic + CTA (1 phút)
2. Claude chạy 7 pha (10–15 phút, em review ở Phase 2 và Phase 5)
3. Xuống `output/{slug}/canva_bulk.csv` (có đường dẫn trong output cuối)
4. Mở Canva template → Apps → Bulk Create → Upload CSV (2 phút)
5. Canva auto-generate 9 trang → em review + điều chỉnh ảnh (5 phút)
6. Export PDF → xong.

## Cấu trúc thư mục

```
lead-magnet-factory/
├── SKILL.md                    # Orchestration brain (Claude đọc khi invoke)
├── schema.json                 # Strict JSON contract
├── README.md                   # File này
├── reference/
│   ├── style_guide.md          # Voice Marie Forleo + adapt Vietnamese
│   └── canva_template_spec.md  # Placeholder spec cho Canva template
├── scripts/
│   ├── to_canva_csv.py         # JSON → Canva Bulk Create CSV
│   └── validate.py             # Quality gates (AI-giveaway, lặp ý, word count)
├── examples/
│   └── sample_output.json      # Ví dụ tiếng Việt hoàn chỉnh (12 sai lầm IG)
└── output/                     # Generated artifacts per ebook run
    └── {slug}/
        ├── research_raw.json
        ├── selection.md
        ├── content.json
        ├── visual_brief.md
        ├── canva_bulk.csv      # ← UPLOAD THIS TO CANVA
        └── preview.md          # ← REVIEW THIS
```

## Chi phí ước lượng

| Item | Chi phí |
|---|---|
| Claude API (Sonnet 4.6 + Opus 4.7 editorial) | ~$0.50–$1.00 / ebook |
| Tavily research | Free tier đủ (1000 credits/tháng) |
| Canva Pro (setup 1 lần, unlimited ebook) | ~380k VND/tháng |
| **Biên mỗi ebook sau setup** | **~25–50k VND** |

Setup 1 lần (template + photoshoot): 3–5 triệu VND.

## Commercial-grade safeguards

Skill đã có sẵn:
- Không bịa testimonial (placeholder buộc em điền thật)
- Không bịa statistics
- Không code-switch Việt-Anh trong body
- Không copy wording Marie Forleo — chỉ mượn cấu trúc template
- Disclaimer auto-inject nếu niche là health/finance/legal
- Traceability: research sources lưu trong `selection.md`

## Troubleshooting

**Claude không load skill khi gõ lệnh**
→ Verify path: `ls ~/.claude/skills/lead-magnet-factory/SKILL.md`. Restart Claude Code session.

**CSV upload vào Canva báo "field not found"**
→ Tên placeholder trong Canva template không match CSV column. Mở `reference/canva_template_spec.md` so sánh từng cái.

**Validate báo lỗi "too similar to item N"**
→ Phase 4 đã sinh 2 heading trùng ý. Re-run Phase 4 hoặc em edit thủ công trong `content.json` rồi re-validate.

**Tavily research quá ít kết quả**
→ Niche có thể quá ngách hoặc query keyword quá cụ thể. Bổ sung seed pain points thủ công khi Claude hỏi.

## Upgrade path (tương lai)

Skill hiện tại là **v1.0 MVP**. Có thể mở rộng:

- **v1.1**: Thêm Ideogram MCP để auto-gen infographic cho từng page
- **v1.2**: Thêm Gmail MCP draft sequence nurture sau khi lead opt-in
- **v1.3**: A/B test 3 title variants rồi em chọn
- **v2.0**: Port sang Agent SDK standalone app để chạy SaaS cho học viên em

Khi sẵn sàng upgrade, edit SKILL.md để thêm phase mới — architecture hiện tại chịu được extension.

## Tham khảo

- [Marie Forleo lead magnet PDF (file gốc em cung cấp)](../../../README.md) — reference cho style + layout
- [Claude Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Canva Bulk Create docs](https://www.canva.com/help/bulk-create/)
