from tkinter import *
import to_portray_bst

class UI:
    def __init__(self, ui):
        self.ui = ui
        self.first = 0

    def save_it(self, val):
        self.first += int(val)

    def go(self):
        lb = Label(master=self.ui, text="Enter the root")
        lb.grid(row=0, column=0)
        ent = Entry(master=self.ui, text='')
        ent.grid(row=1, column=0)
        btn = Button(master=self.ui, text='Start with this node', command=lambda: [self.save_it(ent.get()), self.ui.destroy()])
        btn.grid(row=2, column=0)
        self.ui.mainloop()
        showing = to_portray_bst.Activated(Tk(), self.first)
        showing.show()



def main():
    wn = Tk()
    ui = UI(wn)
    ui.go()


if __name__ == '__main__':
    main()
    
