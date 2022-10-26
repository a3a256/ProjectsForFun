from tkinter import *

class MLOptions:
    def __init__(self, ui, path, selection, dataframe):
        self.ui = ui
        self.path = path
        self.selection = selection
        self.target = None
        self.df = dataframe
        self.x = None
        self.y = None

    def give_target(self, target):
        self.target = target.cget("text")
        self.selection.remove(self.target)

    def get_x_y(self, x_axis, y_axis):
        self.x = self.df.loc[:, x_axis]
        self.y = self.df.loc[:, y_axis]

    def target_select(self, option):
        lb = Label(master=self.ui, text="Choose the target feature!")
        lb.grid(row=0, column=0)
        for i in range(len(self.selection)):
            b = Button(master=self.ui, text=self.selection[i])
            b.grid(row=1, column=i)
            b.configure(command=lambda x=b: [self.give_target(x), self.get_x_y(self.selection, self.target)])

    def supervised(self):
        btn_classification = Button(master=self.ui, text="Classification")
        btn_classification.grid(row=0, column=0)
        btn_regression = Button(master=self.ui, text="Regression", command=lambda: [btn_classification.destroy(), btn_regression.destroy(), self.target_select(self.selection)])
        btn_regression.grid(row=1, column=0)

    def port(self):
        btn_supervised = Button(master=self.ui, text="Supervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy(), self.supervised()])
        btn_supervised.grid(row=0, column=0)
        btn_unsupervised = Button(master=self.ui, text="Unsupervised", command=lambda: [btn_supervised.destroy(), btn_unsupervised.destroy()])
        btn_unsupervised.grid(row=1, column=0)
        self.ui.mainloop()
