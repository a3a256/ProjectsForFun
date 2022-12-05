import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class KNeighborsModel:
    def __init__(self, n_neighbors):
        self.k = n_neighbors
        self.x = None
        self.y = None


    def fit(self, x, y):
        self.x = x
        self.y = y

    def predict(self, x):
        print(len(x.shape))
        predictions = []
        for i in range(len(x)):
            arr = [x[i, 0], x[i, 1]]
            predictions += [self.predict_value(arr)]
        return predictions

    def pred_one_variable(self, x):
        preds = []
        for i in range(len(x)):
            preds += [self.predict_var(x[i])]
        return preds

    def predict_var(self, x):
        distances = dict()
        for i in range(self.x.shape[0]):
            d = abs(self.x[i] - x)
            if d not in distances:
                distances[d] = [y[i]]
            else:
                distances[d] += [y[i]]
        dist = [i for i in distances.keys()]
        categories = []
        n = 0
        k = 0
        while n < self.k:
            for i in distances[dist[k]]:
                categories = [i]
            else:
                categories += [i]
                n += 1
            k += 1
        classify = dict()
        for i in categories:
            if i not in classify:
                classify[i] = 1
            else:
                classify[i] += 1
        s = sorted(classify, key=lambda x: (-classify[x]))
        return s[0]
            

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

    def predict_multi(self, x):
        preds = []
        for i in range(len(x)):
            preds += [self.multivariable_one(x[i, :])]

        return preds


    def multivariable_one(self, x):
        classes = dict()
        first = 0
        while first < self.x.shape[1]-1:
            for j in range(first+1, self.x.shape[1]):
                second = j
                distances = dict()
                x_axis = x[first]
                y_axis = x[second]
                for i in range(self.x.shape[0]):
                    d = self.distance(x_axis, y_axis, self.x[i, first], self.x[i, second])
                    if d not in distances:
                        distances[d] = [[self.x[i, first], self.x[i, second], self.y[i]]]
                    else:
                        distances[d] += [[self.x[i, first], self.x[i, second], self.y[i]]]

                categories = []
                dist = [i for  i in distances.keys()]
                dist = sorted(dist)
                t = 0
                n = 0
                classify = dict()
                while t < self.k:
                    for i in distances[dist[n]]:
                        if i[2] not in classify:
                            classify[i[2]] = 1
                        else:
                            classify[i[2]] += 1
                        t += 1
                    n += 1
                
                s = sorted(classify, key=lambda x: (-classify[x]))
            if s[0] not in classes:
                classes[s[0]] = 1
            else:
                classes[s[0]] += 1
            first += 1
        predictions = sorted(classify, key=lambda x: (-classify[x]))
        return predictions[0]



    def distance(self, x, y, x1, y1):
        return np.sqrt((x-x1)**2 + (y-y1)**2)



if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    le = LabelEncoder()
    x = df.iloc[:, 2].values
    y = df.iloc[:, 1].values
    y = le.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    knn = KNeighborsModel(n_neighbors=3)
    knn.fit(x_train, y_train)
    kp = KNeighborsClassifier(n_neighbors=3)
    kp.fit(x_train.reshape(-1, 1), y_train)
    model = accuracy_score(kp.predict(x_test.reshape(-1, 1)), y_test)
    m = accuracy_score(knn.pred_one_variable(x_test), y_test)
    print(model)
    print(m)
