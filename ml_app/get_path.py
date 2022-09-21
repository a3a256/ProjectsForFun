from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import tables

class BrowseFile:
    def __init__(self, ui):
        self.ui = ui
        self.ui.geometry('800x600')
        self.cv = Canvas(width=800, height=600)
        self.cv.pack(fill='both', expand=True)

    def file_path(self):
        _filename = filedialog.askopenfilename()
        _filename = r'{}'.format(_filename)
        root = Tk()
        t = tables.DataVis(root, _filename).pack(fill='both', expand=True)
        root.mainloop()


    def port(self):
        click = Button(master=self.ui, text='Open File', command=lambda: self.file_path())
        self.cv.create_window(40, 10, window=click)
        self.ui.mainloop()


def main():
    f = BrowseFile(Tk())
    f.port()


if __name__ == '__main__':
    main()
