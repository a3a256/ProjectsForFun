from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd

class DataVis(Frame):
    def __init__(self, path, ui):
        Frame.__init__(self, ui)
        self.text = Text(self, wrap='none')
        self.h = Scrollbar(orient='horizontal', command=self.text.xview)
        self.text.configure(xscrollcommand=self.h.set)
        self.h.pack(side=BOTTOM, fill='x')
        self.text.pack(fill='both', expand=True)
        self.df = pd.read_csv(path)
        self.cols = dict()

    def listen(self, val):
        print(val)
        
    def draw(self):
        cols = self.df.columns
        for col in cols:
            self.cols[col] = Button(self, text=col, command=self.listen(col))
            self.text.window_create(self.cols[col])
            self.text.insert('end', '')
        self.text.configure(state='disabled')
        self.mainloop()

class Example(Frame):
    def __init__(self, parent, path):
        Frame.__init__(self, parent)
        text = Text(self, wrap="none")
        vsb = Scrollbar(self, orient="horizontal", command=text.xview)
        text.configure(xscrollcommand=vsb.set)
        vsb.pack(side=BOTTOM, fill="x")
        text.pack(fill="both", expand=True)
        df = pd.read_csv(path)
        cols = df.columns
        col_lengths = []
        for i in cols:
            ls = [len(str(x)) for x in df.loc[:, i]]
            col_lengths.append(max(ls))
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
                lb = Label(self, text=df.iloc[i, j])
                text.window_create("end", window=lb)
                text.insert("end", " "*col_lengths[v])
                v += 0
            text.insert("end", "\n")

        text.configure(state="disabled")

    def hos(self, val):
        print(val.cget('text'))

if __name__ == "__main__":
    root = Tk()
    t = Example(root, r'C:\Users\Azamat.Ilyasov\Downloads\breast-cancer.csv').pack(fill='both', expand=True)
    root.mainloop()