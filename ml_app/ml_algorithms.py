from tkinter import *

class MLOptions:
    def __init__(self, ui, path, selection):
        self.ui = ui
        self.path = path
        self.selection = selection
        self.target = None

    def give_target(self, target):
        self.target = target

    def target_select(self, option):
        for i in range(len(self.selection)):
            b = Button(master=self.ui, text=self.selection[i])
            b.grid(row=0, column=i)

    def supervised(self):
        btn_classification = Button(master=self.ui, text="Classification")
        btn_classification.grid(row=0, column=0)
        btn_regression = Button(master=self.ui, text="Regression", command=lambda: [btn_classification.destroy(), btn_regression.destroy()])
        btn_regression.grid(row=1, column=0)

    def port(self):
        btn_supervised = Button(master=self.ui, text="Supervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy(), self.supervised()])
        btn_supervised.grid(row=0, column=0)
        btn_unsupervised = Button(master=self.ui, text="Unsupervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy()])
        btn_unsupervised.grid(row=1, column=0)
        self.ui.mainloop()
