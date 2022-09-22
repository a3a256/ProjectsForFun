from tkinter import *
import backend
import time


class Calculations:
    def __init__(self, ui):
        self.ui = ui
        self.intake = "f()="
        self.equation = StringVar()
        self.equation.set(self.intake)
        self.arg = ""

    def num_press(self, val):
        self.intake = self.equation.get()
        if val == "x":
            if self.intake[2] == ")":
                win = Tk()
                lb = Label(master=win, text="Error! Enter argument into f() function, inout is cleared!")
                lb.pack()
                self.intake = "f()="
                self.equation.set(self.intake)
                return
            else:
                if self.intake[2] != "e":
                    self.arg = self.intake[2]
                else:
                    win = Tk()
                    lb = Label(master=win, text="Unfortunately this character is an exponent, enter another character as an argument")
                    lb.pack()
                    self.intake = "f()="
                    self.equation.set(self.intake)
        self.intake += val
        self.equation.set(self.intake)

    def op_press(self, val):
        self.intake = self.equation.get()
        self.intake += val
        self.equation.set(self.intake)

    def equal(self):
        bb = backend.Distribute(self.equation.get(), self.arg)
        self.equation.set(bb.derive_full())

    def exp(self):
        self.intake += "^()"
        self.equation.set(self.intake)

    def activate(self):
        en1 = Entry(master=self.ui, text=self.equation)
        en1.grid(row=0, columnspan=4)
        btn1 = Button(master=self.ui, text="1", command=lambda: self.num_press("1"))
        btn1.grid(row=1, column=0)
        btn2 = Button(master=self.ui, text="2", command=lambda: self.num_press("2"))
        btn2.grid(row=1, column=1)
        btn3 = Button(master=self.ui, text="3", command=lambda: self.num_press("3"))
        btn3.grid(row=1, column=2)
        btn4 = Button(master=self.ui, text="4", command=lambda: self.num_press("4"))
        btn4.grid(row=2, column=0)
        btn5 = Button(master=self.ui, text="5", command=lambda: self.num_press("5"))
        btn5.grid(row=2, column=1)
        btn6 = Button(master=self.ui, text="6", command=lambda: self.num_press("6"))
        btn6.grid(row=2, column=2)
        btn7 = Button(master=self.ui, text="7", command=lambda: self.num_press("7"))
        btn7.grid(row=3, column=0)
        btn8 = Button(master=self.ui, text="8", command=lambda: self.num_press("8"))
        btn8.grid(row=3, column=1)
        btn9 = Button(master=self.ui, text="9", command=lambda: self.num_press("9"))
        btn9.grid(row=3, column=2)
        btn_plus = Button(master=self.ui, text="+", command=lambda: self.op_press("+"))
        btn_plus.grid(row=1, column=3)
        btn_plus = Button(master=self.ui, text="-", command=lambda: self.op_press("-"))
        btn_plus.grid(row=2, column=3)
        btn_mul = Button(master=self.ui, text="*", command=lambda: self.op_press("*"))
        btn_mul.grid(row=3, column=3)
        btn_dot = Button(master=self.ui, text='x', command=lambda: self.num_press("x"))
        btn_dot.grid(row=4, column=1)
        btn0 = Button(master=self.ui, text="0", command=lambda: self.num_press("0"))
        btn0.grid(row=4, column=0)
        btn_equal = Button(master=self.ui, text="=", command=lambda: self.equal())
        btn_equal.grid(row=4, column=2)
        btn_pow = Button(master=self.ui, text="^", command=lambda: self.exp())
        btn_pow.grid(row=4, column=3)
        self.ui.mainloop()


def main():
    c = Calculations(Tk())
    c.activate()


if __name__ == '__main__':
    main()
