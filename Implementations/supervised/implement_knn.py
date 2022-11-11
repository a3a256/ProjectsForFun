import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class KNeighborsModel:
    def __init__(self, n_neighbors, x, y):
        self.k = n_neighbors
        self.x = x
        self.y = y

    def predict(self, x):
        predictions = []
        for i in range(len(x)):
            arr = [x[i, 0], x[i, 1]]
            predictions += [self.predict_value(arr)]
        return predictions

    def predict_value(self, x):
        distances = dict()
        x_axis = x[0]
        y_axis = x[1]
        for i in range(len(self.x)):
            d = self.distance(x_axis, y_axis, self.x[i, 0], self.x[i, 1])
            if d not in distances:
                distances[d] = [[self.x[i, 0], self.x[i, 1], self.y[i]]]
            else:
                distances[d].append([self.x[i, 0], self.x[i, 1], self.y[i]])
        categories = []
        dist = [i for i in distances.keys()]
        dist = sorted(dist)
        j = 0
        t = 0
        while j<self.k:
            a = distances[dist[t]]
            for i in a:
                categories += [i]
                j += 1
            t += 1
        classify = dict()
        for i in categories:
            if i[2] not in classify:
                classify[i[2]] = 1
            else:
                classify[i[2]] += 1
        s = sorted(classify, key=lambda x: (-classify[x]))
        return s[0]



    def distance(self, x, y, x1, y1):
        return np.sqrt((x-x1)**2 + (y-y1)**2)



if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    le = LabelEncoder()
    x = df.iloc[:, [2, 3]].values
    y = df.iloc[:, 1].values
    y = le.fit_transform(y)
    knn = KNeighborsModel(n_neighbors=3, x=x, y=y)
    kp = KNeighborsClassifier(n_neighbors=3)
    kp.fit(x[:-50, :], y[:-50])
    to_pred = x[-50:, :]
    test = y[-50:]
    model = accuracy_score(kp.predict(to_pred), test)
    m = accuracy_score(knn.predict(to_pred), test)
    print(model)
    print(m)