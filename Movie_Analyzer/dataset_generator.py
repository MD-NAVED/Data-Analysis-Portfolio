import pandas as pd
import numpy as np

# ============== DATASET GENERATOR ==============
np.random.seed(101)

movies_data = {
    'MovieID': np.arange(1, 101),
    'Title': [
        f"  *#_{title}_!*" if i % 2 == 0 else f"{title}" 
        for i, title in enumerate([f"Movie_{chr(65+(i%26))}{i}" for i in range(100)])
    ],
    'Genres': np.random.choice([
        'Action|Comedy', 'Sci-Fi|Thriller', 'Romance|Drama', 
        'Action|Sci-Fi|Thriller', 'Comedy', 'Drama', 'Horror|Sci-Fi'
    ], size=100),
    'Rating': np.round(np.random.uniform(2.0, 9.8, size=100), 1),
    'Votes': np.random.randint(100, 50000, size=100)
}

movies_df = pd.DataFrame(movies_data)
# Injecting Messy NaN Data
movies_df.loc[np.random.choice(movies_df.index, size=5, replace=False), 'Rating'] = np.nan
movies_df.loc[np.random.choice(movies_df.index, size=8, replace=False), 'Genres'] = np.nan

movies_df.to_csv('movies_dataset.csv', index=False)
print("Data generated! File 'movies_dataset.csv' created.")
