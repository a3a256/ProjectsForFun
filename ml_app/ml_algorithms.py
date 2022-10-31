from tkinter import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from dimensions import get_dimensions

class MLOptions:
    def __init__(self, ui, path, selection, dataframe):
        self.ui = ui
        self.path = path
        self.selection = selection
        self.target = None
        self.df = dataframe
        self.x = None
        self.y = None
        self.message = ""

    def give_target(self, target):
        self.target = target.cget("text")
        self.selection.remove(self.target)
        return

    def regression_distribute(self):
        if self.message == "LinearRegression":
            su = SupervisedRegression(self.x, self.y, self.selection, self.target)
            su.linear_regression()
            return

    def get_x_y(self, x_axis, y_axis):
        self.x = self.df.loc[:, x_axis].values
        self.y = self.df.loc[:, y_axis].values
        self.regression_distribute()
        return

    def target_select(self, message):
        self.message = message
        lb = Label(master=self.ui, text="Choose the target feature!")
        lb.grid(row=0, column=0)
        for i in range(len(self.selection)):
            b = Button(master=self.ui, text=self.selection[i])
            b.grid(row=1, column=i)
            b.configure(command=lambda x=b: [self.give_target(x), self.get_x_y(self.selection, self.target)])

    def regression_options(self):
        btn_regression = Button(self.ui, text="Linear Regression", command=lambda: [btn_regression.destroy(), self.target_select("LinearRegression")])
        btn_regression.grid(row=0, column=0)

    def supervised(self):
        btn_classification = Button(master=self.ui, text="Classification")
        btn_classification.grid(row=0, column=0)
        btn_regression = Button(master=self.ui, text="Regression", command=lambda: [btn_classification.destroy(), btn_regression.destroy(), self.regression_options()])
        btn_regression.grid(row=1, column=0)

    def port(self):
        btn_supervised = Button(master=self.ui, text="Supervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy(), self.supervised()])
        btn_supervised.grid(row=0, column=0)
        btn_unsupervised = Button(master=self.ui, text="Unsupervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy()])
        btn_unsupervised.grid(row=1, column=0)
        self.ui.mainloop()



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
