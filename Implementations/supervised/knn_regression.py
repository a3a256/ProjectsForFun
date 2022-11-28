import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

class KNNRegression:
    def __init__(self, n_neighbors=1):
        self.neighbors = n_neighbors
        self.x = None
        self.y = None


    def fit(self, x, y):
        self.x = x
        self.y = y

    def predict(self, x):
        if x.shape[0] == 1:
            return self.predict_one(x)
        else:
            predictions = []
            for i in range(x.shape[0]):
                predictions += [self.predict_one(x[i])]
            return predictions

    def predict_one(self, x):
        distances = dict()
        for i in range(self.x.shape[0]):
            d = abs(self.x[i]-x)
            if d not in distances:
                distances[d] = [self.y[i]]
            else:
                distances[d] += [self.y[i]]
        dist = [i for i in distances.keys()]
        j = 0
        t = 0
        vals = []
        while j<self.neighbors:
            for i in distances[dist[t]]:
                vals += [i]
                j += 1
            t += 1

        return sum(vals)/self.neighbors



if __name__ == '__main__':
    df = pd.read_csv(r'breast-cancer.csv')
    x = df.iloc[:, 2].values
    y = df.iloc[:, 3].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    knn_r = KNNRegression(n_neighbors=5)
    knnr = KNeighborsRegressor(n_neighbors=5)
    knn_r.fit(x_train, y_train)
    knnr.fit(x_train.reshape(-1, 1), y_train)
    pred_implemented = knn_r.predict(x_test)
    pred = knnr.predict(x_test.reshape(-1, 1))
    print(mean_squared_error(pred, y_test))
    print(mean_squared_error(pred_implemented, y_test))