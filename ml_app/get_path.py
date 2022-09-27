from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import tables
import pandas as pd
from tables import Nodd
import ops
import common_panel


class BrowseFile(Nodd):
    def __init__(self, ui):
        self.ui = ui
        self.ui.geometry('300x300')
        self.cv = Canvas(width=300, height=300)
        self.cv.pack(fill='both', expand=True)
        self.df = None
        self.tables = None

    def file_path(self):
        _filename = filedialog.askopenfilename()
        _filename = r'{}'.format(_filename)
        self.df = pd.read_csv(_filename)
        root = Tk()
        self.tables = tables.DataVis(root, self.df, self.ui, self.cv).pack(fill='both', expand=True)
        root.mainloop()

    def port(self):
        click = Button(master=self.ui, text='Open File', command=lambda: [self.ui.destroy(), self.file_path()])
        self.cv.create_window(150, 150, window=click)
        self.ui.mainloop()


def main():
    f = BrowseFile(Tk())
    f.port()


if __name__ == '__main__':
    main()
