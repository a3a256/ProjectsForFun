import pandas as pd
import numpy as np


def mean(arr):
    return sum(arr)/len(arr)


def variance(arr):
    return sum([(i - mean(arr))**2 for i in arr])/len(arr)


def covar(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    upper = [(i-mean_x)*(j-mean_y) for i, j in zip(x, y)]
    return sum(upper)/len(x)


def cov(arr):
    res = []
    row = []
    x = []
    y = []
    for k in range(len(arr[0])):
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                if i == k:
                    x += [arr[j][i]]
                else:
                    x += [arr[j][k]]
                    y += [arr[j][i]]
            if i == k:
                row += [variance(x)]
            else:
                row += [covar(x, y)]
            x = []
            y = []
        res += [row]
        row = []

    
    return res




if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')


    vals = df.iloc[:, 4:8].values


    f = cov(vals)
    g = np.cov(vals.T)

    for i in f:
        print(i)

    print("-"*10)

    print(g)