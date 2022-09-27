from tkinter import *
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
import pandas as pd
import get_path

class ShowPlots:
    def __init__(self, x_axis=None, y_axis=None, legend=None):
        self.x = x_axis
        self.y = y_axis
        self.legend = legend

    def scatterplot(self):
        plt.scatter(self.x, self.y)
        plt.show()