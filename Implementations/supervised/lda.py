import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from collections import Counter
import matplotlib.pyplot as plt

class LDA:
    def __init__(self):
        self.w = None


    def between_class(self, x, y):
        means = []
        for i in np.unique(y):
            means += [np.mean(x[y==i, :])]

        means = np.array(means)
        between_class_scatter = np.dot(means.reshape(-1, 1), means.reshape(1, -1))
        return between_class_scatter



    def in_between(self, x, y):
        within_class_scatter = np.zeros((x.shape[1], x.shape[1]))
        for i in np.unique(y):
            sampled = x[y==i, :]
            one_class = np.mean(sampled)
            diffs = []
            for j in range(sampled.shape[0]):
                diffs += [sampled[j, :] - one_class]
            diffs = np.array(diffs).T
            scatter = np.array(np.dot(diffs[:, 0].reshape(-1, 1), diffs[:, 0].T.reshape(1, -1)))
            for j in range(1, diffs.shape[1]):
                scatter += np.array(np.dot(diffs[:, j].reshape(-1, 1), diffs[:, j].T.reshape(1, -1)))
            scatter = scatter/(diffs.shape[1])
            within_class_scatter += scatter
        # print(within_class_scatter)
        return within_class_scatter



    def fit(self, x, y):
        self.w = []
        inside = self.in_between(x, y)
        between = self.between_class(x, y)
        combine = np.dot(np.linalg.inv(inside), between)
        eigenvalues, eigenvectors = np.linalg.eig(combine)
        for i in eigenvectors:
            self.w += [i]
        self.w = np.array(self.w)

    def transform(self, x):
        return np.dot(x, self.w.T)



if __name__ == '__main__':
    df = pd.read_csv(r'breast-cancer.csv')
    le = LabelEncoder()
    df['diagnosis'] = le.fit_transform(df['diagnosis'])
    # sc = StandardScaler()
    x = df.iloc[:, [3, 4]].values
    # x = sc.fit_transform(x)
    y = df.iloc[:, 1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    lda = LDA()
    _lda = LinearDiscriminantAnalysis()
    _lda.fit(x_train, y_train)
    lda.fit(x_train, y_train)
    hat = lda.transform(x_test)
    ty = [x_test, hat]
    fig, axes = plt.subplots(nrows=1, ncols=2)
    # plt.plot(sorted(hat[:, 0]), hat[:, 1])
    for j in range(2):
        for i in np.unique(y_test):
            axes[j].scatter(ty[j][y_test==i, 0], ty[j][y_test==i, 1])
    tup = _lda.predict(x_test)
    plt.show()