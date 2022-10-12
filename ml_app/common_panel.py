from tkinter import *
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Nodes:
    var = []

    def update(val):
        Nodes.var.append(val)

class PreprocessingOption:
    def __init__(self, ui, df, feats):
        self.ui = ui
        self.df = df
        self.cols = feats
        self.results = []

    def info(self):
        root = Tk()
        tables = Description(root, self.df.describe()).pack(fill='both', expand=True)
        root.mainloop()
        return 0

    def column_removal(self):
        self.df.drop(self.cols, axis=1, inplace=True)
        self.results = [self.df, "removal"]

    def column_encoding(self):
        # encoding to be added
        le = LabelEncoder()
        le.fit(self.df[self.cols])
        self.df[self.cols] = le.transform(self.df[self.cols])
        self.results = [self.df, "encoding"]

    def preprocess(self):
        btn_info = Button(master=self.ui, text="Common info on the dataset", command=lambda: self.info())
        btn_info.grid(row=0, column=0)
        btn_encode = Button(master=self.ui, text="Encode chosen columns", command=lambda: self.column_encoding())
        btn_encode.grid(row=1, column=0)
        btn_remove = Button(master=self.ui, text="Remove the column", command=lambda: [self.column_removal(), self.ui.destroy()])
        btn_remove.grid(row=2, column=0)
        self.ui.mainloop()
        return self.results


class Description(Frame):
    def __init__(self, parent, df):
        Frame.__init__(self, parent)
        text = Text(self, wrap="none")
        vsb = Scrollbar(self, orient="horizontal", command=text.xview)
        vsb1 = Scrollbar(self, orient='vertical', command=text.yview)
        text.configure(xscrollcommand=vsb.set)
        text.configure(yscrollcommand=vsb1.set)
        vsb.pack(side=BOTTOM, fill="x")
        vsb1.pack(side='right', fill="y")
        text.pack(fill="both", expand=True)
        gaps = []
        for i in df.index:
            gaps.append(len(i))
        gap = max(gaps)
        text.insert("end", " "*gap)
        for i in df.columns:
            lb = Label(master=self, text=str(i))
            text.window_create("end", window=lb)
            text.insert("end", "")
        text.insert("end", "\n")
        for i in range(len(df.index)):
            lb = Label(master=self, text=str(df.index[i]))
            text.window_create("end", window=lb)
            text.insert("end", "")
            for j in range(len(df.columns)):
                lb = Label(master=self, text=str(round(float(df.iloc[i, j]), 2)))
                text.window_create("end", window=lb)
                text.insert("end", "  ")
            text.insert("end", "\n")
