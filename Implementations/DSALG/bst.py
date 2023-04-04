class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
        self.arr = []
        
    def search(self, tree, val):
        if tree:
            if tree.root == val:
                return True

            elif val > tree.root:
                return self.search(tree.right, val)

            elif val < tree.root:
                return self.search(tree.left, val)

        else:
            return False

    def add(self, value):
        if self.root:
            if self.root == value:
                return
            else:
                if value < self.root:
                    if self.left:
                        self.left.add(value)
                    else:
                        self.left = Tree(value)
                else:
                    if self.right:
                        self.right.add(value)
                    else:
                        self.right = Tree(value)
        else:
            self.root = Tree(value)
        
    def iot(self, root):
        if root:
            self.iot(root.left)
            self.arr.append(root.root)
            self.iot(root.right)
        
    def pot(self, root):
        if root:
            self.arr.append(root.root)
            self.pot(root.right)
            self.pot(root.left)

    def pot_1(self, root):
        if root:
            self.pot_1(root.left)
            self.pot_1(root.right)
            self.arr.append(root.root)
        
    def show(self):
        arr = self.arr
        self.arr = []
        return arr


if __name__ == '__main__':
    t = Tree(5)
    t.add(2)
    t.add(1)
    t.add(7)
    t.add(6)
    t.add(8)
    t.iot(t)
    print(t.show())
    t.pot(t)
    print(t.show())
    t.pot_1(t)
    print(t.show())
    print(t.search(t, 1))
