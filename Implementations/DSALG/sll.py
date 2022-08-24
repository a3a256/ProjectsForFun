from ast import Delete


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, first):
        self.head = Node(first, None)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def add_end(self, value):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)

    def add_start(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        self.head = Node(value, self.head)

    def show(self):
        line = 'head-->'
        itr = self.head
        while itr:
            print(itr.value)
            line += str(itr.value) + '-->'
            itr = itr.next
        return line

    def insert_at(self, index, var):
        itr = self.head
        count = 0
        while count < index:
            itr = itr.next
            count += 1
        temp = itr
        itr.value = var
        itr.next = temp
        


if __name__ == '__main__':
    l = SinglyLinkedList(1)
    l.add_end(2)
    l.add_end(3)
    l.add_start(4)
    l.insert_at(2, 6)
    print(l.show())