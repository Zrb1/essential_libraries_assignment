import numpy as np
#Do not import any other libraries
"""
Write a function that takes a two dimensional array, and returns another two dimensional array where the columns of the array are
the Z scores of the columns in the original array. You should do question 2 before doing this question. For example, suppose
arr = array([[4.,2.,-3.],
             [3.,7.,11.],
             [13.,6.,2.],
             [2.,-9.,8.]])

Then f(arr) should return array([[-0.34188173,  0.07881104, -1.38675049],
                                 [-0.56980288,  0.86692145,  1.20185043],
                                 [ 1.70940865,  0.70929937, -0.46225016],
                                 [-0.79772404, -1.65503185,  0.64715023]])

If you are going to test this function, make sure to use an array of floats rather than an array of integers. Otherwise you may run into
rounding issues. 
"""

def f(arr):
    ##########YOUR CODE HERE##########
    arr=np.array([[4., 2., -3.],
                 [3., 7., 11.],
                 [13., 6., 2.],
                 [2., -9., 8.]])
    mean = np.mean(arr)
    std = np.std(arr)
    larr = len(arr)
    x = np.array([])
    for i in range(larr):
        y = (arr[i] - mean) / std
        x = np.append(y, x)
    return x
    ###########END CODE###############
