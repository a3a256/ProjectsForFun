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
        self.val = ""

    def pair_plot(self):
        if not self.selection:
            sns.pairplot(data=self.df, vars=self.selection)
        else:
            sns.pairplot(data=self.df)
        plt.show()

    def scatter_plot(self):
        plot = ShowPlots(self.df, self.selection)
        plot.process()

    def get(self, val):
        self.val = val
        return

    def bar_plot(self):
        if len(self.selection) > 2:
            # win = Tk()
            # lb = Label(master=win, text="Enter dimensions:")
            # lb.grid(row=0, column=0)
            # ent = Entry(master=win, text="")
            # ent.grid(row=1, column=0)
            # btn = Button(master=win, text="Draw", command=[win.destroy(), self.get(ent.get())])
            # btn.grid(row=2, column=0)
            # win.mainloop()
            # width, height = self.val.split("x")
            min_ = 0
            width, height = len(self.selection), 1
            for i in range(len(self.selection)):
                if len(np.unique(self.selection[i])) < len(np.unique(self.selection[i])):
                    min_ = i
            min_bound = self.selection[min_]
            self.selection.pop(min_)
            fig, axes = plt.subplots(ncols=int(width)-1, nrows=int(height), figsize=(10, 8))
            for j in range(int(width)-1):
                axes[j].bar(self.df[min_bound], self.df[self.selection[j]])
            plt.show()
        elif len(self.selection) == 2:
            col1 = np.unique(self.df[self.selection[0]])
            col2 = np.unique(self.df[self.selection[1]])
            if len(col1) > len(col2):
                plt.bar(self.df[self.selection[1]], self.df[self.selection[0]])
            else:
                plt.bar(self.df[self.selection[0]], self.df[self.selection[1]])
        plt.show()

    def pie_plot(self):
        if len(self.selection) > 1:
            length = len(self.selection)
            ids = []
            for i in range(length):
                if np.unique(self.selection[i]) < 10:
                    ids.append(i)
            if len(ids) > 1:
                fig, axes = plt.subplots(nrows=len(ids), ncols=1, figsize=(10, 8))
                for j in range(len(ids)):
                    print(ids)
        plt.pie(self.df[self.selection].value_counts())
        plt.show()
    
    def plot_options(self):
        btn_scatter = Button(self.ui, text="Scatterplot of selected columns", command=lambda: [self.ui.destroy() ,self.scatter_plot()])
        btn_scatter.grid(row=0, column=0)
        btn_bar = Button(self.ui, text="Barplot", command=lambda: [self.bar_plot()])
        btn_bar.grid(row=1, column=0)
        btn_pairplot = Button(self.ui, text="Show pairplot", command=lambda: [self.ui.destroy(), self.pair_plot()])
        btn_pairplot.grid(row=2, column=0)
        btn_pie = Button(self.ui, text="Show pie chart", command=lambda: [self.ui.destroy(), self.pie_plot()])
        btn_pie.grid(row=3, column=0)
        self.ui.mainloop()

class ShowPlots:
    def __init__(self, df, axes):
        self.axes = axes
        self.df = df

    def process(self):
        hue = len(np.unique(self.df[self.axes[0]]))
        lowest_id = 0
        if len(self.axes) > 2:
            for i, j in enumerate(self.df[self.axes[1:]]):
                if len(np.unique(self.df[j])) < hue:
                    lowest_id = i
                    hue = len(np.unique(self.df[j]))
            axes = []
            legend = lowest_id
            for i in range(len(self.axes)):
                if i != legend:
                    axes.append(i)
            cols = [self.axes[axes[0]], self.axes[axes[1]]]
            vals = self.df.loc[:, cols].values
            self.scatterplot_legend(vals, self.df[self.axes[legend]], cols)
        else:
            self.scatterplot(self.df[self.axes[0]], self.df[self.axes[1]])

    def scatterplot_legend(self, axes, hue, col_names):
        for i in np.unique(hue):
            plt.scatter(axes[hue==i, 0], axes[hue==i, 1])
        plt.xlabel(col_names[0])
        plt.ylabel(col_names[1])
        plt.legend(np.unique(hue))
        plt.show()

    def scatterplot(self, x, y):
        plt.scatter(x, y)
        plt.show()
