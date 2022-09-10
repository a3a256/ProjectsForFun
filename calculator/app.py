from tkinter import *
import orient

class Calculator:
    def __init__(self, gui):
        self.ui = gui
        self.nums = []
        self.hold = ""
        self.expression = ""
        self.equation = StringVar()
        self.operation = ["+", "-", "*", "/"]
        self.ops = []
        self.equal = "="

    def num_press(self, num):
        self.expression = self.expression + str(num)
        self.hold = self.hold + str(num)
        self.equation.set(self.expression)

    def op_press(self, operator):
        self.expression = self.expression + str(operator)
        self.equation.set(self.expression)
        self.nums.append(int(self.hold))
        self.ops.append(operator)
        self.hold = ""

    def clear(self):
        self.expression = ""
        self.equation.set(self.expression)
    
    def equal_press(self):
        self.nums.append(int(self.hold))
        m = orient.Implement(self.nums, self.ops)
        calc = m.distribute()
        self.expression = str(calc)
        self.equation.set(self.expression)
        self.hold = str(calc)
        self.nums = []
        self.ops = []

    def board(self):
        ent = Entry(master=self.ui, text=self.equation)
        ent.grid(row=0, columnspan=4)
        btn_1 = Button(master=self.ui, text="1", command=lambda:self.num_press(1))
        btn_1.grid(row=1, column=0)
        btn_2 = Button(master=self.ui, text="2", command=lambda:self.num_press(2))
        btn_2.grid(row=1, column=1)
        btn_3 = Button(master=self.ui, text="3", command=lambda:self.num_press(3))
        btn_3.grid(row=1, column=2)
        btn_clear = Button(master=self.ui, text="C", command=lambda:self.clear())
        btn_clear.grid(row=1, column=3)
        btn_4 = Button(master=self.ui, text="4", command=lambda:self.num_press(4))
        btn_4.grid(row=2, column=0)
        btn_5 = Button(master=self.ui, text="5", command=lambda:self.num_press(5))
        btn_5.grid(row=2, column=1)
        btn_6 = Button(master=self.ui, text="6", command=lambda:self.num_press(6))
        btn_6.grid(row=2, column=2)
        btn_mul = Button(master=self.ui, text="*", command=lambda:self.op_press("*"))
        btn_mul.grid(row=2, column=3)
        btn_7 = Button(master=self.ui, text="7", command=lambda:self.num_press(7))
        btn_7.grid(row=3, column=0)
        btn_8 = Button(master=self.ui, text="8", command=lambda:self.num_press(8))
        btn_8.grid(row=3, column=1)
        btn_9 = Button(master=self.ui, text="9", command=lambda:self.num_press(9))
        btn_9.grid(row=3, column=2)
        btn_div = Button(master=self.ui, text="/", command=lambda:self.op_press("/"))
        btn_div.grid(row=3, column=3)
        btn_plus = Button(master=self.ui, text="+", command=lambda:self.op_press("+"))
        btn_plus.grid(row=4, column=0)
        btn_0 = Button(master=self.ui, text="0", command=lambda:self.num_press(0))
        btn_0.grid(row=4, column=1)
        btn_minus = Button(master=self.ui, text="-", command=lambda:self.op_press("-"))
        btn_minus.grid(row=4, column=2)
        btn_eq = Button(master=self.ui, text="=", command=lambda:self.equal_press())
        btn_eq.grid(row=4, column=3)
        self.ui.mainloop()


if __name__ == '__main__':
    cl = Calculator(Tk())
    cl.board()