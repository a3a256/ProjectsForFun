class Binary:
    def __init__(self, root, ui, x, y, height=16):
        self.root = root
        self.left = None
        self.right = None
        self.ui = ui
        self.ui.create_text(x, y, text=str(self.root),font=('Helvetica', str(height), 'bold'))
        self.ui.pack()
        self.vals = []
        

    def add(self, value, text_x, text_y, line_x, line_y, coef=200):
        if self.root is None:
            self.root = Binary(value, None, None)
            return
        else:
            if value >= self.root:
                if self.right:
                    self.right.add(value, text_x+coef, text_y+70, line_x+coef, line_y+70, coef=coef-(coef//2))
                else:
                    self.ui.create_line((line_x), line_y+5, (line_x)+coef, (line_y+50), width=1.5)
                    self.right = Binary(value, self.ui, text_x+coef, text_y+80)
            else:
                if self.left:
                    self.left.add(value, text_x-coef, text_y+70, line_x-coef, line_y+70, coef=coef-(coef//2))
                else:
                    self.ui.create_line(line_x, line_y+5, line_x-coef, line_y+50, width=1.5)
                    self.left = Binary(value, self.ui, text_x-coef, text_y+80)

    def pot(self, tree):
        if tree:
            self.vals.append(tree.root)
            self.pot(tree.left)
            self.pot(tree.right)

    def iot(self, tree):
        if tree:
            self.iot(tree.left)
            self.vals.append(tree.root)
            self.iot(tree.right)

    def post(self, tree):
        if tree:
            self.post(tree.left)
            self.post(tree.right)
            self.vals.append(tree.root)
            
    def height(self, tree):
        if tree:
            return 1+max(self.height(tree.left), self.height(tree.right))
        else:
            return -1

    def show(self):
        l = ''
        for i in self.vals:
            l += str(i) + ', '
        self.vals = []
        return l[:-2]

if __name__ == '__main__':
    bn = Binary(5)
    bn.add(3)
    bn.add(4)
    bn.add(2)
    bn.add(7)
    bn.add(6)
    bn.add(8)
    bn.pot(bn)
    print('-'*10)
    bn.iot(bn)
    print('-'*10)
    bn.post(bn)
