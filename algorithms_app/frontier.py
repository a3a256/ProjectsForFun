from tkinter import *
import lst

class ListVis:
    def __init__(self, ui, first):
        self.ui = ui
        self.ui.geometry('1000x400')
        self.cv = Canvas(width=1000, heigh=400)
        self.cv.pack(fill='both', expand=True)
        self.sll = lst.SLL(self.cv, first, 50, 70)
        self.intake = StringVar()

    def adding_start(self, num):
        self.sll.add_start(int(num), 50, 70)
        self.intake.set('')

    def adding_end(self, num):
        self.sll.add_end(int(num), 50, 70)
        self.intake.set('')

    def asc_sorting(self):
        self.sll.sort(50, 70, asc=True)

    def desc_sorting(self):
        self.sll.sort(50, 70, asc=False)
    

    def show(self):
        ent = Entry(master=self.ui, text=self.intake)
        self.cv.create_window(900, 50, window=ent)
        btn_start = Button(master=self.ui, text='Add at start', command=lambda: self.adding_start(ent.get()))
        self.cv.create_window(900, 80, window=btn_start)
        btn_end = Button(master=self.ui, text='Add at end', command=lambda: self.adding_end(ent.get()))
        self.cv.create_window(900, 110, window=btn_end)
        btn_sort = Button(master=self.ui, text='Sort:ASC', command=lambda: self.asc_sorting())
        self.cv.create_window(900, 140, window=btn_sort)
        btn_sort_desc = Button(master=self.ui, text='Sort:DESC', command=lambda: self.desc_sorting())
        self.cv.create_window(900, 170, window=btn_sort_desc)
        
