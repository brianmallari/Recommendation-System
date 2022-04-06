# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 22:17:32 2021

@author: Brian
"""

# Simple Recommendation System inspired by content by Mr. Aditya Sharma on datacamp.com
# (URL = https://www.datacamp.com/community/tutorials/recommender-systems-python)

# list of mods to the data frame 
# mod_1 => changed the data type for column with index 0 from int to str
# mod_2 => dropped column index 4 from the dataframe
# mod_3 => added column names to the dataframe
# mod_4 => grouped count of each user behavior by game title

# mod_5 => isolated just the purchased behavior among all of the games
# mod_6 => grouped the count of purchased behavior by game title
# mod_7 => converted object from a pandas series to a pandas dataframe
# mod_8 => renamed the column titled behavior-name to purchase-count

# mod_9 => isolated just the play behavior among all of the games
# mod_10 => grouped the count of played behavior by game title
# mod_11 => converted object from a pandas series to a pandas dataframe
# mod_12 => renamed the column titled behavior-name to play-count

# mod_13 => join mod_8 and mod_12 dataframes along the indeces (game titles)
# mod_14 => filter out the games where the purchase count and the play count aren't equal
# mod_15 => grouped the sum of hours played by game title
# mod_16 => converted object from a pandas series to a pandas dataframe
# mod_17 => renamed the column titled value to hours-played

# mod_18 => join mod_14 and mod_17 dataframes along the indeces (game titles)
# mod_19 => sort the game titles of mod_18 by total hours played in descending order

# import necessary libraries/pacakges
import pandas as pd

# load Steam games metadata 
# (this data doesn't have a header, as demonstrated from the prior data exploration)
steam_games_metadata = pd.read_csv('steam-200k.csv', header = None, low_memory = False)

# set configuration to show all columns in a pandas dataframe
pd.options.display.max_columns = None

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the dataframe steam_games_metadata: ")
print(steam_games_metadata.head(row_count))
print("\n")

# change the data types for the first column in the data frame steam_games_metadata 
# because the values wre originally treated as as numbers (int) 
# instead of user IDs (str)
steam_games_metadata_mod_1 = steam_games_metadata.astype({0: str})
del steam_games_metadata

print("Data type for each of the columns of the dataframe steam_games_metadata_mod_1: ")
print(steam_games_metadata_mod_1.dtypes)
print("\n")

# remove the last column, because that has no important data, as determined by both 
# the descritpion of the data found at https://www.kaggle.com/tamber/steam-video-games/data
# and the prior data exloration
steam_games_metadata_mod_2 = steam_games_metadata_mod_1.drop(columns = 4)
del steam_games_metadata_mod_1

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_2: ")
print(steam_games_metadata_mod_2.head(row_count))
print("\n")

# add column names to the steam_games_metadata dataframe based off of
# description of the data found at https://www.kaggle.com/tamber/steam-video-games/data 
steam_games_metadata_mod_2.columns = ['user-id', 'game-title', 'behavior-name', 'value']
steam_games_metadata_mod_3 = steam_games_metadata_mod_2
del steam_games_metadata_mod_2

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_3: ")
print(steam_games_metadata_mod_3.head(row_count))
print("\n")

# group the count of each user behavior by game title
# because the number of purchases != the number of plays
# (refer to descriptive statics for procedure/code examples)
steam_games_metadata_mod_4 = steam_games_metadata_mod_3.groupby(['game-title', 'behavior-name'])['behavior-name'].count()

# print content for first few rows to verify that things are going well so far
row_count = 10; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_3: ")
print(steam_games_metadata_mod_4.head(row_count))
print("\n")


# purchased behavior

# isolate just the purchased behavior among all of the games
steam_games_metadata_mod_5 = steam_games_metadata_mod_3[steam_games_metadata_mod_3['behavior-name'] == 'purchase']

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_5: ")
print(steam_games_metadata_mod_5.head(row_count))
print("\n")

# group the count of purchased behavior by game title
steam_games_metadata_mod_6 = steam_games_metadata_mod_5.groupby(['game-title'])['behavior-name'].count()

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_6: ")
print(steam_games_metadata_mod_6.head(row_count))
print("\n")

# identify the data type for steam_games_metadata_mod_6
print("Data type for the variable steam_games_metadata_mod_6: ")
print(type(steam_games_metadata_mod_6))
print("\n")

# convert steam_games_metadata_mod_6 from a pandas series to a pandas dataframe
steam_games_metadata_mod_7 = steam_games_metadata_mod_6.to_frame()

# identify the data type for steam_games_metadata_mod_7
print("Data type for the variable steam_games_metadata_mod_7: ")
print(type(steam_games_metadata_mod_7))
print("\n")

# identify the shape of the data
print("Shape of the dataframe steam_games_metadata_mod_7 (# of rows, # of columns): ")
print(steam_games_metadata_mod_7.shape)
print("\n")

# showcase the names of the columns
print("Column names for the variable steam_games_metadata_mod_7: ")
print(steam_games_metadata_mod_7.columns)
print("\n")

# rename the column titled behavior-name to purchase-count
steam_games_metadata_mod_8 = steam_games_metadata_mod_7.rename(columns = {'behavior-name': 'purchase-count'})

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_8: ")
print(steam_games_metadata_mod_8.head(row_count))
print("\n")

# played behavior

# isolate just the purchased behavior among all of the games
steam_games_metadata_mod_9 = steam_games_metadata_mod_3[steam_games_metadata_mod_3['behavior-name'] == 'play']

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_9: ")
print(steam_games_metadata_mod_9.head(row_count))
print("\n")

# group the count of played behavior by game title
steam_games_metadata_mod_10 = steam_games_metadata_mod_9.groupby(['game-title'])['behavior-name'].count()

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_10: ")
print(steam_games_metadata_mod_10.head(row_count))
print("\n")

# identify the data type for steam_games_metadata_mod_10
print("Data type for the variable steam_games_metadata_mod_10: ")
print(type(steam_games_metadata_mod_10))
print("\n")

# convert steam_games_metadata_mod_10 from a pandas series to a pandas dataframe
steam_games_metadata_mod_11 = steam_games_metadata_mod_10.to_frame()

# identify the data type for steam_games_metadata_mod_11
print("Data type for the variable steam_games_metadata_mod_11: ")
print(type(steam_games_metadata_mod_11))
print("\n")

# identify the shape of the data
print("Shape of the dataframe steam_games_metadata_mod_11 (# of rows, # of columns): ")
print(steam_games_metadata_mod_11.shape)
print("\n")

# showcase the names of the columns
print("Column names for the variable steam_games_metadata_mod_11: ")
print(steam_games_metadata_mod_11.columns)
print("\n")

# rename the column titled behavior-name to play-count
steam_games_metadata_mod_12 = steam_games_metadata_mod_11.rename(columns = {'behavior-name': 'play-count'})

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_12: ")
print(steam_games_metadata_mod_12.head(row_count))
print("\n")

# isolate just the games that were both purchased and played
# because these games were good enough to not only buy but also spend time playing
steam_games_metadata_mod_13 = steam_games_metadata_mod_8.join(steam_games_metadata_mod_12, how = 'inner')

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_13: ")
print(steam_games_metadata_mod_13.head(row_count))
print("\n")

# acquire some descriptive statistics for the dataframe steam_games_metadata_mod_13; 
# this helps to confirm that things are going well, and ideally the counts
# for both purchased games and played games should be the same
print("Some descriptive statistics for the data frame steam_games_metadata_mod_13: ")
print(steam_games_metadata_mod_13.describe())
print("\n")

# identify the data type for each column of steam_games_metadata_mod_13
print("Data types for each of the columns of steam_games_metadata_mod_13")
print(steam_games_metadata_mod_13.dtypes)
print("\n")

# just a simple test to see if numeric equivalence works between an int and a float
print(1 == 1.0)
print(type(1))
print(type(1.0))
print("\n")

# filter out the games where the purchase count and the play count aren't equal, 
# or more specifically, where the purchase count is greater than the play count 
# which would imply that people were willing and able to buy the game, but not willing and able to spend time playing the game, too
steam_games_metadata_mod_14 = steam_games_metadata_mod_13[steam_games_metadata_mod_13['purchase-count'] == steam_games_metadata_mod_13['play-count']]

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_14: ")
print(steam_games_metadata_mod_14.head(row_count))
print("\n")

# group the sum of hours played by game title (builds off of the "mod_9" dataframe)
steam_games_metadata_mod_15 = steam_games_metadata_mod_9.groupby(['game-title'])['value'].sum()

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_15: ")
print(steam_games_metadata_mod_15.head(row_count))
print("\n")

# identify the data type for steam_games_metadata_mod_15
print("Data type for the variable steam_games_metadata_mod_15: ")
print(type(steam_games_metadata_mod_15))
print("\n")

# convert steam_games_metadata_mod_15 from a pandas series to a pandas dataframe
steam_games_metadata_mod_16 = steam_games_metadata_mod_15.to_frame()

# identify the data type for steam_games_metadata_mod_16
print("Data type for the variable steam_games_metadata_mod_16: ")
print(type(steam_games_metadata_mod_16))
print("\n")

# identify the shape of the data
print("Shape of the dataframe steam_games_metadata_mod_16 (# of rows, # of columns): ")
print(steam_games_metadata_mod_16.shape)
print("\n")

# showcase the names of the columns
print("Column names for the variable steam_games_metadata_mod_16: ")
print(steam_games_metadata_mod_16.columns)
print("\n")

# rename the column titled behavior-name to hours-played
steam_games_metadata_mod_17 = steam_games_metadata_mod_16.rename(columns = {'value': 'hours-played'})

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_17: ")
print(steam_games_metadata_mod_17.head(row_count))
print("\n")

# join the dataframe with hours played (mod_17) to the dataframe where count of purchases for a game
# is equal to count of plays for the same game (mod_14)
steam_games_metadata_mod_18 = steam_games_metadata_mod_14.join(steam_games_metadata_mod_17, how = 'inner')

# print content for first few rows to verify that things are going well so far
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_18: ")
print(steam_games_metadata_mod_18.head(row_count))
print("\n")

# sort the game titles of the mod_18 dataframe by total hours played in descending order, 
# and then showcase the top few (e.g., 5 or 10) titles as the games to recommend
steam_games_metadata_mod_19 = steam_games_metadata_mod_18.sort_values(by=['hours-played'], ascending = False)

# print content for first few rows to verify that things are going well so far
row_count = 10; 
print(f"First {row_count} rows of the variable steam_games_metadata_mod_19: ")
print(steam_games_metadata_mod_19.head(row_count))
print("\n")

# consider cleaning up this code for the write-up, 
# or maybe even try out something like Jupyter Notes to create the report 
# with the lines of Python code embedded in with the file contents