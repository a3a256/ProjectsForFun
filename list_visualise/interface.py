from tkinter import *
import sll_fun

class LinkedListPortray:
    def __init__(self, gui, first):
        self.ui = gui
        self.sll = sll_fun.sll(first)
        self.lst = StringVar()
        self.lst.set(str(first))
        self.enter = StringVar()
        self.out = StringVar()
        self.out.set(self.sll.show())

    def beginning(self, num):
        self.sll.add_start(num)
        outage = self.sll.show()
        self.out.set(outage)
        self.enter.set("")

    def ending(self, num):
        self.sll.add_end(num)
        outage = self.sll.show()
        self.out.set(outage)
        self.enter.set("")

    def insert_exe(self, index, num):
        self.sll.insert_at(index, num)
        outage = self.sll.show()
        self.out.set(outage)
        self.enter.set("")

    def inserting(self, num):
        win = Tk()
        lb = Label(master=win, text="Index")
        lb.grid(row=0, column=0)
        ent = Entry(master=win, text="")
        ent.grid(row=0, column=1)
        btn = Button(master=win, text="Enter!", command=lambda:[self.insert_exe(int(ent.get()), num), win.destroy()])
        btn.grid(row=0, column=2)
        win.mainloop()

    def replace_exe(self, index, num):
        self.sll.replace_at(index, num)
        outage = self.sll.show()
        self.out.set(outage)
        self.enter.set("")

    def replacing(self, num):
        win = Tk()
        lb = Label(master=win, text="Index")
        lb.grid(row=0, column=0)
        ent = Entry(master=win, text="")
        ent.grid(row=0, column=1)
        btn = Button(master=win, text="Enter!", command=lambda:[self.replace_exe(int(ent.get()), num), win.destroy()])
        btn.grid(row=0, column=2)
        win.mainloop()

    def sorting(self, asc=True):
        if asc:
            self.sll.sort()
        else:
            self.sll.sort(asc=False)
        outage = self.sll.show()
        self.out.set(outage)

    def reversing(self):
        self.sll.reverse()
        outage = self.sll.show()
        self.out.set(outage)

    def to_do(self):
        ent = Entry(master=self.ui, text=self.enter)
        ent.grid(row=0, columnspan=4)
        btn_start = Button(master=self.ui, text="Add at the start", command=lambda: self.beginning(int(ent.get())))
        btn_start.grid(row=1, column=0)
        btn_end = Button(master=self.ui, text="Add at the end", command=lambda: self.ending(int(ent.get())))
        btn_end.grid(row=1, column=1)
        btn_replace = Button(master=self.ui, text="Replace at", command=lambda: self.replacing(int(ent.get())))
        btn_replace.grid(row=1, column=2)
        btn_insert = Button(master=self.ui, text="Insert at", command=lambda: self.replacing(int(ent.get())))
        btn_insert.grid(row=1, column=3)
        outer = Entry(master=self.ui, text=self.out, width=100)
        outer.grid(row=2, columnspan=4)
        btn_asc = Button(master=self.ui, text="Sort: asc", command=lambda: self.sorting())
        btn_asc.grid(row=3, column=0)
        btn_dsc = Button(master=self.ui, text="Sort: desc", command=lambda: self.sorting(asc=False))
        btn_dsc.grid(row=3, column=1)
        btn_reverse = Button(master=self.ui, text="Reverse", command=lambda: self.reversing())
        btn_reverse.grid(row=3, column=2)
        self.ui.mainloop()
