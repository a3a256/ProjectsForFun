import matplotlib.pyplot as plt
import pandas as pd
from corr import Correlation

class Plotting:
    def __init__(self, df, vars=None):
        self.data = df
        self.vals = 0
        if vars is None:
            self.vals = df.columns
        else:
            self.vals = vars
        self.fig, self.axes = plt.subplots(nrows=len(self.vals), ncols=len(self.vals), figsize=(50, 50))

    def plot(self):
        axes = self.axes
        length = len(self.vals)
        df = self.data
        for i in range(length):
            for j in range(length):
                axes[i][j].scatter(df[self.vals[i]], df[self.vals[j]])
                cor = Correlation(df[self.vals[i]], df[self.vals[j]]).correlate()
                axes[i][j].set_title(label=f'cor={round(cor, 2)}')
        plt.tight_layout()
        plt.show()