from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd

class DataVis(Frame):
    def __init__(self, parent, path):
        Frame.__init__(self, parent)
        text = Text(self, wrap="none")
        vsb = Scrollbar(self, orient="horizontal", command=text.xview)
        vsb1 = Scrollbar(self, orient='vertical', command=text.yview)
        text.configure(xscrollcommand=vsb.set)
        text.configure(yscrollcommand=vsb1.set)
        vsb.pack(side=BOTTOM, fill="x")
        vsb1.pack(side='right', fill="y")
        text.pack(fill="both", expand=True)
        cols = path.columns
        col_lengths = []
        cls = []
        for i in cols:
            ls = [len(str(x)) for x in path.loc[:, i]]
            col_lengths.append(max(ls))
            cls.append(len(str(i)))
        j = 0
        for col in cols:
            b = Button(self, text=col)
            b.configure(command=lambda x=b: self.hos(x))
            text.window_create("end", window=b)
            text.insert("end", " "*(col_lengths[j]))
            j += 1

        text.insert("end", "\n")

        for i in range(20):
            v = 0
            for j in range(len(cols)):
                lb = Label(self, text=path.iloc[i, j])
                text.window_create("end", window=lb)
                text.insert("end", " "*(cls[v]))
                v += 1
            text.insert("end", "\n")

        text.configure(state="disabled")

    def hos(self, val):
        print(val.cget('text'))

if __name__ == "__main__":
    root = Tk()
    t = DataVis(root, pd.read_csv(r'C:\Users\Azamat.Ilyasov\Downloads\breast-cancer.csv')).pack(fill='both', expand=True)
    root.mainloop()
