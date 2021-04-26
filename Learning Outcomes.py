# Creating Project Repo

# importing CSV file
import pandas as pd

netflix_df = pd.read_csv('netflix_titles.csv', index_col='show_id')

print(netflix_df.isna().sum())


# removing coloum with the most missing values
netflix_df1 = netflix_df.drop('director', axis=1)


# dropping duplicates
netflix_df1.drop_duplicates()

print(netflix_df1.isna().sum())


# slicing a Movies and TV
moives_tv = netflix_df1.loc[:, :'type']

release_year = netflix_df1.loc[:, ['country','release_year','listed_in']]

# Iterate through DataFrame
for moives, type in netflix_df1.iterrows():
    print(pd.value_counts(''))

