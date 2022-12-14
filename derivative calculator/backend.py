import process_equation
from process_equation import Tools

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
        temp = "0"
        if self.equation[0] == "-" or self.equation[0] == "+":
            temp = "0"
            temp += self.equation
            self.equation = temp
        else:
            temp = "0+"
            temp += self.equation
            self.equation = temp
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
        if self.target in val:
            while val[i] != self.target:
                weight.append(val[i])
                i += 1
        else:
            return val
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

    def derivative_mul(self, one, two):
        one_weight = str(self.get_num(one))
        two_weight = str(self.get_num(two))
        one_power = 0
        two_power = 0
        if not self.is_exponent(one_weight):
            if self.target in one:
                one_power = 1
            else:
                one_power = 0
        else:
            one_power = int(self.extract_exponent(one))
        if not self.is_exponent(two_weight):
            if self.target in two:
                two_power = 1
            else:
                two_power = 0
        else:
            two_power = int(self.extract_exponent(two))
        new_weight = str(int(one_weight)*int(two_weight))
        new_power = str(one_power+two_power)
        if new_power == "1":
            return str(new_weight)+self.target
        return str(new_weight)+self.target+"^("+str(new_power)+")"

    def arg_equal(self, x1, x2):
        e1 = self.extract_exponent(x1)
        e2 = self.extract_exponent(x2)
        if e1 == e2:
            return True
        return False

    def derive_arithmetics(self, val1, val2, op):
        weight1 = self.get_num(val1)
        weight2 = self.get_num(val2)
        e = self.extract_exponent(val1)
        if op == "+":
            return str(int(weight1) + int(weight2)) + self.target + "^({})".format(e)
        if op == "-":
            if int(weight1) > int(weight2):
                return str(int(weight1)-int(weight2)) + self.target + "^({})".format(e)
            else:
                return "-" + str(int(weight2)-int(weight1)) + self.target + "^({})".format(e)

    def derive_full(self):
        vals = self.extract_nums()
        t = process_equation.PreProcess(vals, self.target, self.operands)
        vals, ops = t.processing()
        new_vals = []
        new_expression = ""
        for i in vals:
            new_vals.append(self.derive_one_num(i))
        new_expression += new_vals[0]
        if len(new_vals)>1:
            for i in range(1, len(new_vals)):
                new_expression += ops[i-1] + new_vals[i]
        return new_expression
