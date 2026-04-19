# 📊 Data Analysis Portfolio
**Author**: Mohammad Naved  

A comprehensive collection of Data Analytics projects demonstrating an end-to-end data pipeline. This repository showcases real-world workflows ranging from raw data extraction and missing-value imputation using Pandas, to advanced, high-performance in-memory SQL execution via DuckDB, concluding with data storytelling and visualization using Matplotlib.

## 🛠️ Tech Stack & Core Skills
- **Languages**: Python, SQL
- **Frameworks & Libraries**: Pandas, DuckDB, Matplotlib, NumPy, urllib
- **Core Competencies**: 
  - Exploratory Data Analysis (EDA)
  - Data Cleansing (NaN/Null Handling, Deduplication, Filtering anomalies)
  - High-performance SQL Aggregations (`GROUP BY`, Multi-Condition Logic)
  - Live Data API Integration (JSON parsing)
  - Data Visualization (Automated Line & Bar Charts)

---

## 📁 Projects Included

### 1. 🛍️ E-Commerce & Retail Analytics (`/ECommerce_Analytics`)
- **Objective**: Cleanse and analyze a massive, unformatted export of simulated online transactions.
- **Execution**:
  - Parsed raw CSV data, handling null cells through median-imputation and dropping negative/returned commodities using **Pandas**.
  - Executed native SQL queries on dataframes via **DuckDB** to identify the most lucrative Region+Category combinations through advanced mathematical joins: e.g., `SUM(Quantity * UnitPrice)`.
  - Processed insights into a High-Definition **Matplotlib** bar chart to communicate top revenue-generating cities clearly.

### 2. 📈 Live Finance & Cryptocurrency Trends (`/Crypto_Analytics`)
- **Objective**: Function as a Quantitative Analyst mapping Live Bitcoin trends to assist trading strategy.
- **Execution**:
  - Built an automated pipeline utilizing `urllib` and `json` to ping **Live Binance APIs**, extracting raw daily Open/High/Low/Close details.
  - Reduced market volatility "noise" by employing Pandas' specialized algorithmic functions like `rolling(window=5).mean()` to compute standard Moving Averages.
  - Generated visual overlays depicting standard prices intersecting with synthesized trend lines using **Matplotlib**.

### 3. 🍿 Netflix / Streaming Entertainment Base (`/Netflix_Analytics`)
- **Objective**: Generate user-centric product insights from thousands of server-side streaming logs.
- **Execution**:
  - Maintained raw server log integrity by safely isolating missing review elements (`NaN`) and resolving duplicates programmatically.
  - Fired parallel **DuckDB** queries traversing 5,000+ entries to determine the viewer retention (averaging total Watch Time) associated with specific `SubscriptionTypes`.
  - Decoded maximum Average User Rating correlations mapped perfectly to explicit content `Genres`.