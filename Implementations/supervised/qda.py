import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split


class QDA:
    def __init__(self):
        self.covariances = []
        self.means = []
        self.priors = []


    def fit(self, x, y):
        freqs = np.bincount(y)
        for i, j in enumerate(np.unique(y)):
            self.priors += [freqs[i]/len(x)]
            self.means += [np.mean(x[y==j, :], axis=0)]
            self.covariances += [np.cov(x.T)]
        print(self.covariances[0])


    def predict_binary(self, x):
        for i in range(len(x)):
            val = x[i, :].reshape(1, -1)
            first = np.dot(val, np.dot(np.linalg.inv(self.covariances[0]-self.covariances[1]), val.T))
            print(self.means[0].shape)
            break
            # first = np.dot()



if __name__ == '__main__':
    df = pd.read_csv(r'pima-indians-diabetes.csv')
    qda = QDA()
    le = LabelEncoder()
    # sc = StandardScaler()
    x = df.iloc[:, :-1].values
    # x = sc.fit_transform(x)
    y = df.iloc[:, -1].values
    y = le.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    qd = QuadraticDiscriminantAnalysis()
    qd.fit(x_train, y_train)
    qda.fit(x_train, y_train)
    yhat = qda.predict_binary(x_test)
    # real = qd.predict(x_test)
    # print("Implemented:", accuracy_score(yhat, y_test))
    # print("Real: ", accuracy_score(real, y_test))