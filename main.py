from numpy.ma import count_masked
import pandas as pd
import numpy as np



df_customers = pd.read_csv("customers.csv")
df_orders = pd.read_csv("orders.csv")



df_customers["Age"] = df_customers["Age"].fillna(df_customers["Age"].median())
df_orders["Quantity"] = df_orders["Quantity"].fillna(1)

(df_customers.isna().sum())
(df_orders.isna().sum())

df_merged = pd.merge(df_customers,df_orders,on="CustomerID",how="inner")

df_merged['Total_Amount'] = df_merged['Price'] * df_merged['Quantity']

df_merged['Age_Group'] = pd.cut(df_merged["Age"],bins=[0,25,45,100],labels=["Youth","Adult","Senior"])

print(df_merged.head())

revenue_by_age = df_merged.groupby("Age_Group")["Total_Amount"].sum()
famous_products = df_merged.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
df_pivot = pd.pivot_table(data=df_merged,index="Location",columns="Product",values="Total_Amount",aggfunc="sum",fill_value=0)



print(revenue_by_age)
print(famous_products)
print(df_pivot)

