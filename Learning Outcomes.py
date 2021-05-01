### Learning Outcomes assessed:

# Imprting packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


# Function
def importdata(filename):
    data=pd.read_csv(filename)



# importing CSV file
netflix_df = pd.read_csv('netflix_titles.csv', index_col='show_id')

print(netflix_df.isna().sum())



# removing coloum with missing values
netflix_df1 = netflix_df.drop('director', axis=1)



# dropping duplicates
netflix_df1.drop_duplicates()

print(netflix_df1.isna().sum())



# slicing dataset - Movies and TV
moives_tv = netflix_df1.loc[:, :'title']

release_year = netflix_df1.loc[:, ['country','release_year','listed_in']]



# Iterate through DataFrame
for index, row in netflix_df.iterrows():
    print(index, ': ', row['title'], 'has', row['duration'], 'duration.')


results = Counter()
netflix_df1['type'].str.lower().str.split().apply(results.update)
print(results)



# merging two dataframes
movies_tv_release_year = moives_tv.merge(release_year, on= 'show_id')



# Using numpy
viewing_time = netflix_df = pd.read_csv('netflix_titles.csv', index_col='show_id', nrows=9)
print(viewing_time.head())

viewing_time_array = viewing_time.values



# Creating a Dictionary of key value pairs
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

print(europe['france']['capital'])

# Create sub-dictionary data
data = {'population': 59.83, 'capital': 'rome'}

# Add data to europe under key
europe['italy'] = data

print(europe)



### Project Report
## Visualize Data for Project

ecomm = pd.read_csv('Train.csv')
print(ecomm.isna().sum())

# Visualization 1 - Transport Method Distribution
plt.hist(ecomm['Mode_of_Shipment'], color='purple', edgecolor='black')
plt.xlabel('Transport Method')
plt.ylabel('# of products shipped')
plt.title('Transport Method Distribution')
plt.show()



# Visualization 2 - Value of product shipped from each Warehouse
ecomm1 = ecomm[['Warehouse_block', 'Cost_of_the_Product']]

value_by_warehouse = ecomm1.groupby("Warehouse_block").sum().plot(kind='bar')
value_by_warehouse.set_xlabel("Warehouse Block")
value_by_warehouse.set_ylabel("Value of Stock Held")
value_by_warehouse.set_title('Value of product shipped from each Warehouse')
plt.show()



# Visualization 3 - Discount Distribution of Purchases
N = 10999
x = ecomm['Discount_offered']
y = ecomm['Cost_of_the_Product']
colors = np.random.rand(N)
area = np.pi*10

plt.title("Discount Distribution of Purchases")
plt.xlabel("Discount Offered in %")
plt.ylabel("Cost of Product per hundred in US Dollars")
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()



# Visualization 4 - Product Imprtance by Gender
ax = sns.boxplot(x="Product_importance", y="Cost_of_the_Product", hue="Gender", data=ecomm, dodge=True)
plt.show()



# Visualization 5 - Relationship between customer rating & repeat purchases
sns.set_theme(style="darkgrid")
g = sns.jointplot(x="Customer_rating", y="Prior_purchases", data=ecomm,
                  kind="reg", truncate=False,
                  xlim=(0, 6), ylim=(0, 11),
                  color="m", height=7)
plt.show()