import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import sys
sys.path.insert(0, r'C:\Users\Azamat.Ilyasov\OneDrive - Optomany Ltd\Desktop\ml_app')
from dimensions import get_dimensions

class SupervisedRegression:
    def __init__(self, x, y, col_names, target_name):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, random_state=42, test_size=0.2)
        self.model = None
        self.names = col_names
        self.target_name = target_name

    def linear_regression(self):
        self.model = LinearRegression()
        self.model.fit(self.x_train, self.y_train)
        self.testing()

    def testing(self):
        if len(self.names) == 1:
            y_hat = self.model.predict(self.x_test)
            plt.scatter(self.x_test, self.y_test)
            plt.scatter(self.x_test, y_hat)
            plt.xlabel(self.names[0])
            plt.ylabel(self.target_name)
            plt.title("Linear Regression r2_score: {}%".format(round(100*r2_score(y_hat, self.y_test), 2)))
            plt.show()
            return
        width, height = get_dimensions(len(self.names))
        print(width, height)
        y_hat = self.model.predict(self.x_test)
        fig, axes = plt.subplots(ncols=int(width), nrows=int(height), figsize=(9, 4))
        v = 0
        if height > 1:
            for i in range(height):
                for j in range(width):
                    axes[i][j].scatter(self.x_test[:, v], self.y_test)
                    axes[i][j].scatter(self.x_test[:, v], y_hat)
                    axes[i][j].set_xlabel(self.names[v])
                    axes[i][j].set_ylabel(self.target_name)
                    v += 1
        else:
            for i in range(width):
                axes[i].scatter(self.x_test[:, v], self.y_test)
                axes[i].scatter(self.x_test[:, v], y_hat)
                v += 1
        score = r2_score(y_hat, self.y_test)
        plt.suptitle("Linear Regression r2 score: {}%".format(round(100*score, 2)))
        plt.tight_layout()
        plt.show()