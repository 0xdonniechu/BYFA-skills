# Đóng góp vào byfa-skills

Skill là tài liệu sống. Bạn dùng nó, thấy nó thiếu hoặc sai, sửa nó, thì
người sau đỡ vấp đúng chỗ bạn vừa vấp. Đó là toàn bộ vòng đời của repo này.

## Cách đóng góp, bốn bước

```bash
# 1. Fork repo này trên GitHub (nút Fork góc phải), rồi clone bản fork về
git clone https://github.com/<tên-bạn>/BYFA-skills.git
cd BYFA-skills

# 2. Tạo branch, sửa đúng file SKILL.md liên quan
git checkout -b fix/ten-ngan-gon

# 3. Commit với mô tả VÌ SAO sửa, không chỉ sửa cái gì
git add <file> && git commit -m "fix: ..."
git push -u origin fix/ten-ngan-gon

# 4. Mở pull request về 0xdonniechu/BYFA-skills, mô tả bằng tiếng Việt
```

Chưa quen git thì mở một issue kể lại chuyện bạn gặp, thế cũng là đóng góp.
Hoặc bảo agent của bạn: "fork 0xdonniechu/BYFA-skills, sửa chỗ X, mở PR giúp tôi".

## Luật cho một đóng góp được nhận

1. **Mỗi luật mới phải kèm một chuyện hỏng thật.** Bạn vấp ở đâu, mất bao
   lâu, sửa thế nào. Luật không có chuyện đứng sau là lý thuyết, sẽ không
   được nhận. Toàn bộ repo này viết theo nguyên tắc đó.
2. **Viết tiếng Việt, thuật ngữ kỹ thuật giữ nguyên tiếng Anh.** `webhook`
   là webhook, không phải "móc nối web".
3. **Không key, không secret, không dữ liệu người thật, không đường dẫn máy
   cá nhân** trong bất kỳ file nào.
4. **Tên skill mới theo dạng `bto-<english-name>`** (ngoại lệ dùng chung đã có là `market-research`), một folder một
   `SKILL.md`, chạy được ngay sau khi symlink.
5. Đề xuất đổi hẳn một quy trình thì mở issue bàn trước, đừng gửi thẳng một
   PR viết lại cả file.

## Kẹt thì hỏi ở đâu

- **cộng đồng nhà phát triển**: kênh `hỏi-đáp`, member trong chương trình là
  nguồn trợ giúp nhanh nhất, phần lớn vấn đề đã có người vấp trước bạn.
- **GitHub Issues** của repo này: cho lỗi trong chính skill.
- **Sơn Piaz**: [github.com/0xdonniechu](https://github.com/0xdonniechu), người viết
  bản gốc các skill này.

Chưa vào chương trình mà muốn học full phương pháp đứng sau các skill:
[github.com/0xdonniechu/BYFA-skills](https://github.com/0xdonniechu/BYFA-skills).
