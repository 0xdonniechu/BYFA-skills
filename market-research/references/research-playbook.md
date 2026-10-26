# Market research playbook

Mở file này cho research sâu. Chọn các phần phù hợp với câu hỏi; không biến checklist thành mục tiêu tự thân.

## 1. Câu hỏi và phạm vi

Trước khi tìm, ghi:

> Tôi cần biết **[điều gì]** về **[phân khúc/thị trường/đối tượng]** để quyết định **[hành động]**.

Nêu thời điểm chốt, địa lý, ICP, kênh, ngôn ngữ, loại khách hàng, tiền tệ, time horizon và giới hạn evidence. Nếu người dùng hỏi một đối thủ, không tự mở rộng thành market census; nếu hỏi toàn thị trường, không dừng ở danh sách hãng nổi bật.

## 2. Nguồn và độ tin cậy

| Loại evidence | Ví dụ | Cách dùng |
|---|---|---|
| Primary record/data | cơ quan nhà nước, filing, pricing/help center, investor/company release, API gốc | Chỉ xác nhận đúng trường dữ liệu hoặc claim mà trang ghi. Filing xác nhận issuer đã nộp lời khai, không tự xác nhận lời khai đúng. |
| Secondary | báo chí, analyst/database, investor portfolio, review platform | Ghi rõ tác giả, methodology/date và lợi ích có thể ảnh hưởng. Tìm nguồn gốc nếu có. |
| Vendor claim | trang chủ, sales copy, founder quote, product demo | Gắn `[VENDOR-CLAIMED]`; không gọi là kết quả độc lập. |
| Derived / scenario | phép tính từ đầu vào đã trích, mô hình sizing | In công thức, input labels, giả định và phạm vi; gắn `[INFERENCE]` hoặc `[ASSUMPTION]`. |

Ưu tiên ngày phát hành và “last updated” thay vì chỉ ngày truy cập. Khi nguồn mâu thuẫn, trình bày hai phiên bản và giải thích vì sao chọn/không chọn; đừng âm thầm lấy số thuận cho thesis.
GitHub-specific facts such as stars, license, default branch and last push belong to the GitHub API/repository itself, not a blog post or copied profile.
Ghi nhận lợi ích của nguồn, selection/survivorship bias và khả năng nhiều bài chỉ sao chép cùng một nguồn gốc. Chủ động tìm evidence phản chứng và lời giải thích thay thế; nhiều bài lặp lại một claim không thành nhiều xác nhận độc lập.

## 3. Song song hóa có kiểm soát

Dùng tối đa 2–3 luồng độc lập khi tác vụ rộng và công cụ delegation sẵn có:

1. Competitor/product/pricing: nguồn gốc và packaging.
2. Customer evidence: review, forum, community; cả tích cực và tiêu cực.
3. Market/funding/finance: định nghĩa thị trường, dữ liệu chính thức, round/funding/traction.

Mỗi brief phải có cùng câu hỏi, scope, ngày chốt, mẫu cần trả về và hợp đồng evidence: URL gốc, ngày truy cập, nhãn, phép tính/định nghĩa, bất đồng và unknown. Không yêu cầu agent đoán từ summary. Người tổng hợp tự mở lại ít nhất một claim quan trọng ở mỗi luồng hoặc mọi claim có thể đổi kết luận. Nếu chưa có delegation, chạy các luồng lần lượt và ghi rõ limitation.

## 4. Competitor research

Xây longlist từ nhiều truy vấn và danh mục khác nhau, sau đó phân loại:

- **Direct:** cùng buyer/job và thay thế phần lớn workflow.
- **Adjacent:** trùng một phần workflow hoặc buyer.
- **Substitute:** dịch vụ, agent tự dựng, agency, spreadsheet hoặc quy trình thủ công.

Nêu quy tắc đưa vào shortlist và những nhóm còn thiếu. Đối chiếu trang pricing, product docs, integration, permissions và limits. Ghi chu kỳ thanh toán, số account/channel/brand/user, credit/token, giới hạn dùng, media spend, phí theo spend, onboarding và add-on. Không quy đổi token/credit thành đơn vị tương đương nếu không biết tỷ lệ tiêu hao.

Ma trận capability chỉ mã hóa bằng chứng được mô tả: `C` rõ, `P` một phần/điều kiện/phụ thuộc người hoặc bên ngoài, `?` không tìm thấy evidence đủ. Kèm nguồn trong từng row hoặc cột. Không lấy feature list từ đối thủ làm phán quyết cuối.

Battlecard chỉ khi cần bán hàng/định vị:

| Mục | Bằng chứng cần có |
|---|---|
| Persona và pitch | Persona theo nguồn, lời hứa gắn nhãn vendor claim |
| Giá/package | chu kỳ, giới hạn, khoản phát sinh, thiết lập |
| Claim và trải nghiệm | claim đối chiếu với docs/review/test; không xem review là fact |
| Risk/weakness | pattern có nhiều evidence, mẫu và phản chứng; unknown không phải flaw |
| Wedge to test | khác biệt có thể kiểm chứng, chưa gọi là “kill shot” |
| Objection response | trả lời chính xác bằng chức năng có evidence, không hạ thấp đối thủ |

## 5. Customer/review evidence

Nếu có review phù hợp, lấy cả 1★/2★ lẫn 4★/5★. Ghi platform, rating, tổng mẫu, kỳ review, ngày, invitation/verification markers nếu có. Review là self-selected report; không khẳng định nguyên nhân, chính sách hoặc lỗi đã được xác minh. Trích ngắn, ưu tiên paraphrase và link trực tiếp. Phân biệt review về sản phẩm cụ thể với toàn suite/agency/support.

## 6. TAM / SAM / SOM

Dùng khi quyết định market entry, pricing, build-for-sale hoặc khi người dùng yêu cầu sizing. Có thể trình bày model proxy thay vì tuyên bố “thị trường trị giá”:

```text
TAM = số account có nhu cầu theo định nghĩa × annual spend/revenue phù hợp
SAM = TAM accounts × share đúng ICP/địa lý/kênh/ngôn ngữ/khả năng phục vụ
SOM = SAM accounts × share tiếp cận/chuyển đổi khả thi trong time horizon
```

Tách count khỏi value. Nêu nguồn cho customer count và annual price/spend; không trộn advertiser count với số doanh nghiệp, ngân sách quảng cáo với phần mềm, hoặc survey share với toàn bộ population nếu định nghĩa không khớp. SAM/SOM percentages phải là `[ASSUMPTION]` hoặc đo từ pipeline/capacity; đưa low/base/high scenario và sensitivity. Kiểm tra bottom-up bằng sales capacity, conversion, ACV và chu kỳ bán. Nếu missing denominator/material input, để range/unknown và nói cần dữ liệu nào; không điền số để hoàn thành bảng.

## 7. Funding, revenue, valuation

Dùng bảng có entity, currency, amount, round/filing/status, date, source class, valuation status và caveat. Tách funding amount khỏi valuation; một round funding không tiết lộ valuation nếu nguồn không nói. Tách market cap (public shares × price at timestamp), private-round valuation, asking price, modeled EV, revenue, ARR/MRR, GMV và total funding. Đừng gán pháp nhân cùng tên cho cùng một sản phẩm nếu chưa chứng minh.

Với TrustMRR hoặc payment-connected services: ghi exact page metric, `data updated` timestamp, access date, active subscription definition và trạng thái connection/staleness. Nói rõ đó là dữ liệu account được kết nối, có thể đổi và không đại diện tự động cho consolidated/audited revenue hoặc profit.

Không suy private-company valuation từ ARR/MRR multiple trừ khi người dùng yêu cầu scenario; nếu làm, gọi là sensitivity model, nêu multiple là assumption và không gọi là observed valuation.

## 8. Investor / fund diligence

Tùy câu hỏi, ghi fund size, vintage, stage, typical check, geography, thesis, relevant portfolio, recent activity, source date và fit/mismatch. Xác minh facts qua fund/company/filing; database profiles là secondary. Phân biệt public thesis với khả năng đầu tư thực tế. Không suy ra current dry powder/check availability từ portfolio cũ.

## 9. Vendor / technology research

Ghi chức năng thực tế, integration/permission, data flow, dependency, lock-in, pricing basis, security/compliance claims và operational cost. Yêu cầu security/compliance certification phải kiểm tra issuer/certificate scope và ngày. Chưa thử thì nói “theo tài liệu”, không viết như kết quả test. Không gửi dữ liệu người dùng vào vendor để “thử” nếu chưa được cho phép.

## 10. Gói báo cáo

Chọn đúng phần, viết bằng ngôn ngữ người dùng nếu họ không yêu cầu khác; report sâu thường có:

1. Câu hỏi quyết định, phạm vi, ngày chốt.
2. Kết luận / lựa chọn có điều kiện.
3. Phân nhóm thị trường và ma trận so sánh.
4. Pricing / packaging.
5. Customer evidence và phản chứng.
6. Market sizing model khi phù hợp.
7. Funding, revenue, valuation khi liên quan.
8. Risk, data gaps, numbers rejected.
9. Phương pháp, nguồn và ngày truy cập.
10. Next step / thí nghiệm; không tuyên bố outcome chưa đo.

Nếu người dùng muốn proof-based case study, chỉ dùng kết quả thật có thể xác minh: snapshot; baseline; cách triển khai; quantified result; trích dẫn có thể kiểm chứng; takeaway. Thiếu dữ liệu thì không dựng quote, baseline hoặc ROI.

Với research thị trường đáng kể, tạo HTML có thể mở trực tiếp trên web và gửi URL đã kiểm tra. Ưu tiên hosting sẵn có trong repo/dự án được người dùng cho phép; giữ biểu đồ, số liệu, bảng và nguồn đồng nhất với báo cáo. Không công khai nghiên cứu nhạy cảm hoặc tạo tài khoản hosting mới; nếu chưa có nơi lưu trữ được phép, bàn giao HTML cục bộ và nêu rõ điều kiện còn thiếu để có link web.
