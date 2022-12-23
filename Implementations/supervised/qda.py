import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


class QDA:
    def __init__(self):
        self.covariances = []
        self.means = []
        self.priors = []


    def fit(self, x, y):
        freqs = np.bincount(y)
        for i, j in enumerate(np.unique(y)):
            self.priors += [freqs[i]/len(x)]
            self.means += [np.mean(x[y==j, :], axis=0)]
            self.covariances += [np.cov(x[y==j].T)]

        
    def multi_equation(self, x):
        res = []
        for i in range(len(self.priors)):
            first = -(1/2)*np.log(np.linalg.det(self.covariances[i]))
            sub2_1 = x - self.means[i]
            sub2_2 = np.linalg.inv(self.covariances[i])
            second = (1/2)*np.dot(np.dot(sub2_1.reshape(1, -1), sub2_2), sub2_1.reshape(-1, 1))
            third = np.log(self.priors[i])
            end = first - second + third
            res += [end]
        return np.argmax(res)


    def predict_binary(self, x):
        res = []
        for i in range(len(x)):
            res += [self.multi_equation(x[i, :])]
        
        return res


def real_dataset():
    df = pd.read_csv(r'breast-cancer.csv')
    qda = QDA()
    le = LabelEncoder()
    sc = StandardScaler()
    x = df.iloc[:, 2:6].values
    x = sc.fit_transform(x)
    y = df.iloc[:, 1].values
    y = le.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    qd = QuadraticDiscriminantAnalysis()
    qd.fit(x_train, y_train)
    qda.fit(x_train, y_train)
    yhat = qda.predict_binary(x_test)
    real = qd.predict(x_test)
    real = qd.predict(x_test)
    print("Implemented:", accuracy_score(yhat, y_test))
    print("Real: ", accuracy_score(real, y_test))


def iris():
    df = load_iris()
    qda = QDA()
    le = LabelEncoder()
    sc = StandardScaler()
    x = df.data
    x = sc.fit_transform(x)
    y = df.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    qd = QuadraticDiscriminantAnalysis()
    qd.fit(x_train, y_train)
    qda.fit(x_train, y_train)
    yhat = qda.predict_binary(x_test)
    real = qd.predict(x_test)
    real = qd.predict(x_test)
    print("Implemented:", accuracy_score(yhat, y_test))
    print("Real: ", accuracy_score(real, y_test))



if __name__ == '__main__':
    real_dataset()
    iris()
