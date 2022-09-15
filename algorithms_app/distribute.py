from tkinter import *
import start

def activate():
    wn = Tk()
    btn_sll = Button(master=wn, text='SinglyLInked List', command=lambda: [wn.destroy(), start.main('sll')])
    btn_sll.pack()
    btn_bst = Button(master=wn, text='BinarySearchTree', command=lambda: [wn.destroy(), start.main('bst')])
    btn_bst.pack()
    wn.mainloop()



if __name__ == '__main__':
    activate()
