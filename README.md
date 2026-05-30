# Học phần - Trực quan hoá dữ liệu

## Đề tài - Phân tích dữ liệu bán hàng thương mại điện tử

### Phân tích - Trực quan hoá dữ liệu

### Dự đoán khu vực có quy mô mở rộng doanh nghiệp

### 1. Tổng quan về tập dữ liệu

Số lượng bản ghi (Records): 9,994 dòng (tương ứng với 9,994 mặt hàng trong các đơn hàng).

Ý nghĩa chung: Tập dữ liệu mô tả các giao dịch bán hàng trực tuyến của một doanh nghiệp bán lẻ tại Mỹ. Nó ghi lại toàn bộ vòng đời của một đơn hàng từ lúc khách hàng đặt mua, hình thức vận chuyển, thông tin khách hàng, vị trí địa lý, cho đến chi tiết sản phẩm, doanh thu và lợi nhuận thu về.

1. Phân tích chi tiết các trường (Cột) dữ liệu

| STT | Tên trường (Column) | Kiểu dữ liệu        | Số record NaN | Ý nghĩa trong chủ đề                                                                                                                             | Thương mại điện tử                                                                      |
| --- | ------------------- | ------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| 1   | Row ID              | Số nguyên (Integer) | 0             | Số thứ tự của dòng dữ liệu (Dùng để định danh duy nhất mỗi hàng).                                                                                | Định danh duy nhất (khóa chính)                                                         |
| 2   | Order ID            | Chuỗi (String)      | 0             | Mã đơn hàng. Một đơn hàng có thể chứa nhiều sản phẩm khác nhau (chung một Mã đơn hàng nhưng khác dòng).                                          |
| 3   | Order Date          | Ngày tháng (Date)   | 0             | Ngày đặt hàng. Quan trọng để phân tích doanh thu theo thời gian (mùa vụ, xu hướng tăng trưởng).                                                  |
| 4   | Ship Date           | Ngày tháng (Date)   | 0             | Ngày giao hàng. Dùng kết hợp với Order Date để tính toán thời gian xử lý và giao hàng (Logistics).                                               |
| 5   | Ship Mode           | Chuỗi (String)      | 0             | Hình thức vận chuyển (Ví dụ: Standard Class, Second Class, Same Day). Ảnh hưởng trực tiếp đến chi phí và sự hài lòng của khách hàng.             |
| 6   | Customer ID         | Chuỗi (String)      | 0             | Mã khách hàng. Dùng để phân tích hành vi mua sắm, lòng trung thành và tần suất quay lại của khách.                                               |
| 7   | Customer Name       | Chuỗi (String)      | 0             | Tên khách hàng.                                                                                                                                  |
| 8   | Segment             | Chuỗi (String)      | 0             | Phân khúc khách hàng (Consumer: Cá nhân, Corporate: Doanh nghiệp, Home Office: Văn phòng nhỏ). Giúp doanh nghiệp định hình chiến lược marketing. |
| 9   | Country             | Chuỗi (String)      | 0             | Quốc gia (Trong tập này chủ yếu là United States).                                                                                               |
| 10  | City                | Chuỗi (String)      | 0             | Thành phố nơi khách hàng đặt hàng.                                                                                                               |
| 11  | State               | Chuỗi (String)      | 0             | Bang/Tỉnh nơi nhận hàng.                                                                                                                         |
| 12  | Postal Code         | Số (Numeric/String) | 0             | hoặc rất ít                                                                                                                                      | \*Mã bưu điện. Giúp định vị chính xác vị trí địa lý để tối ưu hóa kho bãi và logistics. |
| 13  | Region              | Chuỗi (String)      | 0             | Vùng miền (South, West, Central, East). Giúp so sánh hiệu suất kinh doanh giữa các khu vực địa lý lớn.                                           |
| 14  | Product ID          | Chuỗi (String)      | 0             | Mã sản phẩm. Định danh duy nhất cho từng mặt hàng trong kho.                                                                                     |
| 15  | Category            | Chuỗi (String)      | 0             | Danh mục sản phẩm lớn (Furniture: Nội thất, Office Supplies: Văn phòng phẩm, Technology: Công nghệ).                                             |
| 16  | Sub-Category        | Chuỗi (String)      | 0             | Danh mục phụ (Ví dụ: Chairs, Phones, Paper). Giúp phân tích sâu hơn mặt hàng nào đang sinh lời tốt.                                              |
| 17  | Product Name        | Chuỗi (String)      | 0             | Tên chi tiết của sản phẩm.                                                                                                                       |
| 18  | Sales               | Số thực (Float)     | 0             | Doanh số/Doanh thu thu được từ việc bán sản phẩm đó trong đơn hàng (Giá sau khi đã áp chiết khấu).                                               |
| 19  | Quantity            | Số nguyên (Integer) | 0             | Số lượng sản phẩm mà khách hàng mua trong đơn hàng đó.                                                                                           |
| 20  | Discount            | Số thực (Float)     | 0             | Tỷ lệ chiết khấu/giảm giá (Ví dụ: 0.2 nghĩa là giảm 20%). Dùng để đánh giá xem chiến lược giảm giá có thực sự kích cầu hiệu quả không.           |
| 21  | Profit              | Số thực (Float)     | 0             | Lợi nhuận ròng thu về từ sản phẩm đó. Có thể âm (lỗ) hoặc dương (lời). Đây là chỉ số cốt lõi để đánh giá sức khỏe kinh doanh.                    |
