import pandas as pd 
import numpy as np


df1 = pd.read_csv('../dataset1.csv', sep = ',')
df2 = pd.read_csv('../dataset2.csv', sep = ',')

# Remove rows if name column value is empty or NA
df1 = df1[df1['name'].notna()]
df2 = df2[df2['name'].notna()]

# convert price column to float 64 type
df1['price'] = df1['price'].astype('float64')
df2['price'] = df2['price'].astype('float64')

# split name to first and last name by delimiter 
df1[['first_name','last_name']] = df1['name'].str.split(' ',1, expand=True)
df2[['first_name','last_name']] = df2['name'].str.split(' ',1, expand=True)

# Using numpy where to create new field which adds True if price > 100 and False if price <=100
df1['above_100'] = np.where(df1['price'] > 100,True,False)
df2['above_100'] = np.where(df2['price'] > 100,True,False)

# Reassign column order to be more presentable
final_df1 = df1[['name','first_name','last_name','price','above_100']]
final_df1.to_csv("./final_dataset1.csv", index=False)

final_df2 = df2[['name','first_name','last_name','price','above_100']]
final_df2.to_csv("./final_dataset2.csv", index=False)