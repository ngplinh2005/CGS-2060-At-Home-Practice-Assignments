# AHPA #22 - Best Movie
#
# You are a BA in Humanities major who has been tasked with researching 
# what movies were the most liked in the past 5 years.
#
# Write a Python program to read in the "films.csv"file and use the Pandas 
# library to perform the following functions:
#
# 1. Sort based on year released and print the first 5 movies.
#
# 2. Sort based on revenue and print the first 3 movies.
#
# 3. Print the movies in 2014 that had a rating of 7.9 or greater.
#
# Student Name: Linh Nguyen
#

import pandas as pd

df = pd.read_csv("AHPA #22 films.csv")

# 1. Sort based on year released and print the first 5 movies
year_sorted = df.sort_values(by='Year', ascending=True)
print("First 5 movies sorted by year:")
print(year_sorted.head(5))

# 2. Sort based on revenue and print the first 3 movies
revenue_sorted = df.sort_values(by='Revenue (Millions)', ascending=False)
print("\nFirst 3 movies sorted by revenue:")
print(revenue_sorted.head(3))

# 3. Print the movies in 2014 that had a rating of 7.9 or greater
movies_2014 = df.query("Year == 2014 and Rating >= 7.9")
print("\nMovies in 2014 with a rating of 7.9 or greater:")
print(movies_2014)