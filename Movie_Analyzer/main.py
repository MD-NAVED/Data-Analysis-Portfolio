from traceback import print_tb
import pandas as pd
import numpy as np


df = pd.read_csv('movies_dataset.csv')


df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
df["Genres"] = df["Genres"].fillna("Unknown")

df["Title"] = df["Title"].str.replace(r'[*#_! ]', '', regex=True)

comedy_movies = df[df["Genres"].str.contains("Comedy", na=False)]

df["Hit_Status"] = np.where(df.Rating >= 8.0, "Hit", "Flop")

print(df.head(10))

print(comedy_movies.head(5))

print(df["Hit_Status"].value_counts())

Higest_genre = df.groupby("Genres")["Rating"].mean().sort_values(ascending=False)
print(Higest_genre)




