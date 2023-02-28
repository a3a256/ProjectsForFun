import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class LGRegression:
    def __init__(self, n_iter=100):
        self.weights = None
        self.iters = n_iter


    def fit(self, x, y):
        self.weights = [[1e-5]*x.shape[1]]
        self.weights = np.array(self.weights)
        for _ in range(self.iters):
            g = self.predict_probe(x)
            w = np.eye(x.shape[0])
            pred_diff = y.reshape(-1, 1) - g
            pred_diff_shift = np.dot(np.linalg.inv(w), pred_diff)
            equation = np.dot(x, self.weights.T)
            z = equation + pred_diff_shift
            inv_bracket = np.linalg.inv(np.dot(np.dot(x.T, w), x))
            released = np.dot(inv_bracket, x.T)
            self.weights = np.dot(np.dot(released, w), z).T


    
    def predict_probe(self, x):
        equation = np.dot(x, self.weights.T)
        exponent = np.exp(equation)
        return exponent/(1+exponent)
    

    def predict(self, x):
        preds = self.predict_probe(x)
        values = [1 if i[0] > 0.5 else 0 for i in preds]
        return np.array(values)






if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')
    df.drop("id", axis=1, inplace=True)
    le = LabelEncoder()
    le.fit(df.iloc[:, 0])
    df.iloc[:, 0] = le.transform(df.iloc[:, 0])
    x = df.iloc[:, 1:4].values
    # sc = StandardScaler()
    # x = sc.fit_transform(x)
    y = df.iloc[:, 0].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    lr = LGRegression()
    lr.fit(x_train, y_train)
    lg = LogisticRegression()
    lg.fit(x_train, y_train)
    print(lg.coef_)
    y_hat = lg.predict(x_test)
    y_pred = lr.predict(x_test)
    print("Real model: ", accuracy_score(y_hat, y_test))
    print("Implemented: ", accuracy_score(y_pred, y_test))