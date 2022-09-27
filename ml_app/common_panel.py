from tkinter import *
import pandas as pd

class Nodes:
    var = []

    def update(val):
        Nodes.var.append(val)

class PreprocessingOption:
    def __init__(self, ui, df, feats):
        self.ui = ui
        self.df = df
        self.cols = feats

    def info(self):
        root = Tk()
        tables = Description(root, self.df.describe()).pack(fill='both', expand=True)
        root.mainloop()

    def preprocess(self):
        btn_info = Button(master=self.ui, text="Common info on the dataset", command=lambda: self.info())
        btn_info.grid(row=0, column=0)
        btn_encode = Button(master=self.ui, text="Encode chosen columns")
        btn_encode.grid(row=1, column=0)
        self.ui.mainloop()


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
                lb = Label(master=self, text=df.iloc[i, j])
                text.window_create("end", window=lb)
                text.insert("end", "  ")
            text.insert("end", "\n")