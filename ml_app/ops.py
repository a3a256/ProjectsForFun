from tkinter import *
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

class PlotPanel:
    def __init__(self, ui, selection, df):
        self.df = df
        self.ui = ui
        self.selection = selection

    def scatter_plot(self):
        plot = ShowPlots(self.df[self.selection[0]], self.df[self.selection[1]])
        plot.scatterplot()

    def bar_plot(self):
        if len(self.selection) > 2:
            fig, ax = plt.subplots(nrows=1, ncols=len(self.selection), figsize=(10, 10))
            for i in range(len(self.selection)):
                ax[i].bar(self.df[self.selection[i]])
        elif len(self.selection) == 2:
            col1 = np.unique(self.df[self.selection[0]])
            col2 = np.unique(self.df[self.selection[1]])
            if len(col1) > len(col2):
                plt.bar(self.df[self.selection[1]], self.df[self.selection[0]])
            else:
                plt.bar(self.df[self.selection[0]], self.df[self.selection[1]])
        plt.show()
    
    def plot_options(self):
        btn_scatter = Button(self.ui, text="Scatterplot of selected columns", command=lambda: [self.ui.destroy() ,self.scatter_plot()])
        btn_scatter.grid(row=0, column=0)
        btn_bar = Button(self.ui, text="Barplot", command=lambda: [self.ui.destroy(), self.bar_plot()])
        btn_bar.grid(row=1, column=0)
        self.ui.mainloop()

class ShowPlots:
    def __init__(self, x_axis=None, y_axis=None, legend=None):
        self.x = x_axis
        self.y = y_axis
        self.legend = legend

    def scatterplot(self):
        plt.scatter(self.x, self.y)
        plt.show()
