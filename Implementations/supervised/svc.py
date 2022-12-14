import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class SVM:
    def __init__(self, C=0.001, alpha=0.001, fit_intercept=False, n_iters=100):
        self.alpha = alpha
        self.C = C
        self.w = None
        self.bias = None
        self.intercept = fit_intercept
        self.iter = n_iters

    def fit(self, x, y):
        n_samples, n_features = x.shape
        count = 0
        if self.intercept:
            self.bias = np.random.rand(1)
        self.w = np.random.rand(n_features)
        
        for _ in range(self.iter):
            for i in range(n_samples):
                yhat = self.equation(x[i, :], self.w, self.bias)
                error = 1 - y[i]*yhat
                grad = 0
                if error <= 0:
                    grad = self.w
                else:
                    grad = self.w - self.C*y[i]*x[i, :]
                self.w -= self.alpha*grad
                if self.intercept:
                    self.bias -= self.alpha*(1/n_samples) * np.sum(error)
    
    def fit_adam(self, x, y):
        b1 = 0.999
        b2 = 0.9
        n_samples, n_features = x.shape
        if self.intercept:
            self.bias = np.random.rand(1)
        self.w = np.random.rand(n_features)
        
        for _ in range(self.iter):
            m0 = 0
            v0 = 0
            t = 0
            for i in range(n_samples):
                t += 1
                yhat = self.equation(x[i, :], self.w, self.bias)
                error = 1 - y[i]*yhat
                grad = 0
                if error <= 0:
                    grad = self.w
                else:
                    grad = self.w - self.C*y[i]*x[i, :]
                m0 = b1*m0 + (1-b1)*grad
                v0 = b2*v0 + (1-b2)*np.square(grad)
                mhat = m0/(1-b1**t)
                vhat = v0/(1-b2**t)
                self.w -= (self.alpha*mhat)/(np.sqrt(vhat)+10**(-8))
                if self.intercept:
                    self.bias -= self.alpha*(1/n_samples) * np.sum(error)


    def equation(self, x, w, b=None):
        if self.intercept:
            return np.dot(x, w) - b

        else:
            return np.dot(x, w)


    def predict(self, x):
        predict = self.equation(x, self.w, self.bias)
        for i in range(len(x)):
            if predict[i] < 0:
                predict[i] = -1
            elif predict[i] > 0:
                predict[i] = 1
        return predict



if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    df.drop("id", axis=1, inplace=True)
    df.dropna(inplace=True)
    le = LabelEncoder()
    le.fit(df.iloc[:, 0])
    df.iloc[:, 0] = le.transform(df.iloc[:, 0])
    for i in range(len(df)):
        df.iloc[i, 0] = -1 if df.iloc[i, 0] == 0 else 1
    x = df.iloc[:, [1, 2]].values
    sc = StandardScaler()
    x = sc.fit_transform(x)
    y = df.iloc[:, 0].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    sv = SVM()
    sv.fit_adam(x_train, y_train)
    print("Implemented: {}".format(accuracy_score(y_test, sv.predict(x_test))))
    svc = SVC(C=0.001, kernel="linear")
    svc.fit(x_train, y_train)
    print("Real SVC: {}".format(accuracy_score(y_test, svc.predict(x_test))))
