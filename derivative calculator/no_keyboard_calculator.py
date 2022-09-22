from tkinter import *
import backend


class NoKeyboard:
    def __init__(self, ui):
        self.ui = ui
        self.intake = "f()="
        self.equation = StringVar()
        self.equation.set(self.intake)
        self.arg = ""

    def to_power(self):
        self.intake = self.equation.get()
        self.intake += "^()"
        self.equation.set(self.intake)

    def clear(self):
        self.equation.set("f()=")

    def get_target(self):
        ar = ""
        ex = list(self.equation.get())
        while " " in ex:
            ex.remove(" ")
        if ex[2] == ")":
            Label(master=Tk(), text="Please, enter argument for the function f()!").pack()
        else:
            self.arg += ex[2]

    def equal_press(self):
        self.get_target()
        bb = backend.Distribute(self.equation.get(), self.arg)
        self.equation.set("f`({})=".format(self.arg) + bb.derive_full())

    def activate(self):
        ent = Entry(master=self.ui, text=self.equation, width=50)
        ent.grid(row=0, columnspan=3)
        btn_plus = Button(master=self.ui, text="^", command=lambda: self.to_power())
        btn_plus.grid(row=1, column=0)
        btn_clear = Button(master=self.ui, text="C", command=lambda: self.clear())
        btn_clear.grid(row=1, column=1)
        btn_equal = Button(master=self.ui, text="=", command=lambda: self.equal_press())
        btn_equal.grid(row=1, column=2)
        self.ui.mainloop()


def main():
    win = Tk()
    n = NoKeyboard(win).activate()


if __name__ == '__main__':
    main()