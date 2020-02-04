import numpy as np
import pandas as pd
#Do not import any other libraries

"""
Write a function that takes a pandas dataframe, df as input. df is assumed to have the columns col_1 and col_2. df will have missing values (NaNs) in both columns.
The function should return the dataframe but with the missing values in col_1 replaced with the mean value within col_1 and have the rows with missing values in
col_2 dropped. Note that the order that these operations are done matters. Dropping the rows with missing values first will remove some entries and thus change the
mean value in col_1. Make sure that the NaNs in col_1 are replaced with the mean value first and then drop the rows with NaNs in col_2. This function should not actually
mutate df but instead return a different version of it. You can create a copy of df within the function by using the built in copy() method if you wish. There is a
file in this repo called testdf7.csv. Loading this dataframe into memory and running f(df) should return

   col_1  col_2
0    1.0    2.0
2    6.6    6.0
3    7.0    8.0
5    6.6   12.0
6   13.0   14.0
"""
def f(df):
    ##########YOUR CODE HERE##########
    path = 'testdf7.csv'
    df = pd.read_csv(path)
    dfx = df.copy()
    col1_mean = dfx.loc[:, 'col_1'].mean()
    dfx['col_1'] = dfx['col_1'].fillna(col1_mean)
    dfx = dfx.dropna(axis=0)
    return dfx
    ###########END CODE###############
