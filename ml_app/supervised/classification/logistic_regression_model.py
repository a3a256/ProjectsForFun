from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import sys
sys.path.insert(0, r'\ml_app')
from dimensions import get_dimensions

import matplotlib.pyplot as plt
import seaborn as sns

class LogisticClassifier:
    def __init__(self, x, y, col_names, target):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, random_state=42, test_size=0.2)
        self.cols = col_names
        self.target = target
        self.model = None

    def train(self):
        self.model = LogisticRegression()
        self.model.fit(self.x_train, self.y_train)
        self.test()

    def test(self):
        y_hat = self.model.predict(self.x_test)
        plt.figure(figsize=(5, 4))
        sns.heatmap(confusion_matrix(y_hat, self.y_test), annot=True)
        plt.title("LogisticRegression: {}% accuracy".format(round(accuracy_score(y_hat, self.y_test)*100, 2)))
        dims = get_dimensions(self.x_test.shape[1]-1)
        width, height = dims
        print(dims)
        fig, axes = plt.subplots(ncols=width, nrows=height, figsize=(10, 4))
        v = 0
        plt.figure(figsize=(6, 3))
        for i in np.unique(y_hat):
            plt.scatter(self.x_test[y_hat==i, 0], self.x_test[y_hat==i, 1])
        if height > 1:
            for i in range(height):
                for j in range(width):
                    for k in np.unique(self.y_test):
                        axes[i][j].scatter(self.x_test[y_hat==k, v], self.x_test[y_hat==k, -1])
                    axes[i][j].legend(np.unique(self.y_test))
                    v += 1
        else:
            for j in range(width):
                for k in np.unique(self.y_test):
                    axes[j].scatter(self.x_test[y_hat==k, v], self.x_test[y_hat==k, -1])
                axes[j].legend(np.unique(self.y_test))
                v += 1
        plt.tight_layout()
        plt.show()
