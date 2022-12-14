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

    def go_insert(self, val, id):
        self.sll.insert_at(val, int(id))
        print(self.sll.show())

    def deleting_at(self):
        lb = Label(master=self.ui, text="Enter the index to delete at:")
        self.cv.create_window(900, 200, window=lb)
        ent0 = Entry(master=self.ui, text="")
        self.cv.create_window(900, 230, window=ent0)
        btn = Button(master=self.ui, text="Delete!", command=lambda: [self.go_delete(ent0.get()), btn.destroy(), lb.destroy(), ent0.destroy()])
        self.cv.create_window(900, 260, window=btn)
        self.intake.set("")

    def go_delete(self, id):
        self.sll.deleted_value(id)
        print(self.sll.show())

    def inserting_at(self, val):
        lb = Label(master=self.ui, text="Enter the index to insert at:")
        self.cv.create_window(900, 200, window=lb)
        ent0 = Entry(master=self.ui, text="")
        self.cv.create_window(900, 230, window=ent0)
        btn = Button(master=self.ui, text="Insert!", command=lambda: [self.go_insert(val, ent0.get()), btn.destroy(), lb.destroy(), ent0.destroy()])
        self.cv.create_window(900, 260, window=btn)
        self.intake.set("")

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
        btn_insert = Button(master=self.ui, text="Insert at:", command=lambda: self.inserting_at(ent.get()))
        self.cv.create_window(900, 140, window=btn_insert)
        btn_delete = Button(master=self.ui, text="Delete at:", command=lambda: self.deleting_at())
        self.cv.create_window(900, 170, window=btn_delete)
        btn_sort = Button(master=self.ui, text='Sort:ASC', command=lambda: self.asc_sorting())
        self.cv.create_window(900, 290, window=btn_sort)
        btn_sort_desc = Button(master=self.ui, text='Sort:DESC', command=lambda: self.desc_sorting())
        self.cv.create_window(900, 320, window=btn_sort_desc)
        
