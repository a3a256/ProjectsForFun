class Node:
    def __init__(self, val, _next):
        self.val = val
        self.next = _next


class SinglyLinkedList:
    def __init__(self, value):
        self.head = Node(value, None)


    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, None)


        else:

            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = Node(value, None)


    def insert_start(self, value):

        if self.head is None:
            self.head = Node(value, None)


        else:
            self.head = Node(value, self.head)


    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1


        return count

    def merge(self, left, right):
        i = 0
        j = 0

        res = None

        itr_l = left.head
        itr_r = right.head

        while i < left.get_length() and j<right.get_length():
            if itr_l.val < itr_r.val:
                if res is None:
                    res = SinglyLinkedList(itr_l.val)
                else:
                    res.insert_end(itr_l.val)

                i += 1
                itr_l = itr_l.next

            else:
                if res is None:
                    res = SinglyLinkedList(itr_r.val)
                else:
                    res.insert_end(itr_r.next)

                itr_r = itr_r.next

                j += 1

        if j < right.get_length():
            while itr_r:
                res.insert_end(itr_r.val)
                itr_r = itr_r.next

        if i < left.get_length():
            while itr_l:
                res.insert_end(itr_l.val)
                itr_l = itr_l.next

        return res


    def mergeSort(self, sll):
        if sll.get_length() == 1:
            print('hit')
            return sll
        itr = sll.head
        length = sll.get_length()
        middle = length//2

        left = SinglyLinkedList(itr.val)
        itr = itr.next
        count = 1
        while count < middle:
            left.insert_end(itr.val)
            itr = itr.next
            count += 1
        left.display()
        right = SinglyLinkedList(itr.val)
        count += 1
        itr = itr.next
        while count < length:
            right.insert_end(itr.val)
            itr = itr.next
            count += 1


        self.merge(self.mergeSort(left), self.mergeSort(right))

        




    def display(self):

        itr = self.head

        while itr:

            print(itr.val, end = " ")

            itr = itr.next

        print()


    


if __name__ == "__main__":
    sll = SinglyLinkedList(1)

    sll.insert_end(2)
    sll.insert_end(3)
    sll.insert_start(5)
    sll.insert_start(4)
    sll.insert_end(8)

    sll.display()

    sll.mergeSort(sll)