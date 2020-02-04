import numpy as np
import pandas as pd
#Do not import any other libraries

"""
Write a function that takes 2 pandas dataframes as input, df1 and df2. df1 and df2 each have their own set of columns but there will be at least one column
that is common to both of them called the 'id' column. This function should return a new dataframe which is df2 joined onto df1 on the 'id' column. You should
use an inner join to merge them. However, there may be other columns in df2 that are also in df1, so if we simply do an inner join between df1 and df2 then
duplicate columns will exist in the final result. The returned dataframe should not contain any duplicate columns. The built in difference() pandas function
may be useful for finding the columns in df2 that are not in df1. There are 2 csv files called testdf10_1.csv and testdf10_2.csv. Loading the first file as
df1 and the second file as df2 and running f(df1, df2) should return

   id   Name  Birthdate                         School                Job State of Origin
0   1  Alice  1991/1/13       University of Washington  Software Engineer      Washignton
1   2    Bob  1992/3/13                Seattle Central        Electrician          Oregon
2   3  Cathy   1989/4/3  Western Washington University             Retail      California
3   8  Frank  1987/9/21                            NaN        Stockbroker        New York
4   9   Gina  1991/12/1              Evergreen College                NaN      Washington
"""
def f(df1, df2):
    ##########YOUR CODE HERE##########
    cols = ['id'] + list(df2.columns.difference(df1.columns))
    x = df1.merge(df2[cols], on='id', how='inner')
    return x
    ###########END CODE###############
