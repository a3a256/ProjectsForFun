class Combine:
    def __init__(self, size_of_set, selected):
        self.size_of_set = size_of_set
        self.selected = selected

    def permutate(self, val):
        num = 1
        for i in range(1, val+1):
            num *= i
        return num

    def execute(self):
        upper = self.permutate(self.size_of_set)
        lower = self.permutate(self.size_of_set-self.selected)*self.permutate(self.selected)
        return upper/lower

    
if __name__ == "__main__":
    cm = Combine(10, 8)
    print(cm.execute())