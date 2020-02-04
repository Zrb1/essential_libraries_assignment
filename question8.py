import numpy as np
import pandas as pd
#Do not import any other libraries

"""
Write a function that takes a pandas dataframe, df as input. df is assumed to have the columns col_1 and col_2. The function should return a new dataframe that
has the rows in df that satisfy at least one of the two conditions: The col_1 entry is a multiple of 3, or the col_2 entry is greater than 6. The general syntax
for subsetting a dataframe based on multiple conditions is df[(condition1) | (condition2)]. Replace the "|" with "&" depending on whether you want the rows that
satisfy any of the conditions or you want the rows to satisfy both (all) the conditions. "|" means OR and "&" means AND. There is a csv file called testdf8.csv.
Loading this as a dataframe and running f(df) should return 

   col_1  col_2
1      3      4
3      7      8
4      9     10
5     11     12
6     13     14
"""
def f(df):
    ##########YOUR CODE HERE##########
    path = 'testdf8.csv'
    df = pd.read_csv(path)
    dfx = df.copy()
    dfx = dfx[(df.col_1 % 3 == 0) | (dfx.col_2>6)]
    return dfx
    ###########END CODE###############