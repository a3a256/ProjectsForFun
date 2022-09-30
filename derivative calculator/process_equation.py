class Tools:
    def get_num(val, target):
        weight = []
        i = 0
        if target in val:
            while val[i] != target:
                weight.append(val[i])
                i += 1
        else:
            return val
        if not weight:
            return "1"
        return "".join(weight)

    def extract_exponent(val):
        if not Tools.is_exponent(val):
            return "1"
        length = len(val)
        end = length-2
        e = ""
        while val[end] != "(":
            e += val[end]
            end -= 1
        return e

    def is_exponent(val):
        if "^" in val:
            return True
        return False


class PreProcess:
    def __init__(self, equation, target, ops):
        self.eq = equation
        self.target = target
        self.ops = ops

    def exponent_equality(self, x1, x2):
        e1 = Tools.extract_exponent(x1)
        e2 = Tools.extract_exponent(x2)
        if e1 == e2:
            return True
        return False

    def multiplication(self, val1, val2):
        weight1 = Tools.get_num(val1, self.target)
        weight2 = Tools.get_num(val2, self.target)
        e1 = Tools.extract_exponent(val1)
        e2 = Tools.extract_exponent(val2)
        new_weight = str(int(weight1)*int(weight2))
        new_e = str(int(e1)+int(e2))
        if new_e == "1":
            return new_weight + "x"
        if new_e == "0":
            return new_weight
        return new_weight+self.target+"^({})".format(new_e)

    def process_num(self, val):
        exp = False
        weight = Tools.get_num(val, self.target)
        e = ""
        if "^" in weight:
            l = len(val) - 2
            while weight[l] != "(":
                e += weight[l]
                l -= 1
            i = 0
            n = ""
            while val[i] != "^":
                n += val[i]
                i += 1
            return str(int(n)**(int(e)))
        else:
            return weight

    def division(self, val1, val2):
        weight1 = Tools.get_num(val1, self.target)
        weight2 = Tools.get_num(val2, self.target)
        e1 = Tools.extract_exponent(val1)
        e2 = Tools.extract_exponent(val2)
        new_weight = str(int(int(weight1)/int(weight2)))
        new_e = ""
        if int(e1) < int(e2):
            new_e = str(int(e2) - int(e1))
        else:
            new_e = str(int(e1) - int(e2))
        if new_e == "1":
            return new_weight + "x"
        if new_e == "0":
            return new_weight
        return new_weight + self.target + "^({})".format(new_e)
        
    def basic(self, val1, val2, op):
        if self.exponent_equality(val1, val2):
            if op == "+":
                if int(Tools.extract_exponent(val1)) > 1:
                    return str(int(Tools.get_num(val1, self.target)) + int(Tools.get_num(val2, self.target))) + self.target + "^({})".format(Tools.extract_exponent(val1))
                else:
                    return str(int(Tools.get_num(val1, self.target)) + int(Tools.get_num(val2, self.target))) + self.target
            else:
                if int(Tools.get_num(val1, self.target)) < int(Tools.get_num(val2, self.target)):
                    if int(Tools.extract_exponent(val1)) > 1:
                        return "-" + str(int(Tools.get_num(val2, self.target)) - int(Tools.get_num(val1, self.target))) + self.target + "^({})".format(Tools.extract_exponent(val1))
                    else:
                        return "-" + str(int(Tools.get_num(val2, self.target)) - int(Tools.get_num(val1, self.target))) + self.target
                if int(Tools.extract_exponent(val1)) > 1:
                    return str(int(Tools.get_num(val1, self.target)) - int(Tools.get_num(val2, self.target))) + self.target + "^({})".format(Tools.extract_exponent(val1))
                else:
                    return str(int(Tools.get_num(val1, self.target)) - int(Tools.get_num(val2, self.target))) + self.target
        else:
            return "not equal"
    
    def legit(self, val1, val2):
        if (self.target in val1) and (self.target in val2):
            return True
        else:
            return False

    def arg_process(self, val):
        if Tools.is_exponent(val):
            return val
        if Tools.is_exponent(val):
            return val + "^(1)"

    def exponent_change(self):
        length = len(self.eq)
        for i in range(length):
            self.eq[i] = self.arg_process(self.eq[i])

    def mix_multiply(self, val1, val2):
        weight1 = Tools.get_num(val1, self.target)
        weight2 = Tools.get_num(val2, self.target)
        e = ""
        if self.target in val1:
            e += Tools.extract_exponent(val1)
        else:
            e += Tools.extract_exponent(val2)
        new_weight = int(weight1)*int(weight2)
        return str(new_weight)+self.target+"^({})".format(e)

    def distibute(self, val1, val2, op):
        if op == "*":
            return self.multiplication(val1, val2)
        elif op == "/":
            return self.division(val1, val2)
        elif self.legit(val1, val2) == "mix":
            pass
        else:
            return self.basic(val1, val2, op)
    
    def processing(self):
        length = len(self.ops)
        new_expression = []
        mul_div_id = []
        if ("*" in self.ops) or ("/" in self.ops):
            for j in range(len(self.ops)):
                if self.ops[j] == "*" or self.ops[j] == "/":
                    mul_div_id.append(j)
        if mul_div_id:
            for i in mul_div_id:
                if self.eq[i] != "_":
                    if self.legit(self.eq[i], self.eq[i+1]):
                        if self.eq[i] != "_":
                            self.eq[i] = self.distibute(self.eq[i], self.eq[i+1], self.ops[i])
                            new_expression.append(self.eq[i])
                            self.eq[i+1] = "_"
                            self.ops[i] = "_"
                    elif self.legit(self.eq[i], self.eq[i+1]) == "mix":
                        if self.eq[i] != "_":
                            self.eq[i] = self.distibute(self.eq[i], self.eq[i+1], self.ops[i])
                            new_expression.append(self.eq[i])
                            self.eq[i+1] = "_"
                            self.ops[i] = "_"
                else:
                    j = i
                    while self.eq[j] == "_":
                        j -= 1
                    if self.legit(self.eq[j], self.eq[i+1]):
                        self.eq[j] = self.distibute(self.eq[j], self.eq[i+1], self.ops[i])
                        self.eq[i+1] = "_"
                        self.ops[i] = "_"
                        new_expression.append(self.eq[j])
        while "_" in self.ops:
            self.ops.remove("_")
        while "_" in self.eq:
            self.eq.remove("_")
        for l in range(len(self.ops)):
            for q in range(l+1, len(self.eq)):
                b = ""
                if self.eq[q] != "_" and self.eq[l] != "_":
                    print(self.eq[l], self.eq[q])
                    if self.legit(self.eq[l], self.eq[q]):
                        a = self.distibute(self.eq[l], self.eq[q], self.ops[q-1])
                        if a != "not equal":
                            self.eq[l] = a
                            self.eq[q] = "_"
                            self.ops[q-1] = "_"
        while "_" in self.eq:
            self.eq.remove("_")
        while "_" in self.ops:
            self.ops.remove("_")
        print(self.eq)
        return self.eq, self.ops
