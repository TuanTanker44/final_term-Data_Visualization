from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load dataset
# =========================
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR.parent.parent / "data" / "e-commerce_dataset.csv"
df = pd.read_csv(csv_path, encoding="latin1")

# =========================
# Process datetime
# =========================
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Feature Engineering
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Weekday"] = df["Order Date"].dt.day_name()

# =========================
# Aggregate orders by month
# =========================
monthly_orders = (
    df.groupby(["Year", "Month"])
    .size()
    .reset_index(name="Orders")
)

monthly_orders["Date"] = pd.to_datetime(
    monthly_orders["Year"].astype(str)
    + "-"
    + monthly_orders["Month"].astype(str)
    + "-01"
)

# =========================
# Top cities
# =========================
top_cities = (
    df.groupby("City")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

# =========================
# Region distribution
# =========================
region_orders = df.groupby("Region").size()

# =========================
# Shipping duration
# =========================
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# =========================
# Create output folder
# =========================
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# =========================
# Save charts
# =========================
chart1 = output_dir / "monthly_orders.png"
chart2 = output_dir / "top_cities.png"
chart3 = output_dir / "region_distribution.png"

# ===== Chart 1 =====
plt.figure(figsize=(10, 5))
plt.plot(monthly_orders["Date"], monthly_orders["Orders"])
plt.xticks(rotation=45)
plt.title("Monthly Orders Trend")
plt.xlabel("Time")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(chart1)
plt.close()

# ===== Chart 2 =====
plt.figure(figsize=(10, 5))
top_cities.plot(kind="bar")
plt.title("Top 10 Cities by Number of Orders")
plt.xlabel("City")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(chart2)
plt.close()

# ===== Chart 3 =====
plt.figure(figsize=(7, 5))
region_orders.plot(kind="bar")
plt.title("Orders by Region")
plt.xlabel("Region")
plt.ylabel("Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(chart3)
plt.close()

# =========================
# Create TXT report
# =========================
report_path = output_dir / "report.txt"

with open(report_path, "w", encoding="utf-8") as f:

    f.write("PHAN TICH DU LIEU THUONG MAI DIEN TU\n")
    f.write("=" * 50 + "\n\n")

    # Tổng quan
    f.write("1. TONG QUAN DU LIEU\n")
    f.write(f"So luong ban ghi: {df.shape[0]}\n")
    f.write(f"So luong thuoc tinh: {df.shape[1]}\n")
    f.write(f"So thanh pho: {df['City'].nunique()}\n")
    f.write(f"So khu vuc: {df['Region'].nunique()}\n\n")

    # Top cities
    f.write("2. TOP THANH PHO NHIEU DON HANG\n")
    f.write(str(top_cities))
    f.write("\n\n")

    # Region
    f.write("3. PHAN BO DON HANG THEO REGION\n")
    f.write(str(region_orders))
    f.write("\n\n")

    # Shipping
    f.write("4. THOI GIAN GIAO HANG TRUNG BINH\n")
    f.write(
        f"{df['Shipping Days'].mean():.2f} ngay\n\n"
    )

    # ML
    f.write("5. DE XUAT MACHINE LEARNING\n")
    f.write("- XGBoost Regressor\n")
    f.write("- Random Forest\n")
    f.write("- Prophet Forecasting\n\n")

    # Kết luận
    f.write("6. KET LUAN\n")
    f.write(
        "Du lieu phu hop cho bai toan du bao nhu cau "
        "giao hang va mo rong logistics.\n"
    )

print("DONE")
print("Charts saved in:", output_dir)
print("TXT report:", report_path)