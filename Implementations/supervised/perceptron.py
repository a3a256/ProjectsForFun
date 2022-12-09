import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, n_iter=20, lr=0.9):
        self.w = []
        self.b = []
        self.alpha = lr
        self.epochs = n_iter

    def fit(self, x, y):
        self.w = np.array([abs(np.random.normal(0, 0.01, 1)) for i in range(x.shape[1])])
        self.b = np.array([abs(np.random.normal(0, 0.01))])
        for i in range(self.epochs):
            er = 0
            for j in range(x.shape[0]):
                pred = np.dot(x[j, :], self.w) + self.b
                activate = self.relu(pred)
                error = y[j] - activate
                print(error)
                er += error
                self.w += error*x[j, :].reshape(-1, 1)
                self.b += error
            # print(error/len(x))


    def relu(self, x):
        return x if x>0 else 0

    def predict(self, x):
        preds = []
        for i in range(len(x)):
            preds += [self.relu(np.dot(x[i, :], self.w)+self.b)]
            # preds += [np.dot(x[i, :], self.w)+self.b]
        return np.array(preds)


if __name__ == "__main__":
    perceptron = Perceptron()
    df = pd.read_csv(r'breast-cancer.csv')
    x = df.iloc[:, [3, 4]].values
    y = df.iloc[:, 1].values
    le = LabelEncoder()
    lg = LogisticRegression()
    sc1 = StandardScaler()
    sc2 = StandardScaler()
    x = sc1.fit_transform(x)
    y = le.fit_transform(y)
    lr = LinearRegression()
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    perceptron.fit(x_train, y_train)
    lr.fit(x_train, y_train)
    lg.fit(x_train, y_test)
    hat = perceptron.predict(x_test)
    test = lg.predict(x_test)
    print(accuracy_score(hat, y_test))
    print(accuracy_score(y_test, test))