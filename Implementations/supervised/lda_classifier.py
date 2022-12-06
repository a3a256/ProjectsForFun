import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


class LDAClassifier:
    def __init__(self):
        self.covariances = []
        self.means = []
        self.priors = []

    def fit(self, x, y):
        counts = np.bincount(y)
        self.priors = [counts[i]/len(x) for i in range(len(counts))]
        for i in np.unique(y):
            self.means += [np.mean(x[y==i, :], axis=0).reshape(-1, 1)]
            self.covariances += [np.cov(x[y==i, :].T)]

    def predict(self, x):
        if len(self.priors) == 2:
            return self.predict_binary(x)
        else:
            return self.predict_multi(x)

    def multi_equation(self, x):
        res = []
        for i in range(self.priors):
            first = np.dot(np.dot(self.means[i].T, np.linalg.inv(self.covariances[i])), x.T)
            second = 0.5*np.dot(np.dot(self.means[i].T, np.linalg.inv(self.covariances[i])), self.means[i])
            end = np.log(self.priors[i])
            res += [first-second+end]
        return np.argmax(res)

    def predict_multi(self, x):
        res = []
        for i in range(len(x)):
            res += [self.multi_equation(x[i, :])]
        return res

    def predict_binary(self, x):
        res = []
        answers = []
        kk = (self.means[0]-self.means[1]).T
        first_part = np.dot(2*np.dot(np.linalg.inv(self.covariances[i]), (self.means[0] - self.means[1])).T, x.T)
        second_part = np.dot(np.dot((self.means[0]-self.means[1]).T, np.linalg.inv(self.covariances[i])), (self.means[0]-self.means[1]))
        end = 2*np.log(self.priors[1]/self.priors[0])
        res += [first_part+second_part+end]
        answers = [0 if i > 0 else 1 for i in res[0][0]]
        return answers


if __name__ == '__main__':
    df = pd.read_csv(r'breast-cancer.csv')
    lda = LDAClassifier()
    le = LabelEncoder()
    sc = StandardScaler()
    df['diagnosis'] = le.fit_transform(df['diagnosis'])
    x = df.iloc[:, [2, 3]].values
    x = sc.fit_transform(x)
    y = df.iloc[:, 1].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    ld = LinearDiscriminantAnalysis()
    ld.fit(x_train, y_train)
    lda.fit(x_train, y_train)
    yhat = lda.predict(x_test)
    real = ld.predict(x_test)
    print("Implemented:", accuracy_score(yhat, y_test))
    print("Real: ", accuracy_score(real, y_test))
