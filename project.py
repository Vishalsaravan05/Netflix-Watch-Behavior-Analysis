import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset with low_memory=False to handle mixed data types
df = pd.read_csv("C:/Users/91893/OneDrive/Documents/project_saran/vodclickstream_uk_movies EDITED.csv", low_memory=False)
print(df.head())

# Rename columns to match expected names
df.rename(columns={'datetime': 'Date', 'title': 'Title'}, inplace=True)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

# Extract year and month for trend analysis
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Most watched shows/movies
top_watched = df['Title'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(y=top_watched.index, x=top_watched.values, palette='coolwarm')
plt.xlabel("Watch Count")
plt.ylabel("Title")
plt.title("Top 10 Most Watched Shows/Movies")
plt.show()

# Watch trend over time
plt.figure(figsize=(12,6))
df.groupby('Year')['Title'].count().plot(marker='o', linestyle='-')
plt.xlabel("Year")
plt.ylabel("Number of Titles Watched")
plt.title("Yearly Watching Trend")
plt.grid()
plt.show()

# Word cloud of most-watched words in titles
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(' '.join(df['Title'].dropna()))
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Watched Titles Word Cloud")
plt.show()
