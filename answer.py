import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def f1(n):
    res = np.zeros((n,n))
    for i in range(1,n+1):
        res[:i,:i] += np.ones((i,i))
    return res

def f2(arr):
    return (arr - np.mean(arr)) / np.std(arr)

def f3(arr):
    res = np.zeros(arr.shape)
    ncolumns = arr.shape[1]
    for i in range(n_columns):
        res[:,i] = (res[:,i] - np.mean(res[:,i])) / np.std(res[:,i])
    return res

def f4(arr1, arr2):
    return round(np.dot(arr1/np.linalg.norm(arr1), arr2/np.linalg.norm(arr2)), 4)

def f5(arr1,arr2):
    return np.vstack((arr1[arr1[:,0] > 0], arr2[arr2[:,0] > 0]))

def f6(path):
    df = pd.read_csv(path, header=None, delimiter=' ')
    df.columns = ['column_{}'.format(str(i+1)) for i in range(df.shape[1])]
    return df

def f7(df):
    df1 = df.copy()
    df1['col_1'] = df['col_1'].replace(np.nan, np.mean(df['col_1']))
    return df1.dropna(subset=['col_2'])

def f8(df):
    return df[(df.col_1%3==0) | (df.col_2>6)]

def f9(df):
    def nwords(s):
        return len(s.split())

    return df[df['text'].apply(nwords) >= 10]

def f10(df1, df2):
    cols = ['id'] + list(df2.columns.difference(df1.columns))
    return df1.merge(df2[cols], on='id', how='inner')

def f11(y, y_pred):
    return 1/len(y) * np.sum((y-y_pred)**2)

def f12(df):
    loss = 0
    for index, row in df.iterrows():
        clss = row['y']
        loss += -np.log(row['p_{}'.format(clss)])
    loss = loss / len(df)
    return loss

def f13(path):
    df = pd.read_csv(path)
    df = df.dropna()
    y = df['Class']
    X = df.drop('Class', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

def f14(path):
    n_estimators_l = [10,50,100]
    max_depth_l = [2, 5, 10, 100]
    min_samples_split_l = [2,4,8,16]
    df = pd.read_csv(path)
    df = df.dropna()
    y = df['Class']
    X = df.drop('Class', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    report = []
    for x in n_estimators_l:
        for y in max_depth_l:
            for z in min_samples_split_l:
                model = RandomForestClassifier(n_estimators = x, max_depth = y, min_samples_split = z)
                model.fit(X_train, y_train)
                report.append(([x,y,z], model.score(X_test, y_test)))
    report = sorted(report, key=lambda x: x[1], reverse=True)
    return report[0]
