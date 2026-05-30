import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Đọc dữ liệu
data_path = Path(__file__).resolve().parents[2] / 'data' / 'e-commerce_dataset.csv'
df = pd.read_csv(data_path, encoding='latin1')

# 1. Vẽ biểu đồ cột so sánh Lợi nhuận theo Danh mục sản phẩm
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Category', y='Profit', estimator=sum, errorbar=None, palette='Blues_d')
plt.title('Tổng Lợi Nhuận Theo Từng Danh Mục Lớn')
plt.show()

# 2. Vẽ Scatter Plot xem mối quan hệ giữa Giảm giá và Lợi nhuận
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', alpha=0.5)
plt.title('Mối Quan Hệ Giữa Mức Chiết Khấu Và Lợi Nhuận')
plt.show()