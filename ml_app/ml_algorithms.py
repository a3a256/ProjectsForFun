from tkinter import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from dimensions import get_dimensions
from supervised.classification import naive_bayes_model
from supervised.classification import logistic_regression_model
from supervised.classification import knn_classifier_model
from supervised.regression import linear_regression

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
        self.spec = ""
        self.n = None

    def give_target(self, target):
        self.target = target.cget("text")
        self.selection.remove(self.target)
        return

    def regression_distribute(self):
        if self.message == "LinearRegression":
            su = linear_regression.SupervisedRegression(self.x, self.y, self.selection, self.target)
            su.linear_regression()
            return

    def get_x_y(self, x_axis, y_axis):
        self.x = self.df.loc[:, x_axis].values
        self.y = self.df.loc[:, y_axis].values
        if self.spec == "Regression":
            self.regression_distribute()
        elif self.spec == "Classification":
            self.classification_distribute()
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
        self.spec = "Regression"
        btn_regression = Button(self.ui, text="Linear Regression", command=lambda: [btn_regression.destroy(), self.target_select("LinearRegression")])
        btn_regression.grid(row=0, column=0)

    def get_neighbors(self, m):
        self.n = str(m)
        return

    def classification_distribute(self):
        if self.message == "GaussianNB":
            nb = naive_bayes_model.BayesClassifier(self.x, self.y, self.selection, self.target)
            nb.train()
            return
        if self.message == "LogisticRegression":
            lr = logistic_regression_model.LogisticClassifier(self.x, self.y, self.selection, self.target)
            lr.train()
            return
        if self.message == "KNN":
            n = None
            en_neighbors = Entry(self.ui, text="")
            en_neighbors.grid(row=0, column=0)
            btn_neighbors = Button(self.ui, text="Enter neighbors", command=lambda: [en_neighbors.destroy(), btn_neighbors.destroy(), self.get_neighbors(en_neighbors.get())])
            btn_neighbors.grid(row=0, column=1)
            knn = knn_classifier_model.KNN(self.x, self.y, self.selection, self.target, self.n)
            knn.train()
            return

    def classification_option(self):
        self.spec = "Classification"
        btn_gaussiannb = Button(self.ui, text="GaussianNB", command=lambda: [btn_gaussiannb.destroy(), btn_lgregression.destroy(), self.target_select("GaussianNB")])
        btn_gaussiannb.grid(row=0, column=0)
        btn_lgregression = Button(self.ui, text="LogisticRegression", command=lambda: [btn_gaussiannb.destroy(), btn_lgregression.destroy(), self.target_select("LogisticRegression")])
        btn_lgregression.grid(row=1, column=0)
        btn_knn = Button(self.ui, text="KNearestNeighbors", command=lambda: [btn_gaussiannb.destroy(), btn_lgregression.destroy(), btn_knn.destroy(), self.target_select("KNN")])
        btn_knn.grid(row=2, column=0)

    def supervised(self):
        btn_classification = Button(master=self.ui, text="Classification", command=lambda: [btn_classification.destroy(), btn_regression.destroy(), self.classification_option()])
        btn_classification.grid(row=0, column=0)
        btn_regression = Button(master=self.ui, text="Regression", command=lambda: [btn_classification.destroy(), btn_regression.destroy(), self.regression_options()])
        btn_regression.grid(row=1, column=0)

    def port(self):
        btn_supervised = Button(master=self.ui, text="Supervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy(), self.supervised()])
        btn_supervised.grid(row=0, column=0)
        btn_unsupervised = Button(master=self.ui, text="Unsupervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy()])
        btn_unsupervised.grid(row=1, column=0)
        self.ui.mainloop()
