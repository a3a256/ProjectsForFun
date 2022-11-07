class KDTree:
    def __init__(self, val):
        self.val = val
        self.children = [None, None, None, None]

    def add(self, x, y):
        if not self.val:
            self.val = KDTree([x, y])
            return

        if x > self.val[0] and y > self.val[1]:
            if self.children[3] is None:
                self.children[3] = KDTree([x, y])
            else:
                self.children[3].add(x, y)
        elif x<self.val[0] and y>self.val[1]:
            if self.children[1] is None:
                self.children[1] = KDTree([x, y])
            else:
                self.children[1].add(x, y)
        elif x<self.val[0] and y<self.val[1]:
            if self.children[0] is None:
                self.children[0] = KDTree([x, y])
            else:
                self.children[0].add(x, y)
        elif x>self.val[0] and y<self.val[1]:
            if self.children[2] is None:
                self.children[2] = KDTree([x, y])
            else:
                self.children[2].add(x, y)

    def traversal(self, root):
        q = [root]

        while len(q)!=0:
            n = len(q)
            while n>0:
                node = q.pop(0)
                print(node.val, end=" ")

                for i in range(4):
                    if node.children[i]:
                        q.append(node.children[i])

                n -= 1

            print()



if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    y = [2, 7, 3, 9, 10, 3, 1, 8, 3]
    tree = KDTree([6, 6])
    for i in range(len(x)):
        tree.add(x[i], y[i])

    tree.traversal(tree)