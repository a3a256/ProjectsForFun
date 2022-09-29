from tkinter import *

class Node:
    def __init__(self, val, _next):
        self.val = val
        self.next = _next


class SLL:
    def __init__(self, ui, first, x, y):
        self.ui = ui
        self.arrows = [self.ui.create_line(x+10, y, x+30, y, width=1.5, arrow=LAST)]
        self.nodes = [self.ui.create_text(x-25, y, text='head', font=('Helvetica', str(16)))]
        self.nodes.append(self.ui.create_text(x+40, y, text=str(first), font=('bold')))
        self.head = Node(first, None)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def add_start(self, num, x, y):
        itr = self.head
        self.head = Node(num, itr)
        for i, j in zip(self.nodes[1:], self.arrows):
            self.ui.move(i, 45, 0)
            self.ui.move(j, 45, 0)
        self.arrows.append(self.ui.create_line(x+10, y, x+30, y, width=1.5, arrow=LAST))
        self.nodes.append(self.ui.create_text(x+40, y, text=str(num), font=('bold')))

    def deleted_value(self, id):
        x = 50
        itr = self.head
        index = int(id) - 1
        count = 0
        while itr:
            if count == index:
                itr.next = itr.next.next
                break
            x += 45
            count += 1
            itr = itr.next
        self.ui.delete(self.nodes[index+2])
        self.nodes.pop(index+2)
        self.ui.delete(self.arrows[index+1])
        self.arrows.pop(index+1)
        for i, j in zip(self.nodes[index+2:], self.arrows[index+1:]):
            self.ui.move(i, -45, 0)
            self.ui.move(j, -45, 0)

    def add_end(self, num, x, y):
        itr = self.head
        x += 45
        while itr.next:
            itr = itr.next
            x += 45
        itr.next = Node(num, None)
        self.arrows.append(self.ui.create_line(x+10, y, x+30, y, width=1.5, arrow=LAST))
        self.nodes.append(self.ui.create_text(x+40, y, text=str(num), font=('bold')))

    def insert_label(self, val, id):
        x = 50
        y = 70
        itr = self.head
        for i in range(id-1):
            x += 45
            itr = itr.next
        for i, j in zip(self.nodes[id:], self.arrows[id-1:]):
            self.ui.move(i, 45, 0)
            self.ui.move(j, 45, 0)
        self.arrows.append(self.ui.create_line(x+10, y, x+30, y, width=1.5, arrow=LAST))
        self.nodes.append(self.ui.create_text(x+40, y, text=str(val), font=("bold")))

    def insert_at(self, val, id):
        if id >= self.get_length():
            raise Exception("Error! Index is out of bound")
        else:
            itr = self.head
            i = 0
            while i<id-1:
                itr = itr.next
                i += 1
            itr.next = Node(val, itr.next)
        self.insert_label(val, id)

    def sort(self, x, y, asc=False):
        clear = False
        while not clear:
            x1 = x
            i = 1
            clear = True
            itr = self.head
            while itr.next:
                if asc:
                    if int(str(itr.val)) > int(str(itr.next.val)):
                        clear = False
                        temp = itr.val
                        itr.val = itr.next.val
                        itr.next.val = temp
                        self.ui.delete(self.nodes[i])
                        self.ui.delete(self.nodes[i+1])
                        self.nodes[i] = self.ui.create_text(x1+40, y, text=str(itr.val), font=('bold'))
                        self.nodes[i+1] = self.ui.create_text(x1+85, y, text=str(itr.next.val), font=('bold'))
                else:
                    if int(str(itr.val)) < int(str(itr.next.val)):
                        clear = False
                        temp = itr.val
                        itr.val = itr.next.val
                        itr.next.val = temp
                        self.ui.delete(self.nodes[i])
                        self.ui.delete(self.nodes[i+1])
                        self.nodes[i] = self.ui.create_text(x1+40, y, text=str(itr.val), font=('bold'))
                        self.nodes[i+1] = self.ui.create_text(x1+85, y, text=str(itr.next.val), font=('bold'))
                x1 += 45
                itr = itr.next
                i += 1

    def show(self):
        l = 'head --> '
        itr = self.head
        while itr:
            l += str(itr.val) + ' --> '
            itr = itr.next
        return l[:-5]
