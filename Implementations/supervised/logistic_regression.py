import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import LabelEncoder
import numpy.linalg as LA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class OneLogisticRegression:
    def __init__(self, alpha=0.001):
        self.alpha = alpha
        self.b1 = None
        self.b0 = None

    def log_func(self, x, b1, b0):
        y = b0 + np.dot(b1, x)
        exponent = np.exp(y)
        outcome = (exponent)/(1 + exponent)
        return outcome

    def _fit(self, x, y):
        k = 0
        for _ in range(100):
            initial = np.array([self.b0, self.b1])
            p = self.log_func(x, self.b1, self.b0)
            b0 = np.sum(y-p)
            b1 = np.sum(np.dot(y, x) - np.dot(x.T, p))
            u = np.array([b0, b1])
            up_left = np.sum(np.dot(p.T, (1-p)))
            up_right = np.sum(np.dot(np.dot(x.T, p), (1-p).T))
            low_right = np.sum(np.dot(np.dot(np.power(x, 2).T, p), (1-p).T))
            information = np.array([[up_left, up_right], [up_right, low_right]])
            eq = None
            if LA.det(information) != 0:
                information = -LA.matrix_power(information, -1)
                eq = initial - np.dot(LA.matrix_power(information, -1), u)
            eq = initial - self.alpha*np.dot(information, u)
            self.b0 = eq[0]
            self.b1 = eq[1]

    def fit(self, x, y):
        n_samples, n_features = x.shape
        self.b0, self.b1 = 0, np.zeros(n_features)
        for _ in range(5):
            yhat = np.dot(x, self.b1) - self.b0
            lg = self._sigmoid(yhat)
            error = yhat - y
            self.b1 -= self.alpha*(1/n_samples)*(np.dot(x.T, error))
            self.b0 -= self.alpha*(1/n_samples)*(np.sum(error))

        print(self.b1)

    def _sigmoid(self, x):
        return 1/(1-np.exp(-x))

    def prediction(self, x):
        y = [0 if i < 0.5 else 1 for i in self._sigmoid(np.dot(x, self.b1) - self.b0)]
        return y


    def _prediction(self, x):
        y = [0 if i < 0.5 else 1 for i in self.log_func(x, self.b1, self.b0)]
        return y



if __name__ == "__main__":
    df = pd.read_csv(r'C:\Users\Azamat.Ilyasov\OneDrive - Optomany Ltd\Desktop\new_sll\breast-cancer.csv')
    df.drop("id", axis=1, inplace=True)
    le = LabelEncoder()
    le.fit(df.iloc[:, 0])
    df.iloc[:, 0] = le.transform(df.iloc[:, 0])
    x = df.iloc[50:, 1:4].values
    y = df.iloc[50:, 0].values
    x_test = df.iloc[:50, 1:4].values
    y_test = df.iloc[:50, 0].values
    lr = OneLogisticRegression()
    lr.fit(x, y)
    lg = LogisticRegression()
    lg.fit(x, y)
    print(lg.coef_)
    y_hat = lg.predict(x_test)
    y_pred = lr.prediction(x_test)
    print(accuracy_score(y_hat, y_test))
    print(accuracy_score(y_pred, y_test))
