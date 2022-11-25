import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class LinearRgeression:
    def __init__(self, alpha=0.01, fit_intercept=False, n_iter = 500):
        self.m = None
        self.alpha = alpha
        self.iters = n_iter

    def fit(self, x, y):
        n_samples, n_features = x.shape
        # self.m = np.random.rand(n_features)
        self.m = np.array([0.0001]*n_features)
        for j in range(self.iters):
            for i in range(n_samples):
                y_hat = self.solve(x[i, :], self.m)
                grad = -2*self.m*(y[i] - y_hat)
                self.m -= self.alpha*grad
        print(self.m)

    def fit_failed(self, x, y):
        n_samples, n_features = x.shape
        self.m = np.random.rand(n_features)
        for j in range(self.iters):

            y_hat = self.solve(self.x, self.m, self.n)
            error = self.y - y_hat
            grad = np.dot(self.x.T, error)
            dw = (1/self.n_samples) * grad
            db = (1/self.n_samples) * np.sum(error)
            self.m -= self.alpha*dw
            self.n -= self.alpha*db
        print(self.m)

    def predict1(self, x):
        a = x.dot(self.m)
        return a

    def solve(self, x, weight):
        return np.dot(x, weight.T)


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
    lr = LinearRgeression()
    lr.fit(x_train, y_train)
    yhat = lr.predict1(x_test)
    pred = l1.predict(x_test)
    print(r2_score(y_test, yhat))
    print(r2_score(y_test, pred))
