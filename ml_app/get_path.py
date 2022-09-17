from tkinter import *


class BrowseFile:
    def __init__(self, ui):
        self.ui = ui

    def file_path(self):
        _filename = filedialog.askopenfilename()