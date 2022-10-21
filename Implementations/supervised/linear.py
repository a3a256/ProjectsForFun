import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class LinearRgeression:
    def __init__(self, x, y, alpha=0.01):
        self.x = x
        self.y = y
        self.n_samples, self.n_features = self.x.shape
        self.alpha = alpha
        self.n, self.m = 0, np.zeros(self.n_features)

    def fit(self):
        for j in range(50):
            y_hat = self.solve(self.x, self.m, self.n)
            error = self.y - y_hat
            grad = np.dot(self.x.T, error)
            dw = (1/self.n_samples) * grad
            db = (1/self.n_samples) * np.sum(error)
            self.m -= self.alpha*dw
            self.n -= self.alpha*db
        print(self.m)

    def predict1(self, x):
        a = x.dot(self.m) + self.n
        return a

    def solve(self, x, weight, bias):
        return np.dot(x, weight) + bias


def r2_score(y_true, y_pred):
        corr_matrix = np.corrcoef(y_true, y_pred)
        corr = corr_matrix[0, 1]
        return corr ** 2

if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    df = df.dropna()
    x = df.iloc[:, 2:5].values
    y = df.iloc[:, 7].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    l1 = LinearRegression()
    l1.fit(x_train, y_train)
    print(l1.coef_)
    lr = LinearRgeression(x_train, y_train)
    lr.fit()
    yhat = lr.predict1(x_test)
    pred = l1.predict(x_test)
    print(r2_score(y_test, yhat))
    print(r2_score(y_test, pred))