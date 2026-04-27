# Canva Template Spec

This spec defines the **9-page Canva template** the user must create ONCE. The `to_canva_csv.py` script outputs rows keyed to these exact placeholder names. Mismatched names = broken Bulk Create.

## How Canva Bulk Create works

1. Design your template in Canva Pro.
2. Place text where dynamic content should go.
3. Right-click text → **Connect to data** (or "Bulk Create" in Apps) → name the field.
4. Upload CSV where column headers = the field names you chose.
5. Canva generates one design per row — for this skill, ONE row = ONE complete ebook (all 9 pages populated).

## Required placeholder names (exact, case-sensitive)

### Page 1 — Cover
| Placeholder | Source JSON path | Notes |
|---|---|---|
| `cover_title_part1` | `cover.title_full` — split before first highlight word | Plain text |
| `cover_title_highlight` | `cover.title_highlight_words[0]` | Apply pill-highlight style in Canva |
| `cover_title_part2` | remainder of title after highlight word | Plain text |
| `cover_subtitle` | `cover.subtitle` | Optional — hide in template if empty |
| `author_name` | `metadata.author_name` | Top of cover |

### Page 2 — Intro
| Placeholder | Source JSON path |
|---|---|
| `intro_hook_title` | `intro.hook_title` |
| `intro_body_1` | `intro.body_paragraphs[0]` |
| `intro_body_2` | `intro.body_paragraphs[1]` |
| `intro_body_3` | `intro.body_paragraphs[2]` (optional) |
| `intro_cta_line` | `intro.cta_line` (styled as handwriting accent) |
| `intro_cta_summary` | `intro.cta_summary` |

### Page 3 — Items 1–4
| Placeholder | Source |
|---|---|
| `item_1_number` | `items[0].number` |
| `item_1_heading` | `items[0].heading` |
| `item_1_body_1` | `items[0].body_paragraphs[0]` |
| `item_1_body_2` | `items[0].body_paragraphs[1]` |
| `item_2_number` through `item_4_body_2` | same pattern |

### Page 4 — Items 5–7
| Placeholder | Source |
|---|---|
| `item_5_number` through `item_7_body_2` | same pattern |

### Page 5 — Items 8–10
| Placeholder | Source |
|---|---|
| `item_8_number` through `item_10_body_2` | same pattern |

### Page 6 — Items 11–12
| Placeholder | Source |
|---|---|
| `item_11_number` through `item_12_body_2` | same pattern |

*Note: pages 3–6 split depends on your visual density. Adjust if you prefer 2+4+4+2 or 3+3+3+3 — just keep placeholder names `item_1_*` through `item_12_*`.*

### Page 7 — Offer
| Placeholder | Source |
|---|---|
| `offer_header` | `offer_page.header` |
| `offer_title_part1` | split similar to cover |
| `offer_title_highlight` | `offer_page.title_highlight_words[0]` |
| `offer_title_part2` | remainder |
| `offer_description` | `offer_page.description` |
| `benefit_1_emoji` | `offer_page.benefits[0].emoji` |
| `benefit_1_title` | `offer_page.benefits[0].title` |
| `benefit_1_desc` | `offer_page.benefits[0].description` |
| `benefit_2_*`, `benefit_3_*` | same pattern |
| `offer_cta_button` | `offer_page.cta_button` |
| `offer_closer` | `offer_page.description` last sentence (optional) |

### Page 8 — Testimonials
| Placeholder | Source |
|---|---|
| `testimonial_1_name` | `testimonials[0].name` |
| `testimonial_1_role` | `testimonials[0].role` |
| `testimonial_1_quote` | `testimonials[0].quote` |
| `testimonial_2_*` through `testimonial_5_*` | same pattern |

### Page 9 — Closing
| Placeholder | Source |
|---|---|
| `closing_title_part1` | split before highlight |
| `closing_title_highlight` | a word from title (e.g., "Different") |
| `closing_title_part2` | remainder |
| `closing_intro_line` | `closing_page.intro_line` |
| `diff_1_emoji` | `closing_page.differentiators[0].emoji` |
| `diff_1_title` | `closing_page.differentiators[0].title` |
| `diff_1_desc` | `closing_page.differentiators[0].description` |
| `diff_2_*` through `diff_4_*` | same pattern |
| `closing_final_hook` | `closing_page.final_hook` |
| `closing_cta_button` | `closing_page.cta_button` |
| `closing_tagline` | `closing_page.closing_tagline` |
| `closing_signature` | `closing_page.signature_line` |

## Design tokens (Marie Forleo reference)

| Token | Hex | Usage |
|---|---|---|
| `--bg-primary` | `#7C7AE8` | Page background (lavender/purple) |
| `--bg-secondary` | `#F3F0E8` | Intro page background (warm cream) |
| `--accent-lime` | `#D5F26A` | Stroke around portrait figures, page footer band |
| `--accent-coral` | `#F48A6F` | Pill-highlight on title words, CTA button |
| `--text-dark` | `#1F1F1F` | Body text |
| `--text-light` | `#FFFFFF` | Text on purple background |
| `--card-bg` | `#F9F5EB` | Rounded card containers for item text |

## Typography (suggestions, adjust to brand)

- **Display (titles)**: bold sans-serif with wide letterspacing — e.g., Mona Sans Bold, Gilroy Black, Integral CF
- **Serif accent (hook titles)**: e.g., Playfair Display, Canela
- **Handwriting accent**: e.g., Caveat, Homemade Apple — for "here's where it all starts:" and signature
- **Body**: clean sans-serif, 11–13pt — e.g., Inter, Mona Sans Regular

## Visual treatments

- **Portrait photo**: apply lime stroke outline (offset shape behind figure in accent-lime color)
- **Title highlight**: coral rounded-pill behind selected words (Canva: "Highlight text" effect)
- **Numbered circles**: 1.5–2rem circle with coral outline, number in coral italic serif
- **Emoji pills**: rounded rectangle card with emoji + title stacked, on card-bg color
- **Testimonial cards**: rounded rectangle on card-bg, 5-star row, avatar circle, name + role + quote

## Where to get a starter template

Options (in order of effort):
1. **Build from scratch in Canva Pro** using these tokens (2–4 hours, one time)
2. **Canva Marketplace**: search "12 tips lead magnet" or "ebook listicle" — pick one closest, customize colors
3. **Creative Market / Etsy**: search "ebook Canva template" — ~$10–30, often more polished
4. **Commission a designer** on Fiverr: ~$50–150 for custom match to brand

**Recommendation for commercial use**: commission once ($100–150), own it forever. Custom template = instantly distinguishable from every other AI-generated ebook.

## Template-CSV handshake test

Before first real run:
1. Export this skill's sample: `python scripts/to_canva_csv.py examples/sample_output.json /tmp/test.csv`
2. In Canva: Apps → Bulk Create → Upload CSV
3. Verify all placeholders map correctly
4. If any mismatch → rename Canva fields OR edit `to_canva_csv.py` column names

Do this test ONCE when setting up the template. After that, every ebook Just Works.
