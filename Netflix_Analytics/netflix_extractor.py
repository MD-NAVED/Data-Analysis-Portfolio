import pandas as pd
import numpy as np
import random

print("Downloading Netflix/Entertainment User Stream Logs...")

np.random.seed(42)
n_rows = 5000

user_ids = [f"U-{random.randint(1000, 9999)}" for _ in range(n_rows)]
movies = [
    "Inception", "Stranger Things", "The Dark Knight", "Breaking Bad", 
    "Interstellar", "Friends", "Money Heist", "Narcos", "The Matrix", "Game of Thrones"
]
genres_map = {
    "Inception": "Sci-Fi", "Stranger Things": "Sci-Fi", "The Dark Knight": "Action", 
    "Breaking Bad": "Crime", "Interstellar": "Sci-Fi", "Friends": "Comedy", 
    "Money Heist": "Crime", "Narcos": "Crime", "The Matrix": "Sci-Fi", "Game of Thrones": "Fantasy"
}

chosen_movies = random.choices(movies, k=n_rows)
genres = [genres_map[m] for m in chosen_movies]

watch_times = [random.randint(5, 180) for _ in range(n_rows)] # minutes watched
ratings = []
for _ in range(n_rows):
    if random.random() > 0.2:
        ratings.append(round(random.uniform(1.0, 5.0), 1))
    else:
        ratings.append(np.nan) # Users who watched but didn't leave a rating

subs = random.choices(["Basic", "Standard", "Premium"], weights=[0.5, 0.3, 0.2], k=n_rows)

df = pd.DataFrame({
    'UserID': user_ids,
    'MovieTitle': chosen_movies,
    'Genre': genres,
    'WatchTime_Mins': watch_times,
    'UserRating': ratings,
    'SubscriptionType': subs
})

# Add some duplicates (Simulation of server logs glitches)
df = pd.concat([df, df.sample(100)])

df.to_csv("netflix_streams_raw.csv", index=False)
print("SUCCESS: 'netflix_streams_raw.csv' generated with 5100 stream logs.")
print("Handing over to the Data Analyst...")
