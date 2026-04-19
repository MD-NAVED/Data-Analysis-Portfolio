import pandas as pd
import duckdb 


df = pd.read_csv("Netflix_Analytics/netflix_streams_raw.csv")

df.drop_duplicates(inplace=True)
df.fillna(df['UserRating'].median(), inplace=True)

df.to_csv("Netflix_Analytics/clean_netflix_data.csv", index=False)


query1 = f"""
    SELECT 
        Genre,
        COUNT(*) AS Total_Streams,
        AVG(WatchTime_Mins) AS Avg_WatchTime_Mins,
        AVG(UserRating) AS Avg_UserRating
    FROM df
        
    GROUP BY 
        Genre
    ORDER BY 
        Total_Streams DESC;
"""

query2 = f"""
    SELECT 
        SubscriptionType,
        COUNT(*) AS Total_Streams,
        AVG(WatchTime_Mins) AS Avg_WatchTime_Mins,
        AVG(UserRating) AS Avg_UserRating
    FROM df
        
    GROUP BY 
        SubscriptionType
    ORDER BY 
        Total_Streams DESC;
"""

result_df = duckdb.execute(query1).df() 
print(result_df)

result_df = duckdb.execute(query2).df() 
print(result_df)
