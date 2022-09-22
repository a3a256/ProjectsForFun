from tkinter import E


class Distribute:
    def __init__(self, equation, target):
        self.target = target
        self.equation = equation[5:]
        self.rule = ["+", "-", "*", "/"]
        self.operands = []

    def process(self):
        l = list(self.equation)
        for i in l:
            if i == ' ':
                l.remove(i)
        l = "".join(l)
        self.equation = l

    def extract_nums(self):
        vals = []
        nums = ""
        self.process()
        for i in self.equation:
            if i in self.rule:
                self.operands.append(i)
                vals.append(nums)
                nums = ""
            else:
                nums += i
        vals.append(nums)
        return vals

    def clear(self, val):
        while "_" in val:
            val.remove("-")
        return val

    def get_num(self, val):
        weight = []
        i = 0
        while val[i] != "x":
            weight.append(val[i])
            i += 1
        if not weight:
            return "1"
        return "".join(weight)

    def extract_exponent(self, val):
        length = len(val)
        end = length-2
        e = ""
        while val[end] != "(":
            e += val[end]
            end -= 1
        return e

    def is_exponent(self, val):
        if "^" in val:
            return True
        return False

    def derive_one_num(self, val):
        if val == self.target:
            return "1"
        if self.target not in val:
            return "0"
        weight = int(self.get_num(val))
        if not self.is_exponent(val):
            return str(weight)
        powers = int(self.extract_exponent(val))
        new_weight = str(weight*powers)
        new_powers = str(powers-1)
        if new_powers == "1":
            return str(str(new_weight) + str(self.target))
        return str(str(new_weight)+str(self.target)+"^("+str(new_powers)+")")

    def derive_full(self):
        vals = self.extract_nums()
        new_vals = []
        for i in vals:
            new_vals.append(self.derive_one_num(i))
        new_expression = new_vals[0]
        if len(new_vals) > 1:
            for i in range(1, len(new_vals)):
                new_expression += self.operands[i-1] + new_vals[i]
        return new_expression
