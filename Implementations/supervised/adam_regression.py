import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import random

class Regression:
    def __init__(self, alpha=0.001, fit_intercept=False, n_iter = 20):
        self.w = None
        self.alpha = alpha
        self.iters = n_iter
        self.b1 = 0.9
        self.b2 = 0.999
        self.epsilon = 10**(-8)

    def fit(self, x, y):
        self.w = np.array([abs(np.random.normal(0, 0.01, 1)) for _ in range(x.shape[1])])
        for _ in range(self.iters):
            m0 = 0
            v0 = 0
            t = 0
            for i in range(x.shape[0]):
                t += 1
                g = [self.w[j]*x[i, j] for j in range(len(self.w))]
                g = np.array(g)
                m0 = self.b1*m0 + (1-self.b1)*g
                v0 =self.b2*v0 + (1-self.b2)*np.square(g)
                mhat = m0/(1-self.b1**t)
                vhat = v0/(1-self.b2**t)
                self.w -= (self.alpha*mhat)/(np.sqrt(vhat)+self.epsilon)
        
        # print(self.w.reshape(1, -1))

    def predict(self, x):
        return np.dot(x, self.w)


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
    yhat = lr.predict(x_test)
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