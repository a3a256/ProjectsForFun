from tkinter import *
from tkinter import ttk, filedialog
from xml.etree.ElementPath import ops
import pandas as pd
import list_of_cols
import common_panel
import ops
import ml_algorithms

class Nodd:
    data = ""
    arr = []

    def update(val):
        Nodd.arr = val

    def get():
        return Nodd.arr

class DataVis(Frame):
    def __init__(self, parent, path, ui, pathway):
        Frame.__init__(self, parent)
        self.lst = list_of_cols.LinkedList(None)
        text = Text(self, wrap="none")
        vsb = Scrollbar(self, orient="horizontal", command=text.xview)
        vsb1 = Scrollbar(self, orient='vertical', command=text.yview)
        text.configure(xscrollcommand=vsb.set)
        text.configure(yscrollcommand=vsb1.set)
        vsb.pack(side=BOTTOM, fill="x")
        vsb1.pack(side='right', fill="y")
        text.pack(fill="both", expand=True)
        self.df = path
        cols = path.columns
        col_names_lengths = [len(x) for x in self.df.columns]
        col_vals_lengths = []
        for i in range(self.df.shape[1]):
            a = []
            for j in range(self.df.shape[0]):
                a.append(len(str(self.df.iloc[j, i])))
            col_vals_lengths.append(max(a))
        col_gaps = []
        for i, j in zip(col_names_lengths, col_vals_lengths):
            if i > j:
                col_gaps.append(i)
            else:
                col_gaps.append(j)
        self.selection = StringVar()
        self.col_op = []
        col_lengths = []
        self.ui = ui
        self.vals = dict()
        cls = []
        self.way = pathway
        for i in cols:
            ls = [len(str(x)) for x in path.loc[:, i]]
            col_lengths.append(max(ls))
            cls.append(len(str(i)))
        j = 0
        btn_preprocess = Button(self, text="Preprocessing", command=lambda: self.prepare_data())
        text.window_create("end", window=btn_preprocess)
        text.insert("end", "")
        btn_visualise = Button(master=self, text="Visualise the data", command=lambda: self.show_data())
        text.window_create("end", window=btn_visualise)
        text.insert("end", "")
        btn_model = Button(master=self, text="Teach model", command=lambda: self.model_data())
        text.window_create("end", window=btn_model)
        text.insert("end", " ")
        ent_cols = Entry(self, text=self.selection, width=60)
        text.window_create("end", window=ent_cols)
        text.insert("end", "\n")
        self.text_window = []
        for col in cols:
            b = Button(self, text=col)
            var = str(col)
            gap = col_gaps[j] - len(var) - 2
            b.configure(command=lambda x=b: self.hos(x))
            text.insert("end", " "*(gap))
            self.text_window.append(text.window_create("end", window=b))
            # text.insert("end", "")
            j += 1

        text.insert("end", "\n")

        for i in range(20):
            for j in range(len(cols)):
                lb = Label(self, text=path.iloc[i, j])
                var = str(path.iloc[i, j])
                gap = abs(col_gaps[j] - len(var))-1
                text.insert("end", " "*gap)
                text.window_create("end", window=lb)
                # text.insert("end", "")
            text.insert("end", "\n")

        text.configure(state="disabled")


    def hos(self, val):
        self.lst.add(val.cget('text'))
        self.col_op.append(val.cget('text'))
        Nodd.update(self.col_op)
        self.selection.set(self.lst.show())

    def preprocessing_result(self, val):
        if val == []:
            pass
        elif val[1] == "removal":
            root = Tk()
            t = DataVis(root, val[0], self.ui, self.way).pack(fill='both', expand=True)
            root.mainloop()
        elif val[1] == "encoding":
            root = Tk()
            t = DataVis(root, val[0], self.ui, self.way).pack(fill="both", expand=True)
            root.mainloop()

    def model_data(self):
        ml = ml_algorithms.MLOptions(Tk(), self.way, Nodd.get(), self.df)
        Nodd.arr = []
        self.col_op = []
        self.lst = list_of_cols.LinkedList(None)
        self.selection.set("")
        ml.port()

    def prepare_data(self):
        val = common_panel.PreprocessingOption(Tk(), self.df, Nodd.get())
        self.preprocessing_result(val.preprocess())

    def show_data(self):
        val = ops.PlotPanel(Tk(), Nodd.get(), self.df)
        Nodd.arr = []
        self.col_op = []
        print(Nodd.get())
        self.lst = list_of_cols.LinkedList(None)
        self.selection.set("")
        val.plot_options()
