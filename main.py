import pandas as pd

df=pd.read_csv("netflix_titles.csv")
print(df.head(10))
print(df.shape)
print(df.columns)
print(df.info())


# null values
print(df.isnull().sum())

# handle the null values 
df["director"] =df["director"].fillna("Unknown")
print(df.isnull().sum())
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"]=df["rating"].fillna("N/A")
df = df.dropna(subset=["duration"])
df = df.dropna(subset=["date_added"])


print(df.isnull().sum())
df.info()


# checking duplicates

print(df.duplicated().sum())

print(df.columns)

df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()

print(df.columns)
df["duration_value"] = df["duration"].str.extract(r"(\d+)").astype(float)

df["duration_unit"] = df["duration"].str.extract(r"([A-Za-z]+)")
print(df["release_year"].describe())
movies = df[df["type"] == "Movie"].copy()

tv_shows = df[df["type"] == "TV Show"].copy()
print(movies["duration"].head())
print(tv_shows["duration"].head())



# Save as CSV
movies.to_csv("netflix_movies.csv", index=False)
tv_shows.to_csv("netflix_tv_shows.csv", index=False)

# Check
print("Movies:", movies.shape)
print("TV Shows:", tv_shows.shape)

df.to_csv("netflix_cleaned.csv", index=False)