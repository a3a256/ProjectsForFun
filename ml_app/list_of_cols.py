class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data, None)


    def add(self, val):
        itr = self.head
        if itr.data is None:
            self.head = Node(val, None)
        else:
            while itr.next:
                itr = itr.next
            itr.next = Node(val, None)

    def show(self):
        l = ""
        itr = self.head
        while itr:
            l += str(itr.data) + ", "
            itr = itr.next
        return l[:-2]