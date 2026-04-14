import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Stock_Market_Analyzer/stock_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Close_Price'] = pd.to_numeric(df['Close_Price'], errors='coerce')
df['Close_Price'] = df['Close_Price'].interpolate()
df['7_day_avg'] = df['Close_Price'].rolling(window=7).mean()

# ----------------- CHART 1: Basic Line Chart -----------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close_Price'])
plt.title("Stock Price")
plt.xlabel("Date")
plt.ylabel("Close_Price")
plt.tight_layout()
plt.savefig('01_line_chart.png', dpi=300)

# ----------------- CHART 2: Multiple Lines & Legend -----------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close_Price'], label="Close Price")
plt.plot(df['Date'], df['7_day_avg'], label="7-Day Avg", color="orange", linestyle="--")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('02_moving_average.png', dpi=300)

# ----------------- CHART 3: Bar Chart (First 10 Days) -----------------
plt.figure(figsize=(10,5))
df_10 = df.head(10)
plt.bar(df_10['Date'], df_10['Close_Price'], color="skyblue")
plt.title("Starting 10 Days (Bar Chart)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('03_bar_chart.png', dpi=300)

# ----------------- CHART 4: Subplots Dashboard -----------------
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
plt.plot(df['Date'], df['Close_Price'], label="Close Price", color="blue")
plt.plot(df['Date'], df['7_day_avg'], label="7-Day Avg", color="orange", linestyle="--")
plt.title("Stock Trend (Line Chart)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(df_10['Date'], df_10['Close_Price'], color="green")
plt.title("Starting 10 Days (Bar Chart)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('04_dashboard.png', dpi=300)

# ----------------- CHART 5: Histogram -----------------
plt.figure(figsize=(8,5))
plt.hist(df['Close_Price'].dropna(), bins=10, color="purple", edgecolor="black")
plt.title("Price Distribution (Histogram)")
plt.xlabel("Price Ranges ($)")
plt.ylabel("Frequency (Kitne Din)")
plt.tight_layout()
plt.savefig('05_histogram.png', dpi=300)
plt.show()