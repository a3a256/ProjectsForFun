from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np



class RidgeClassify:
    def __init__(self, alpha=1, n_iters=100):
        self.alpha = alpha
        self.iters = n_iters
        self.weights = None


    def fit(self, x, y):
        # y_modern = [1 if i == 1 else -1 for i in y]
        # y_modern = np.array(y_modern)
        self.weights = [[1e-5]*x.shape[1]]
        self.weights = np.array(self.weights)
        iden = np.eye(x.shape[1])
        for _ in range(self.iters):
            g = self.predict_probe(x)
            w = np.eye(x.shape[0])
            pred_diff = y.reshape(-1, 1) - g
            pred_diff_shift = np.dot(np.linalg.inv(w), pred_diff)
            equation = np.dot(x, self.weights.T)
            z = equation + pred_diff_shift
            v = np.dot(np.dot(x.T, w), x) + self.alpha*iden
            first = np.dot(np.linalg.inv(v), x.T)
            self.weights = np.dot(np.dot(first, w), z).T




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
    lr = RidgeClassify()
    lr.fit(x_train, y_train)
    lg = RidgeClassifier()
    lg.fit(x_train, y_train)
    print(lg.coef_)
    y_hat = lg.predict(x_test)
    y_pred = lr.predict(x_test)
    print("Real model: ", accuracy_score(y_hat, y_test))
    print("Implemented: ", accuracy_score(y_pred, y_test))