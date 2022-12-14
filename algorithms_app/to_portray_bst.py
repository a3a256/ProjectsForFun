from tkinter import *
import bst_fun

class Activated:
    def __init__(self, ui, first):
        self.gui = ui
        self.gui.geometry('1000x1000')
        self.cv = Canvas(width=1000, height=1000)
        self.cv.pack(fill='both', expand=True)
        self.tree = bst_fun.Binary(first, self.cv, 400, 25)
        self.intake = StringVar()
        self.intake.set('')
        self.traverse = StringVar()


    def adding(self, num):
        n = int(num)
        self.tree.add(n, 400, 25, 400, 40)
        self.intake.set('')


    def in_order(self):
        self.tree.iot(self.tree)
        outage = self.tree.show()
        label = Label(master=self.gui, text=f'InOrderTraversal: {outage}', font=('Helvetica', 16))
        self.cv.create_window(400, 600, window=label)


    def pre_order(self):
        self.tree.pot(self.tree)
        outage = self.tree.show()
        label = Label(master=self.gui, text=f'PreOrderTraversal: {outage}', font=('Helvetica', 16))
        self.cv.create_window(400, 630, window=label)


    def post_order(self):
        self.tree.post(self.tree)
        outage = self.tree.show()
        label = Label(master=self.gui, text=f'PostOrderTraversal: {outage}', font=('Helvetica', 16))
        self.cv.create_window(400, 660, window=label)

    def breadth_first_traversal(self):
        self.tree.bfs(self.tree)
        outage = self.tree.show()
        label = Label(master=self.gui, text=f'BreadthFirstTraversal: {outage}', font=('Helvetica', 16))
        self.cv.create_window(400, 660, window=label)


    def get_height(self):
        outage = 'The height is:'
        outage += str(self.tree.height(self.tree)+1)
        lb = Label(master=self.gui, text=outage)
        self.cv.create_window(900, 330, window=lb)
        


    def show(self):
        ent = Entry(master=self.gui, text=self.intake)
        ent_window = self.cv.create_window(900,50, window=ent)
        btn = Button(master=self.gui, text="Add number", command=lambda: self.adding(ent.get()))
        btn_window = self.cv.create_window(900,80, window=btn)
        tr_lb = Label(master=self.gui, text="Traverse!")
        tr_lb_window = self.cv.create_window(900, 150, window=tr_lb)
        iot_btn = Button(master=self.gui, text="InOrderTraversal", command=lambda: self.in_order())
        iot_btn_window = self.cv.create_window(900, 180, window=iot_btn)
        pre_btn = Button(master=self.gui, text="PreOrderTraversal", command=lambda: self.pre_order())
        pre_btn_window = self.cv.create_window(900, 210, window=pre_btn)
        post_btn = Button(master=self.gui, text="PostOrderTraversal", command=lambda: self.post_order())
        post_btn_window = self.cv.create_window(900, 240, window=post_btn)
        bfs_btn = Button(master=self.gui, text="BreadthFirstTraversal", command=lambda: self.breadth_first_traversal())
        bfs_window = self.cv.create_window(900, 300, window=bfs_btn)
        height_btn = Button(master=self.gui, text='Click to know the height', command=lambda: self.get_height())
        height_window = self.cv.create_window(900, 360, window=height_btn)
        self.gui.mainloop()



if __name__ == '__main__':
    u = Activated(Tk(), 10)
    u.show()
        
