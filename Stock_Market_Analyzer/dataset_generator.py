import pandas as pd
import numpy as np

np.random.seed(42)
# 100 dino ki dates banate hain
dates = pd.date_range(start='2025-01-01', periods=100)

# Random Walk (Share market ke up / down patterns)
prices = np.random.randn(100).cumsum() * 5 + 200 
df = pd.DataFrame({'Date': dates, 'Close_Price': np.round(prices, 2)})

# Jan boojhkar kuch dino ka data delete karte hain (Missing Values)
df.loc[10:15, 'Close_Price'] = np.nan
df.loc[70:73, 'Close_Price'] = np.nan

df.to_csv('stock_data.csv', index=False)
print("Data generated! 'stock_data.csv' ban gayi hai.")
