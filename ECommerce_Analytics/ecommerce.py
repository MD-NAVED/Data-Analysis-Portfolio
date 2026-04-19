import pandas as pd
import duckdb 


df = pd.read_csv('ECommerce_Analytics/company_sales_raw.csv')


df.info()
print(df.duplicated().sum())
print(df.isnull().sum())
print(df.describe() )



df = df.drop_duplicates()

df['Quantity'].fillna(df['Quantity'].median())
df = df[df['Quantity'] >= 0]

df['UnitPrice'].fillna(df['UnitPrice'].median())
df = df[df['UnitPrice'] >= 0]

print(df.isnull().sum())


df.to_csv('clean_ecommerce.csv', index=False)


df = pd.read_csv('clean_ecommerce.csv')



query = f"""
    SELECT
        City,
        Category,
        SUM(Quantity) as TotalQuantity,
        SUM(UnitPrice * Quantity) as TotalRevenue
    FROM df
    GROUP BY City, Category
    ORDER BY TotalRevenue DESC
    """

result = duckdb.execute(query).df()
print(result)
top_5=  result.head(5)



import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.bar(top_5['City'], top_5['TotalRevenue'],color='green',alpha=0.7)
plt.title('Top 5 Cities by Total Revenue')
plt.xlabel('City')
plt.ylabel('Total Revenue (In Rupees)')
plt.savefig('ECommerce_Analytics/ecommerce_top_revenue.png',dpi=300,bbox_inches='tight')
plt.show()



