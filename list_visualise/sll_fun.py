class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

class sll:
    def __init__(self, data):
        self.head = Node(data, None)

    def add_start(self, val):
        itr = self.head
        if itr.data:
            self.head = Node(val, itr)
        else:
            self.head = Node(val, None)

    def add_end(self, val):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)

    def show(self):
        l = 'head --> '
        itr = self.head
        while itr:
            l += str(itr.data) + ' --> '
            itr = itr.next
        return l[:-5]

    def sort(self, asc=True):
        clear = False
        while not clear:
            clear = True
            itr = self.head
            while itr.next:
                if not asc:
                    if int(str(itr.data)) < int(str(itr.next.data)):
                        clear = False
                        temp = itr.data
                        itr.data = itr.next.data
                        itr.next.data = temp
                else:
                    if int(str(itr.data)) > int(str(itr.next.data)):
                        clear = False
                        temp = itr.data
                        itr.data = itr.next.data
                        itr.next.data = temp
                itr = itr.next

    def length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, num):
        count = 0
        itr = self.head
        while count < index-1:
            count += 1
            itr = itr.next
        itr.next = Node(num, itr.next)

    def replace_at(self, index, num):
        count = 0
        etr = self.head
        itr = self.head
        while count < index-1:
            count += 1
            itr = itr.next
        itr.next = Node(num, itr.next)
        i = 0
        while i < index:
            i += 1
            etr = etr.next
        etr.next = etr.next.next

    def reverse(self):
        ln = self.length()//2
        count = 0
        ert = self.head
        while count < ln:
            itr = self.head
            end = self.length() - (count + 1)
            i = 0
            while i < end:
                itr = itr.next
                i += 1
            temp = ert.data
            ert.data = itr.data
            itr.data = temp
            ert = ert.next
            count += 1

def main():
    first = int(input("Enter the first number:"))
    sl = sll(first)
    print(sl.show())
    end = False
    while not end:
        other = str(input("Enter the next node:"))
        if other.lower() == 'no':
            end = True
        else:
            sl.add_end(int(other))
            print(sl.show())
    act = True
    while act:
        choice = input("What's next?")
        if choice.lower() == 'nothing':
            act = False
        else:
            if choice == 'reverse':
                sl.reverse()
                print(sl.show())
            if choice == 'sort':
                ask = input("Ascending of descdending order (asc/desc)?")
                if ask.lower() == "asc":
                    sl.sort()
                    print(sl.show())
                if ask.lower() == "desc":
                    sl.sort(asc=False)
                    print(sl.show())
            if choice == 'replace':
                ask = input("Replace at:")
                rep = input("Replacement:")
                sl.replace_at(int(ask), int(rep))
                print(sl.show())
    print("Resulting Singly Linked List")    
    print(sl.show())
