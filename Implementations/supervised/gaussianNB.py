import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

class NaiveBayesClassifier:
    def __init__(self):
        self.x = None
        self.y = None
        self.mean = []
        self.std = []
        self.pi = np.pi
        self.categories = []
        self.c_probabilities = None

    def fit(self, x, y):
        n_features = x.shape[1]
        self.c_probabilities = np.bincount(y)/len(y)
        for j in np.unique(y):
            self.mean += [[]]
            self.std += [[]]
            self.categories += [j]
            for i in range(n_features):
                self.mean[j] += [np.mean(x[y==j, i])]
                self.std[j] += [np.std(x[y==j, i])]
        print(self.mean)
        print(self.std)

    def predict(self, x):
        n_samples, n_features = x.shape
        probabilites = []
        for i in range(n_samples):
            proba = []
            for j in self.categories:
                a = 1
                for p in range(n_features):
                    a *= 1/np.sqrt(2*self.pi*self.std[j][p]**2)*np.exp(-0.5*((x[i, p]-self.mean[j][p])/self.std[j][p])**2)
                proba += [a]
            probabilites += [np.argmax(proba)]
        return probabilites




if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    le = LabelEncoder()
    x = df.iloc[:, [2, 3]].values
    y = df.iloc[:, 1].values
    y = le.fit_transform(y)
    knn = NaiveBayesClassifier()
    knn.fit(x[:-50, :], y[:-50])
    pen = GaussianNB()
    pen.fit(x[:-50, :], y[:-50])
    to_pred = x[-50:, :]
    test = y[-50:]
    knn.predict(to_pred)
    model = accuracy_score(knn.predict(to_pred), test)
    m = accuracy_score(pen.predict(to_pred), test)
    print(model)
    print(m)