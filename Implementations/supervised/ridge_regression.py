from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


class RidgeRegression:
    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.w = None


    def fit(self, x, y):
        identity = np.eye(x.shape[1])
        first = np.dot(x.T, x) + self.alpha*identity
        inverse = np.linalg.inv(first)
        second = np.dot(inverse, x.T)
        self.w = np.dot(second, y.reshape(-1, 1))

    def predict(self, x):
        return np.dot(x, self.w)
    



def real_dataset():
    df = pd.read_csv(r'breast-cancer.csv')
    lr = RidgeRegression(alpha=0.1)
    # sc = StandardScaler()
    x = df.iloc[:, 2:6].values
    # x = sc.fit_transform(x)
    y = df.iloc[:, 7].values
    # y = le.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    lr1 = RidgeRegression()
    lr.fit(x_train, y_train)
    lr1.fit(x_train, y_train)
    yhat = lr1.predict(x_test)
    real = lr.predict(x_test)
    print("Implemented:", mean_squared_error(yhat, y_test))
    print("Real: ", mean_squared_error(real, y_test))
    
if __name__ == '__main__':
    real_dataset()