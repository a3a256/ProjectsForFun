import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class OLS:
    def __init__(self):
        self.b = None


    def fit(self, x, y):
        self.b = np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y.reshape(-1, 1))
    
    def predict(self, x):
        return np.dot(x, self.b)



def real_dataset():
    df = pd.read_csv(r'breast-cancer.csv')
    lr = LinearRegression()
    # sc = StandardScaler()
    x = df.iloc[:, 2:6].values
    # x = sc.fit_transform(x)
    y = df.iloc[:, 7].values
    # y = le.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    lr1 = OLS()
    lr.fit(x_train, y_train)
    lr1.fit(x_train, y_train)
    yhat = lr1.predict(x_test)
    real = lr.predict(x_test)
    print("Implemented:", mean_squared_error(yhat, y_test))
    print("Real: ", mean_squared_error(real, y_test))
    fig, axes = plt.subplots(nrows=1, ncols=3)
    axes[0].scatter(x_test[:, 0], y_test)
    axes[0].set_title("Original")
    axes[1].scatter(x_test[:, 0], yhat)
    axes[1].set_title("Implemented")
    axes[2].scatter(x_test[:, 0], real)
    axes[2].set_title("Real model")
    plt.show()
    
if __name__ == '__main__':
    real_dataset()
