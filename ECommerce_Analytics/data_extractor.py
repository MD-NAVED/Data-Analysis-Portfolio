import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("Connecting to Company Live Database...")
np.random.seed(101)
n_rows = 5000

order_ids = [f"ORD-{random.randint(1000, 99999)}" for _ in range(n_rows)]
customers = [f"CUST-{random.randint(100, 999)}" for _ in range(n_rows)]
categories = random.choices(["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports"], k=n_rows)
cities = random.choices(["Mumbai", "Delhi", "Bangalore", "Pune", "Chennai"], k=n_rows)

dates = []
for _ in range(n_rows):
    d = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    if random.random() < 0.05:
        dates.append(d.strftime("%m/%d/%Y")) # Messy formatting
    elif random.random() < 0.05:
        dates.append("Data Not Found") # Missing formatting
    else:
        dates.append(d.strftime("%Y-%m-%d"))

quantities = []
prices = []
for _ in range(n_rows):
    q = random.randint(-2, 10) # Returns show as negative
    p = round(random.uniform(10.0, 500.0), 2)
    if random.random() < 0.03: q = np.nan 
    if random.random() < 0.02: p = np.nan 
    quantities.append(q)
    prices.append(p)

df = pd.DataFrame({
    'OrderID': order_ids,
    'CustomerID': customers,
    'City': cities,
    'OrderDate': dates,
    'Category': categories,
    'Quantity': quantities,
    'UnitPrice': prices
})

# Adding duplicates to mimic network issues
df = pd.concat([df, df.sample(75)])

df.to_csv("company_sales_raw.csv", index=False)
print("SUCCESS: 'company_sales_raw.csv' data fetched and saved.")
print("Waiting for Data Analyst to clean and report.")
