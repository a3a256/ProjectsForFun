from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns

class BayesClassifier:
    def __init__(self, x, y, col_names, target):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, random_state=42, test_size=0.2)
        self.cols = col_names
        self.target = target
        self.model = None

    def train(self):
        self.model = GaussianNB()
        self.model.fit(self.x_train, self.y_train)
        self.test()

    def test(self):
        y_hat = self.model.predict(self.x_test)
        print(accuracy_score(y_hat, self.y_test))