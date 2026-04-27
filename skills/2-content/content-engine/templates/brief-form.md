# Customer Profile Brief Form

> Form 20 câu để tạo `profile.json` khi không có fanpage để scrape. Buyer điền hoặc skill hỏi từng câu.
>
> **Quy tắc vàng:** ưu tiên trích lời nguyên văn của khách hàng thật (FB comment, IG DM, ghi chú phỏng vấn). Tránh viết "tổng hợp lại" — đó là nguồn gốc của profile generic.

---

## Section A — Persona cơ bản (Q1-4)

**Q1. Persona này là ai? Mô tả 1 câu.**
Ví dụ: "Mai — coach phát triển cá nhân, 32 tuổi, ex-HR manager FMCG, build personal brand 6 tháng, đang ở 3.2k follow IG, muốn launch cohort đầu tiên Q3-2026."

**Q2. Niche/identity họ tự gọi mình là gì?**
Ví dụ: "leadership coach", "mẹ bỉm làm content", "beauty creator", "designer freelance".

**Q3. Tuổi (band) + giai đoạn cuộc đời?**
Ví dụ: "26-30, mới sinh con thứ nhất 8 tháng" hoặc "30-35, mới nghỉ corporate 6 tháng".

**Q4. Khoảng thu nhập hiện tại (VND/tháng)?** (Bỏ qua nếu không biết)
Ví dụ: "under-15tr", "15-30tr", "30tr+".

---

## Section B — Hành vi platform (Q5-6)

**Q5. Platform chính + format ưu tiên?**
Ví dụ: "IG-first, reel + carousel, peak 21h-23h và 6h-7h sáng".

**Q6. Behavior trên platform?**
- `lurker` (ít comment, ít post)
- `commenter` (thường comment)
- `creator-active` (post 3+/tuần)

---

## Section C — Jobs (Q7-9)

> 3-7 việc khách đang cố làm. Mix functional / emotional / social.

**Q7. Functional jobs — task cụ thể họ đang cố hoàn thành (3-5)?**
Ví dụ: "launch khoá mini 1.5tr trong 60 ngày", "viết 4 reel/tuần".

**Q8. Emotional jobs — trạng thái cảm xúc họ muốn đạt (1-3)?**
Ví dụ: "hết áp lực phải hoàn hảo khi lên sóng", "tự tin khi nói về giá".

**Q9. Social jobs — cách họ muốn người khác nhìn họ (1-3)?**
Ví dụ: "được xem là chuyên gia thật, không phải reviewer kiếm hoa hồng".

---

## Section D — Pains (Q10-12)

> 5-10 nỗi đau. Mix obstacle / undesired_outcome / risk. **Mỗi pain phải có severity (mild/moderate/extreme) + frequency (rare/occasional/frequent/constant)**.

**Q10. Obstacles — rào cản chặn họ bắt đầu/làm xong (3-5)?**
Ví dụ: "chưa từng build curriculum, không biết chia bài bao nhiêu" — extreme + constant.

**Q11. Undesired outcomes — kết quả tệ họ đang gặp (2-4)?**
Ví dụ: "đăng 5 bài/tuần mà reach vẫn 200 view" — moderate + constant.

**Q12. Risks — sợ điều xấu xảy ra (1-3)?**
Ví dụ: "sợ launch flop, follower chỉ thích review chứ không bỏ tiền học" — extreme + frequent.

---

## Section E — Gains (Q13-15)

> 5-10 mong đợi. Phải đủ 4 level: required / expected / desired / unexpected.

**Q13. Required gains — không có thì offer fail (2-3)?**
Ví dụ: "framework rõ pricing + sales flow + lesson structure".

**Q14. Expected gains — mặc định mong có (2-3)?**
Ví dụ: "template caption + email launch sẵn dùng".

**Q15. Desired + Unexpected gains — kể ra mới nhớ + chưa nghĩ tới (1-3 mỗi loại)?**
Ví dụ desired: "network với creator đã launch thành công".
Ví dụ unexpected: "được mentor 1-1 review sales page trước launch".

---

## Section F — Voice & Vocabulary (Q16-19) — QUAN TRỌNG NHẤT

> Đây là dữ liệu giá trị nhất. **Yêu cầu nguyên văn — không paraphrase.**

**Q16. Self-labels — họ tự gọi mình là gì (≥2 examples)?**
Ví dụ: "đứa làm content", "mẹ bỉm side-hustle", "coach mới ra nghề".

**Q17. Repeated words — từ ngữ họ hay lặp lại (≥3 examples)?**
Ví dụ: "lú", "flop", "bấp bênh", "hoa hồng bèo", "tụt mood".

**Q18. Metaphors — cách họ ví von (≥1)?**
Ví dụ: "làm content như đẻ", "thuật toán như thời tiết", "đi trên dây".

**Q19. Verbatim quotes — câu nói nguyên văn (≥5 examples, bắt buộc)?**
Ví dụ:
- "em lú lắm chị, không biết chia 5 buổi hay 10 buổi"
- "lỡ mở khoá mà flop thì quê lắm"
- "affiliate hoa hồng bèo lắm chị"

> **Nếu không có ≥5 verbatim quote thật:** quay lại đào FB comments / IG DM / phỏng vấn 3 khách cũ. Đừng "tổng hợp lại" → sẽ ra profile generic.

---

## Section G — Evidence (Q20)

**Q20. Nguồn data — bạn lấy thông tin từ đâu?**
- `fb_insight_miner_run_id` (nếu có)
- `interview_count` — phỏng vấn 1-1 bao nhiêu khách thật?
- `dm_export_path` — IG/FB DM export?
- `survey_response_count`?
- Hoặc đánh dấu `assumed` nếu chỉ là giả thuyết — *flag để verify ASAP, không ship sang Stage 2*.

---

## Sau khi điền xong

Skill sẽ:
1. Parse câu trả lời → fill `profile.json` theo schema.
2. Tag mỗi entry với `confidence`: `observed` (Q19 verbatim hoặc Q20 source thật) / `inferred` (suy từ behavior) / `assumed` (giả thuyết).
3. Tính `evidence_summary.observed_pct`. Nếu < 60% → **block Stage 2**, yêu cầu bổ sung evidence.
4. Cross-check với `niche-packs/{niche}.json` (nếu có) để cảnh báo các trường thiếu.
