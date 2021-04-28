# Creating Project Repo
import label as label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def importdata(filename):
    data=pd.read_csv(filename)



# importing CSV file
netflix_df = pd.read_csv('netflix_titles.csv', index_col='show_id')

print(netflix_df.isna().sum())



# removing coloum with the most missing values
netflix_df1 = netflix_df.drop('director', axis=1)



# dropping duplicates
netflix_df1.drop_duplicates()

print(netflix_df1.isna().sum())



# slicing a Movies and TV
moives_tv = netflix_df1.loc[:, :'title']

release_year = netflix_df1.loc[:, ['country','release_year','listed_in']]



# Iterate through DataFrame
for index, row in netflix_df.iterrows():
    print(index, ': ', row['title'], 'has', row['duration'], 'duration.')

from collections import Counter
results = Counter()
netflix_df1['type'].str.lower().str.split().apply(results.update)
print(results)



# merging two dataframes

movies_tv_release_year = moives_tv.merge(release_year, on= 'show_id')



# numpy
viewing_time = netflix_df = pd.read_csv('netflix_titles.csv', index_col='show_id', nrows=9)
print(viewing_time.head())

viewing_time_array = viewing_time.values



# Creating a Dictionary of countries and capital, key value pairs
europe = { 'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }



# Visualize
# Visualization 1
ecomm = pd.read_csv('Train.csv')

plt.hist(ecomm['Mode_of_Shipment'], color='purple', edgecolor='black')
plt.xlabel('Transport Method')
plt.ylabel('# of products shipped')
plt.title('Transport Method Distribution')

plt.show()


# Visualization 2
ecomm1 = ecomm[['Warehouse_block', 'Cost_of_the_Product']]

value_by_warehouse = ecomm1.groupby("Warehouse_block").sum().plot(kind='bar')
value_by_warehouse.set_xlabel("Warehouse Block")
value_by_warehouse.set_ylabel("Value of Stock Held")
value_by_warehouse.set_title('Value of product shipped from each Warehouse')

plt.show()


# Visualization 3
