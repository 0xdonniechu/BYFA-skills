# bto-skills

**Bộ công cụ AI Agent Skills thực chiến dành cho Claude Code, Cursor và autonomous AI agents.**

Một skill là một tệp hướng dẫn agent tự đọc và kích hoạt khi gặp đúng bối cảnh công việc. Bạn không cần phải nhớ quy trình thủ công hay dán đi dán lại prompt mỗi lần thao tác — agent tự nhận diện ngữ cảnh, nạp hướng dẫn và thi hành chuẩn xác.

Toàn bộ nguyên tắc được chắt lọc từ kinh nghiệm vận hành thực tế: kiểm soát bí mật, nghiên cứu thị trường có đối chiếu nguồn tin, bóc tách sản phẩm, quản trị vòng đời mã nguồn và điều phối đội ngũ multi-agent.

---

## Danh mục Skills

| Skill | Chức năng & Bối cảnh sử dụng |
|---|---|
| `/bto-researchmarket` | Nghiên cứu thị trường sâu, xác minh dữ liệu 3 tầng (`[CONFIRMED]`, `[SECONDARY]`, `[VENDOR-CLAIMED]`), đào review 1★/2★ tìm content wedge, tính toán TAM/SAM/SOM bằng chuỗi số học, lập Sales Battlecard và đóng gói Case Study chuẩn xác |
| `/bto-teardown` | Phân rã sản phẩm đối thủ: core features, pricing model, tech stack và luồng trải nghiệm người dùng theo phương pháp clean-room |
| `/bto-secrets` | Bảo vệ thông tin nhạy cảm: rà soát API key, `.env`, tokens và thông tin xác thực trước khi commit/push |
| `/bto-sdlc` | Quy trình phát triển phần mềm chuẩn mực: spec trước, code sau, phân đoạn rõ ràng cho feature lớn và refactor |
| `/bto-agent-team` | Điều phối multi-agent: duyệt một lần chạy tới xong (build → review độc lập → fix → merge → verify) qua nhiều wave |
| `/bto-whats-next` | Tổng kết cuối phiên làm việc: rà soát việc dở dang, đề xuất bước đi tiếp theo và ghi nhận tiến độ |
| `/bto-page-quality` | Đánh giá chất lượng trang: tốc độ tải, Core Web Vitals, độ tin cậy giao diện sau launch |
| `/bto-optimize-mac` | Dọn dẹp ổ đĩa, tối ưu RAM và môi trường phát triển trên macOS an toàn |
| `/bto-event-review` | Tổng hợp và biên tập nội dung chuyên sâu từ slides, hội thảo và transcripts |
| `/bto-posthog` | Cấu hình analytics chuẩn mực với PostHog: đo lường chuyển đổi và hiển thị dashboard dữ liệu rõ ràng |
| `/bto-create-skill` | Bộ khung tiêu chuẩn giúp tự tạo mới hoặc tùy biến skill theo nhu cầu của riêng bạn |

---

## Hướng dẫn cài đặt

### Dành cho Claude Code

Chạy lệnh tự động cài đặt toàn bộ skills:

```bash
git clone https://github.com/0xdonniechu/bto-skills.git ~/.claude/skills/bto-skills
~/.claude/skills/bto-skills/setup
```

Hoặc chỉ cài đặt một skill cụ thể (ví dụ: `bto-researchmarket`):

```bash
mkdir -p ~/.claude/skills/bto-researchmarket
curl -o ~/.claude/skills/bto-researchmarket/SKILL.md \
  https://raw.githubusercontent.com/0xdonniechu/bto-skills/main/bto-researchmarket/SKILL.md
```

### Dành cho Cursor & Agents khác

Tham khảo hướng dẫn chi tiết tại [HUONG-DAN-HOC-VIEN.md](HUONG-DAN-HOC-VIEN.md).

---

## Kiểm tra sau cài đặt

Mở phiên làm việc mới với agent và thử nghiệm bằng các câu lệnh:

```
Tôi sắp nghiên cứu thị trường này để đánh giá đối thủ — dùng quy trình nào?
Tôi sắp build feature mới — có quy trình spec trước code không?
Giờ làm gì tiếp theo trong session này?
```

Khi agent tự động nạp framework tương ứng (yêu cầu phân loại nguồn, lập spec trước khi code hoặc kiểm tra việc dở dang), skill đã kích hoạt thành công.

---

## Nguyên tắc cốt lõi

1. **Thực chứng hơn giả định**: Mọi số liệu phải có nguồn gốc rõ ràng hoặc tự tính toán minh bạch.
2. **Agent hỗ trợ, con người ra quyết định**: Skill giúp agent ghi nhớ quy tắc và giữ kỷ luật thực thi; quyết định cuối cùng và phê duyệt luôn thuộc về bạn.
3. **Liên tục tối ưu**: Mỗi skill được thiết kế để tự cải tiến qua các phiên làm việc và đóng góp thực tế. Xem thêm tại [CONTRIBUTING.md](CONTRIBUTING.md).
