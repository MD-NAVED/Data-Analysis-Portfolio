import pandas as pd
import numpy as np

np.random.seed(42)

# 1. Customers Data
customer_ids = np.arange(1, 101)
customers = pd.DataFrame({
    'CustomerID': customer_ids,
    'Age': np.random.randint(18, 65, size=100),
    'Location': np.random.choice(['Delhi', 'Mumbai', 'Bangalore', 'Pune', 'Hyderabad'], size=100)
})
# Inject some missing ages
customers.loc[np.random.choice(customers.index, size=5, replace=False), 'Age'] = np.nan

# 2. Sales Data
orders = pd.DataFrame({
    'OrderID': np.arange(1001, 1501),
    'CustomerID': np.random.choice(customer_ids, size=500),
    'Product': np.random.choice(['Laptop', 'Smartphone', 'Headphones', 'Monitor', 'Keyboard'], size=500),
    'Price': np.random.choice([50000, 20000, 2000, 10000, 1500], size=500),
    'Quantity': np.random.randint(1, 5, size=500)
})

# Inject missing values in Quantity
orders.loc[np.random.choice(orders.index, size=15, replace=False), 'Quantity'] = np.nan

customers.to_csv('customers.csv', index=False)
orders.to_csv('orders.csv', index=False)

print("Datasets generated successfully: 'customers.csv' and 'orders.csv'!")
