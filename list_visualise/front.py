from tkinter import *
import interface

class major:
    def __init__(self, ui):
        self.ui = ui
        self.save = 0

    def saving(self, num):
        self.save = int(num)

    def start(self):
        lb = Label(master=self.ui, text="Enter the first node:")
        lb.grid(row=0, column=0)
        ent = Entry(master=self.ui, text='')
        ent.grid(row=1, columnspan=2)
        btn = Button(master=self.ui, text="Start!", command=lambda: [self.saving(ent.get()), self.ui.destroy()])
        btn.grid(row=2, column=0)
        self.ui.mainloop()
        ui = interface.LinkedListPortray(Tk(), self.save)
        ui.to_do()


def main():
    m = major(Tk())
    m.start()

if __name__ == '__main__':
    main()
