class CombinePermutation:
    def __init__(self, size_of_set, selected):
        self.size_of_set = size_of_set
        self.selected = selected

    def factorial_count(self, val):
        num = 1
        for i in range(1, val+1):
            num *= i
        return num

    def permute(self):
        upper = self.factorial_count(self.size_of_set)
        lower = self.factorial_count(self.size_of_set - self.selected)
        return upper/lower

    def combine(self):
        upper = self.factorial_count(self.size_of_set)
        lower = self.factorial_count(self.size_of_set-self.selected)*self.factorial_count(self.selected)
        return upper/lower

    
if __name__ == "__main__":
    cp = CombinePermutation(10, 8)
    print(cp.combine())
    print(cp.permute())
