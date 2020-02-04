import numpy as np
import pandas as pd
#Do not import any other libraries

"""
Suppose you have a series of datapoints that all belong to one of three classes 'blue', 'green', or 'red'. Now suppose you have created a probabilistic classification
model to predict the classes of these datapoints, and so with each datapoint you have the predicted probabilities of each datapoint belonging to each class. Write a
function that takes a pandas dataframe df as input. The columns of this dataframe will be ['y', 'p_blue', 'p_green', 'p_red'] where p_blue, p_green, and p_red are
the predicted probabilities that each datapoint is each of the three classes, and y is the actual class that each datapoint belongs to. This function should return
the loss between the actual classes and the predicted probabilities where the loss is defined for this problem to be,

loss = 1/N * Sum from i=1 to N  -1*log(h(p_i, y_i)) (See sklearn part 1 video for more details about this loss function)

Where N is the number of datapoints, log is the natural log, p_i is the predicted probability that the class of the point was the class it actually belonged to, and y_i
is the class of each datapoint. You may want to iterate over the rows of the dataframe to do this problem. A general syntax for this is 'for index, row in df.iterrows():'
For example, running the code

for index, row in df.iterrows():
    print(row['y'])

would print out the classes of each datapoint one by one. There is a test csv file called testdf12.csv. Loading this file and running f(df) should return 0.6087900679163438.
"""

def f(df):
    ##########YOUR CODE HERE##########
    path = 'testdf12.csv'
    df = pd.read_csv(path)
    N = df['y'].size
    s = 0
    for index, row in df.iterrows():
        if row['y'] == 'blue':
            s = s + -np.log(row['p_blue'])/N
        elif row['y'] == 'green':
            s = s + -np.log(row['p_green'])/N
        elif row['y'] == 'red':
            s = s + -np.log(row['p_red'])/N
    return s
    ###########END CODE###############
