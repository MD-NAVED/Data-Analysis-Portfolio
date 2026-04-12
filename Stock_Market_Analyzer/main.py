import pandas as pd
import numpy as np



df = pd.read_csv('Stock_Market_Analyzer/stock_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Close_Price'] = pd.to_numeric(df['Close_Price'], errors='coerce')
df['Close_Price'] = pd.to_numeric(df['Close_Price'], errors='coerce')
df['Close_Price'] = df['Close_Price'].interpolate()

print(df.head(20))

df['7_day_avg'] = df['Close_Price'].rolling(window=7).mean()

print(df.head(15))

df['Sgnal'] = np.where(df['Close_Price'] > df['7_day_avg'], 'Buy', 'Sell')
df.loc[[df['Close_Price'].idxmax()]]
print(df.head(10))
print(df.loc[[df['Close_Price'].idxmax()]])

