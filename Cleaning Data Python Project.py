#!/usr/bin/env python
# coding: utf-8



import pandas as pd
from functools import reduce

df_1 = pd.read_csv('/Users/cristinamulas/Desktop/fish-and-seafood-consumption-per-capita.csv')
df_1 = pd.DataFrame(df_1) # convert into DataFrame
#print(df_1.head()) # print 5 rows
df_1columns = pd.read_csv('/Users/cristinamulas/Desktop/fish-and-seafood-consumption-per-capita.csv', nrows=0, sep='\t').columns.tolist()
#print(df_1columns) # ALL COLUMNS IN THIS DATAFRAME
df_1 =df_1.drop(columns=['Code']) # REMOVE CODE COLUMN
#print(df_1)
fish2013 = df_1.loc[df_1['Year'] == 2013] # selecting only 2013 rows
#fish2013
#print(fish2013['Year'].isnull()) # cheking for null values in Year column
fish2013 = fish2013.dropna(how='any',axis=0)  # delete null values
#print(fish2013.head())

# print(fish2013.describe()) # Statistical description on this table

df_2 = pd.read_csv('/Users/cristinamulas/Desktop/number-of-people-with-cancer.csv')
df_2 = pd.DataFrame(df_2) # convert into DataFrame
#print(df_2.head()) # print 5 rows

df_2columns = pd.read_csv('/Users/cristinamulas/Desktop/number-of-people-with-cancer.csv', nrows=0, sep='\t').columns.tolist()
#print(df_2columns) # ALL COLUMNS IN THIS DATAFRAME

df_2 =df_2.drop(columns=['Code']) # REMOVE CODE COLUMN
#print(df_2)
cancer2013 = df_2.loc[df_1['Year'] == 2013] # selecting only 2013 rows
#cancer2013
# print(cancer2013['Year'].isnull()) # cheking for null values in Year column
cancer2013 = cancer2013.dropna(how='any',axis=0)  # delete null values
#cancer2013
# print(cancer2013.describe()) # Statistical description on this table
df_3 = pd.read_csv('/Users/cristinamulas/Desktop/global-meat-production.csv')
df_3 = pd.DataFrame(df_1) # convert into DataFrame
#print(df_3.head()) # print 5 rows
df_3columns = pd.read_csv('/Users/cristinamulas/Desktop/global-meat-production.csv', nrows=0, sep='\t').columns.tolist()
#print(df_3columns) # ALL COLUMNS IN THIS DATAFRAME

meat2013 = df_3.loc[df_1['Year'] == 2013] # selecting only 2013 rows
#meat2013
# print(meat2013['Year'].isnull()) # cheking for null values in Year column
meat2013 = meat2013.dropna(how='any',axis=0)  # delete null values
#meat2013
# print(meat2013.describe()) # Statistical description on this table
df_4 = pd.read_csv('/Users/cristinamulas/Desktop/per-capita-milk-consumption.csv')
df_4 = pd.DataFrame(df_4) # convert into DataFrame
#print(df_4.head()) # print 5 rows

df_4columns = pd.read_csv('/Users/cristinamulas/Desktop/per-capita-milk-consumption.csv', nrows=0, sep='\t').columns.tolist()
#print(df_4columns) # ALL COLUMNS IN THIS DATAFRAME
df_4 =df_4.drop(columns=['Code']) # REMOVE CODE COLUMN
#print(df_4)
milk2013 = df_2.loc[df_1['Year'] == 2013] # selecting only 2013 rows
#milk2013
# print(milk2013['Year'].isnull()) # cheking for null values in Year column
milk2013 = milk2013.dropna(how='any',axis=0)  # delete null values
#milk2013
#print(milk2013.describe()) # Statistical description on this table
df_5 = pd.read_csv('/Users/cristinamulas/Desktop/per-capita-egg-consumption-kilograms-per-year.csv')
df_5 = pd.DataFrame(df_5) # convert into DataFrame
#print(df_5.head()) # print 5 rows

df_5columns = pd.read_csv('/Users/cristinamulas/Desktop/per-capita-egg-consumption-kilograms-per-year.csv', nrows=0, sep='\t').columns.tolist()
#print(df_5columns) # ALL COLUMNS IN THIS DATAFRAME
df_5 =df_5.drop(columns=['Code']) # REMOVE CODE COLUMN
#print(df_5)
egg2013 = df_5.loc[df_1['Year'] == 2013] # selecting only 2013 rows
#egg2013
# print(egg2013['Year'].isnull()) # cheking for null values in Year column
egg2013 = egg2013.dropna(how='any',axis=0)  # delete null values
#egg2013
#print(egg2013.describe()) # Statistical description on this table
data_frames = [fish2013, meat2013, milk2013, egg2013, cancer2013 ]
df_final = reduce(lambda left,right:pd.merge(left,right,on='Year'), data_frames)
print(df_final.head())






# Normalize total_bedrooms column
#x_array = np.array(df2013[''])
#normalized_X = preprocessing.normalize([x_array])
#conver to DF

