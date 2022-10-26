class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add(self, val):
        if not self.val:
            self.val = Tree(val)
            return
        ask = input("Do you want to go to the next level?[y/n]")
        if ask.lower() == "n":
            self.children.append(Tree(val))
        else:
            if len(self.children) > 1:
                ask = int(input("Which child would we go to?[index]-"))
                if self.children[ask]:
                    self.children[ask].add(val)
                else:
                    self.children[ask] = Tree(val)
    
    def level_order(self, root):
        if not root:
            return

        q = []
        q.append(root)
        while len(q) != 0:
            n = len(q)
            while n>0:
                p = q.pop(0)
                print(p.val, end=" ")

                for i in range(len(p.children)):
                    q.append(p.children[i])

                n -= 1

            print()



if __name__ == "__main__":
    tree = Tree(10)
    while True:
        n = int(input("Add number to the tree: "))
        tree.add(n)
        ask = input("Done?")
        if ask.lower() == "y":
            break

    tree.level_order(tree)