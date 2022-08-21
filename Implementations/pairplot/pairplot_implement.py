import matplotlib.pyplot as plt
import pandas as pd

class Pairplot:
    def __init__(self, df, vars=None, corner=True, hue=None):
        self.flag = corner
        self.data = df
        self.vars = 0
        if vars is None:
            self.vars = df.columns
        else:
            self.vars = vars
        self.x = len(self.vars)
        self.fig, self.axes = plt.subplots(nrows=self.x, ncols=self.x)

    def draw(self):
        if self.flag:
            self.draw_corner()
        else:
            self.draw_no_corner()

    def draw_no_corner(self):
        axes = self.axes
        x = self.vars
        y = self.vars
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    axes[i][j].hist(self.data[x[i]], bins=15)
                elif j > i:
                    axes[i][j].axis("off")
                else:
                    axes[i][j].scatter(self.data[x[i]], self.data[y[j]])
        plt.show()
    
    def draw_corner(self):
        axes = self.axes
        x = self.vars
        y = self.vars
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    axes[i][j].hist(self.data[x[i]], bins=15)
                else:
                    axes[i][j].scatter(self.data[x[i]], self.data[y[j]])
        plt.show()