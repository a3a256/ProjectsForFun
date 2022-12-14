import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import LabelEncoder
import numpy.linalg as LA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class OneLogisticRegression:
    def __init__(self, alpha=0.001, n_iters=200):
        self.alpha = alpha
        self.b1 = None
        self.b0 = None
        self.a1 = 0.999
        self.a2 = 0.9
        self.n_iters = n_iters
        self.epsilon = 10**(-8)

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
        self.b1 = np.array([0.00001]*n_features)
        self.b1 = np.random.rand(n_features)
        for i in range(self.n_iters):
            for j in range(n_samples):
                yhat = np.dot(x[j, :], self.b1.T)
                error = 0
                if y[j] == 0:
                    error = 1/(1-yhat)
                else:
                    error = -(1/yhat)
                self.b1 -= self.alpha*error*self.b1
            if i%1000 == 0:
                print("Loss: ", error)
        
        print(self.b1)
    
    def adam_fit(self, x, y):
        n_samples, n_features = x.shape
        self.b1 = np.array([abs(np.random.normal(0, 0.0001, 1)) for _ in range(n_features)])
        self.b1 = self.b1.T
        for _ in range(self.n_iters):
            m0 = 0
            v0 = 0
            t = 0
            for i in range(n_samples):
                t += 1
                c = np.dot(x[i, :], self.b1.T)
                g = self._sigmoid(c)
                if y[i] == 0:
                    g = 1/(1-g)
                else:
                    g = -(1/g)
                m0 = self.a1*m0 + (1-self.a1)*g
                v0 =self.a2*v0 + (1-self.a2)*np.square(g)
                mhat = m0/(1-self.a1**t)
                vhat = v0/(1-self.a2**t)
                self.b1 -= (self.alpha*mhat)/(np.sqrt(vhat) + self.epsilon)

    def failed_fit(self, x, y):
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
        y = [0 if i < 0.5 else 1 for i in self._sigmoid(np.dot(x, self.b1.T))]
        return y


    def _prediction(self, x):
        y = [0 if i < 0.5 else 1 for i in self.log_func(x, self.b1, self.b0)]
        return y



if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    df.drop("id", axis=1, inplace=True)
    le = LabelEncoder()
    le.fit(df.iloc[:, 0])
    df.iloc[:, 0] = le.transform(df.iloc[:, 0])
    x = df.iloc[:, 1:4].values
    sc = StandardScaler()
    x = sc.fit_transform(x)
    y = df.iloc[:, 0].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    lr = OneLogisticRegression()
    lr.adam_fit(x_train, y_train)
    lg = LogisticRegression()
    lg.fit(x_train, y_train)
    print(lg.coef_)
    y_hat = lg.predict(x_test)
    y_pred = lr.prediction(x_test)
    print("Real model: ", accuracy_score(y_hat, y_test))
    print("Implemented: ", accuracy_score(y_pred, y_test))
    # print(y_test)
    # print(y_pred)
