import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import LabelEncoder
import numpy.linalg as LA
from sklearn.linear_model import LogisticRegression

class OneLogisticRegression:
    def __init__(self, alpha=0.01):
        self.alpha = alpha
        self.b1 = 0
        self.b0 = 0

    def log_func(self, x, b1, b0):
        y = b0 + np.dot(b1, x)
        exponent = np.exp(y)
        outcome = (exponent)/(1 + exponent)
        return outcome

    def fit(self, x, y):
        k = 0
        for _ in range(20):
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
            eq = initial - np.dot(information, u)
            self.b0 = eq[0]
            self.b1 = eq[1]
        print(self.b0)
        print(self.b1)



if __name__ == "__main__":
    df = pd.read_csv(r'C:\Users\Azamat.Ilyasov\OneDrive - Optomany Ltd\Desktop\new_sll\breast-cancer.csv')
    df.drop("id", axis=1, inplace=True)
    le = LabelEncoder()
    le.fit(df.iloc[:, 0])
    df.iloc[:, 0] = le.transform(df.iloc[:, 0])
    x = df.iloc[:, 1].values
    y = df.iloc[:, 0].values
    lr = OneLogisticRegression()
    lr.fit(x.reshape(-1, 1), y)
    lg = LogisticRegression(fit_intercept=True)
    lg.fit(x.reshape(-1, 1), y)
    print(lg.coef_)
    print(lg.intercept_)