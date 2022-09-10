from app import Calculator

class Implement:
    def __init__(self, nums, operations):
        self.nums = nums
        self.operations = operations
        self.res = nums[0]

    def distribute(self):
        length = len(self.operations)
        for i in range(length):
            if self.operations[i] == "+":
                self.res += self.nums[i+1]
            if self.operations[i] == "-":
                self.res -= self.nums[i+1]
            if self.operations[i] == "*":
                self.res = self.res*self.nums[i+1]
            if self.operations[i] == "/":
                self.res = self.res/self.nums[i+1]
        return self.res