# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:06:29 2021

@author: Brian
"""

# list of mods to the data frame 
# mod_1 => changed the data type for column with index 0 from int to str

# import necessary libraries/pacakges
import pandas as pd

# load Steam games metadata  
# steam_games_metadata = pd.read_csv('steam-200k.csv', low_memory = False)
steam_games_metadata = pd.read_csv('steam-200k.csv', header = None, low_memory = False)

# set configuration to show all columns in a pandas dataframe
pd.options.display.max_columns = None

# print content for first few rows
row_count = 5; 
print(f"First {row_count} rows of the variable steam_games_metadata: ")
print(steam_games_metadata.head(row_count))
print("\n")

# identify the data type for steam_games_metadata
print("Data type for the variable steam_games_metadata: ")
print(type(steam_games_metadata))
print("\n")

# identify the shape of the data
print("Shape of the dataframe steam_games_metadata (# of rows, # of columns): ")
print(steam_games_metadata.shape)
print("\n")

# change the data types for one of the columns in the data frame steam_games_metadata
steam_games_metadata_mod_1 = steam_games_metadata.astype({0: str})
del steam_games_metadata

# acquire some descriptive statistics for the dataframe steam_games_metadata_mod_1
print("Some descriptive statistics for the data frame steam_games_metadata_mod_1: ")
print(steam_games_metadata_mod_1.describe())
print("\n")

# acquire descriptive statistics for the columns of dataframe steam_games_metadata_mod_1
# with non-numeric values
print("Descriptive statistics for non-numeric values of the dataframe steam_games_metadata_mod_1: ")
print(steam_games_metadata_mod_1.iloc[ : , [0, 1, 2]].describe())
print("\n")

# determine the count of "purchase" and the count of "play", and then
# compare the two values (in case the two counts are different)
print("Counts for the different player behaviors with respect to Steam games: ")
print(steam_games_metadata_mod_1.iloc[ : , 2].value_counts())
print("\n")

# think about how to determine what games to recommend
# total hours played by all players?
# average hours played by players? 
# ratio of played to purchased? 