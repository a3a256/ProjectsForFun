import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import random

class Regression:
    def __init__(self, alpha=0.01, fit_intercept=False, n_iter = 1000):
        self.m = None
        self.alpha = alpha
        self.iters = n_iter

    def fit(self, x, y):
        n_samples, n_features = x.shape
        # self.m = np.random.rand(n_features)
        self.m = np.array([random.random()]*n_features)
        for j in range(self.iters):
            for i in range(n_samples):
                y_hat = self.solve(x[i, :], self.m)
                loss = 2*y_hat*(y_hat-y[i])
                for k in range(n_features):
                    self.m[k] -= self.alpha*(loss*self.m[k])
                # grad = y_hat*(y[i] - y_hat)
            if j%100 == 0:
                print("Loss: ", loss)
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

    def predict1(self, x):
        a = x.dot(self.m)
        return a

    def solve(self, x, weight):
        return np.dot(x, weight.T)


if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    df = df.dropna()
    sc = StandardScaler()
    x = df.iloc[:, 2:7].values
    x = sc.fit_transform(x)
    y = df.iloc[:, 7].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    l1 = LinearRegression()
    l1.fit(x_train, y_train)
    lr = Regression()
    lr.fit(x_train, y_train)
    yhat = lr.predict1(x_test)
    pred = l1.predict(x_test)
    print("Implemnted: ", mean_squared_error(y_test, yhat))
    print("Real: ", mean_squared_error(y_test, pred))
    fig, axes = plt.subplots(nrows=1, ncols=3)
    axes[0].scatter(x_test[:, 0], y_test)
    axes[0].set_title("Original")
    axes[1].scatter(x_test[:, 0], yhat)
    axes[1].set_title("Implemented")
    axes[2].scatter(x_test[:, 0], pred)
    axes[2].set_title("Real model")
    plt.show()
