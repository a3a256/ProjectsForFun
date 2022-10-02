from tkinter import *
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class PlotPanel:
    def __init__(self, ui, selection, df):
        self.df = df
        self.ui = ui
        self.selection = selection

    def scatter_plot(self):
        plot = ShowPlots(self.df[self.selection[0]], self.df[self.selection[1]])
        plot.scatterplot()
    
    def plot_options(self):
        btn_scatter = Button(self.ui, text="Scatterplot of selected columns", command=lambda: self.scatter_plot())
        btn_scatter.grid(row=0, column=0)
        btn_bar = Button(self.ui, text="Barplot")
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
