# Học phần: Trực quan hóa dữ liệu

# Đề tài: Phân tích dữ liệu bán hàng thương mại điện tử

## Phân tích và trực quan hóa dữ liệu

## Dự đoán khu vực có tiềm năng mở rộng kinh doanh

### 1. Tổng quan về tập dữ liệu

- **Số lượng bản ghi (Records):** 9.994 dòng (tương ứng với 9.994 mặt hàng trong các đơn hàng).
- **Ý nghĩa chung:** Tập dữ liệu mô tả các giao dịch bán hàng trực tuyến của một doanh nghiệp bán lẻ tại Hoa Kỳ. Dữ liệu ghi lại toàn bộ vòng đời của một đơn hàng, từ thời điểm khách hàng đặt mua, hình thức vận chuyển, thông tin khách hàng, vị trí địa lý, đến chi tiết sản phẩm, doanh thu và lợi nhuận thu được.

### 1.1. Phân tích chi tiết các trường dữ liệu

| STT | Tên trường (Column) | Kiểu dữ liệu                   | Số bản ghi NaN | Ý nghĩa trong thương mại điện tử                                                                                                          |
| --- | ------------------- | ------------------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Row ID              | Số nguyên (Integer)            | 0              | Số thứ tự của dòng dữ liệu, dùng để định danh duy nhất mỗi bản ghi (khóa chính).                                                          |
| 2   | Order ID            | Chuỗi (String)                 | 0              | Mã đơn hàng. Một đơn hàng có thể chứa nhiều sản phẩm khác nhau nên nhiều dòng có thể cùng một mã đơn hàng.                                |
| 3   | Order Date          | Ngày tháng (Date)              | 0              | Ngày đặt hàng. Quan trọng trong việc phân tích doanh thu theo thời gian, mùa vụ và xu hướng tăng trưởng.                                  |
| 4   | Ship Date           | Ngày tháng (Date)              | 0              | Ngày giao hàng. Kết hợp với Order Date để tính thời gian xử lý và giao hàng.                                                              |
| 5   | Ship Mode           | Chuỗi (String)                 | 0              | Hình thức vận chuyển (ví dụ: Standard Class, Second Class, Same Day). Ảnh hưởng đến chi phí vận chuyển và mức độ hài lòng của khách hàng. |
| 6   | Customer ID         | Chuỗi (String)                 | 0              | Mã khách hàng. Dùng để phân tích hành vi mua sắm, mức độ trung thành và tần suất mua hàng.                                                |
| 7   | Customer Name       | Chuỗi (String)                 | 0              | Tên khách hàng.                                                                                                                           |
| 8   | Segment             | Chuỗi (String)                 | 0              | Phân khúc khách hàng (Consumer, Corporate, Home Office). Hỗ trợ xây dựng chiến lược marketing phù hợp.                                    |
| 9   | Country             | Chuỗi (String)                 | 0              | Quốc gia của khách hàng (trong tập dữ liệu này chủ yếu là United States).                                                                 |
| 10  | City                | Chuỗi (String)                 | 0              | Thành phố nơi khách hàng đặt hàng.                                                                                                        |
| 11  | State               | Chuỗi (String)                 | 0              | Bang hoặc tiểu bang nơi nhận hàng.                                                                                                        |
| 12  | Postal Code         | Số hoặc Chuỗi (Numeric/String) | 0 hoặc rất ít  | Mã bưu điện, giúp xác định vị trí địa lý chính xác để tối ưu hóa logistics và kho bãi.                                                    |
| 13  | Region              | Chuỗi (String)                 | 0              | Khu vực địa lý (South, West, Central, East). Dùng để so sánh hiệu quả kinh doanh giữa các vùng.                                           |
| 14  | Product ID          | Chuỗi (String)                 | 0              | Mã sản phẩm, dùng để định danh duy nhất từng mặt hàng.                                                                                    |
| 15  | Category            | Chuỗi (String)                 | 0              | Danh mục sản phẩm chính (Furniture, Office Supplies, Technology).                                                                         |
| 16  | Sub-Category        | Chuỗi (String)                 | 0              | Danh mục phụ (ví dụ: Chairs, Phones, Paper), hỗ trợ phân tích chi tiết hiệu quả từng nhóm sản phẩm.                                       |
| 17  | Product Name        | Chuỗi (String)                 | 0              | Tên chi tiết của sản phẩm.                                                                                                                |
| 18  | Sales               | Số thực (Float)                | 0              | Doanh thu thu được từ sản phẩm trong đơn hàng (sau khi áp dụng chiết khấu).                                                               |
| 19  | Quantity            | Số nguyên (Integer)            | 0              | Số lượng sản phẩm được mua trong đơn hàng.                                                                                                |
| 20  | Discount            | Số thực (Float)                | 0              | Tỷ lệ chiết khấu hoặc giảm giá (ví dụ: 0.2 tương ứng với giảm 20%). Dùng để đánh giá hiệu quả của các chương trình khuyến mãi.            |
| 21  | Profit              | Số thực (Float)                | 0              | Lợi nhuận ròng thu được từ sản phẩm. Giá trị có thể âm (lỗ) hoặc dương (lãi). Đây là chỉ số quan trọng để đánh giá hiệu quả kinh doanh.   |

### Nhận xét

Tập dữ liệu cung cấp đầy đủ thông tin về:

- **Khách hàng** (Customer ID, Segment, City, State, Region).
- **Sản phẩm** (Category, Sub-Category, Product Name).
- **Đơn hàng và vận chuyển** (Order Date, Ship Date, Ship Mode).
- **Hiệu quả kinh doanh** (Sales, Quantity, Discount, Profit).

Đây là nguồn dữ liệu phù hợp để thực hiện các bài toán:

1. Phân tích doanh thu và lợi nhuận theo thời gian.
2. Đánh giá hiệu quả kinh doanh theo khu vực địa lý.
3. Phân tích hành vi mua sắm của khách hàng.
4. Xác định nhóm sản phẩm mang lại lợi nhuận cao.
5. Dự đoán khu vực tiềm năng để mở rộng hoạt động kinh doanh trong tương lai.
