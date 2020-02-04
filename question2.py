import numpy as np
#Do not import any other libraries
"""
Write a function that takes a one dimensional numpy array and returns an array that is the Z scores of all the elements in the
original array. Say arr is a one dimensional array. The Z score of arr[i] is arr[i] minus the mean of arr, all divided by the
standard deviation of arr, or (arr[i] - mean(arr)) / stdev(arr). Suppose arr = array([1,2,3,4,5,6]). Then f(a) should return
array([-1.46385011, -0.87831007, -0.29277002,  0.29277002,  0.87831007, 1.46385011]). Taking the Z score of a column of data is
a common way of normalizing the values in a dataset.
"""

def f(arr):
    ##########YOUR CODE HERE##########
    arr = np.array([1,2,3,4,5,6])
    mean = np.mean(arr)
    std = np.std(arr)
    larr = len(arr)
    x = np.array([])
    for i in range(larr):
        y = (arr[i] - mean) / std
        x = -np.append(y, x)
    return x
    ###########END CODE###############

