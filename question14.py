import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
#Do not import any other libraries

"""
Write a function that takes a path to a csv file as input. It will load this file into a pandas dataframe. This dataset is assumed to have a column called 'Class'.
Like in question 13, we are going to create a classification model to predict the 'Class' column but this time we are going to try to beat out previous accuracy
score by using a Random Forest Classifier (see https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) and finding an optimal
set of hyerparameters through a grid search. Three of the several hyper parameters that can be specified in this model are n_estimators, max_depth, and min_samples_split.
We are going to initialize models, fit them to the training data, and record the score for each combination of hyperparameters in the three following lists.

n_estimators in [10,50,100]
max_depth in [2, 5, 10, 100]
min_samples_split in [2,4,8,16]

This function will need to take the following steps,

* Load the csv file specified in the path to a pandas dataframe.
* Remove all rows with missing values.
* Split the data into a training set and testing set with the sklearn train_test_split() method
(see https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). y is the 'Class' column, and X is all of the other columns. Use
a test_size of 0.3, and a random_state of 0. These values are important for when the assignment is graded.
* Iterate over every possible combination of hyperparameters in the above lists totalling 48 combinations. With each combination, initialize a scikit-learn random forest
classifier model with the corresponding hyperparameters and fit that model to the training set data. Then record that list of hyperparameters in the order
[n_estimators, max_depth, min_samples_split], as well as the classification score for that model on the testing set data.
* Return a tuple where the first entry is the highest classification score that was recorded, and the second entry is the list of hyperparameters (in the same order) that
was used to get that classification score. A sample result that may be returned is (0.95, [10,2,2]). However you will get a different result running f(path) where path
is the path to the same breast-cancer-wisconsin.csv file.

This is definitely not an extensive grid search. There are more hyperparameters that could be changed, more values that could be specified for each hyperparameter, and
you could try running completely different models. However for the sake of our ability to grade this problem for all the students, the grid search is being limited to
what it is here.
"""

def f(path):
    ##########YOUR CODE HERE##########
    path = 'breast-cancer-wisconsin.csv'
    n_estimators = [10, 50, 100]
    max_depth = [2, 5, 10, 100]
    min_samples_split = [2, 4, 8, 16]

    L=[n_estimators, max_depth, min_samples_split]

    df = pd.read_csv(path)
    df = df.dropna(axis='rows')
    y = df['Class']
    X = df.drop('Class',axis='columns')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.3, random_state = 0)

    plist = []
    plist = [(i, j, k) for i in n_estimators for j in max_depth for k in min_samples_split]

    score1 = []
    for (i, j, k) in plist:
        clf = RandomForestClassifier(n_estimators = i, max_depth = j, min_samples_split = k)
        fit = clf.fit(X_train, y_train)
        score = fit.score(X_test, y_test)
        score1 = score1.append(score)
        index_max = score1.index(max(score1))
        maxscore = score[index_max]
        maxclf = clf[index_max]
        print(maxscore, maxclf)
        return maxscpre, maxclf
    ###########END CODE###############