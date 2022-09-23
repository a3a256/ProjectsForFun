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
        self.target = equation
        self.ops = ops

    def exponent_equality(self, x1, x2):
        e1 = Tools.extract_exponent(x1)
        e2 = Tools.extract_exponent(x2)
        if e1 == e2:
            return True
        return False

    def multiplication(self, val1, val2):
        weight1 = Tools.get_num(val1, self.target)
        weight2 = Tools.get_hum(val2, self.target)
        e1 = Tools.extract_exponent(val1)
        e2 = Tools.extract_exponent(val2)
        new_weight = str(int(weight1)*int(weight2))
        new_e = str(int(e1)+int(e2))
        if new_e == "1":
            return new_weight + "x"
        if new_e == "0":
            return new_weight
        return new_weight+self.target+"^({})".format(new_e)

    def division(self, val1, val2):
        weight1 = Tools.get_num(val1, self.target)
        weight2 = Tools.get_hum(val2, self.target)
        e1 = Tools.extract_exponent(val1)
        e2 = Tools.extract_exponent(val2)
        new_weight = str(int(weight1)/int(weight2))
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
                return str(int(Tools.get_num(val1)) + int(Tools.get_num(val2))) + self.target + "^({})".format(Tools.extract_exponent(val1))
            else:
                if int(Tools.get_num(val1)) < int(Tools.get_num(val2)):
                    return "-" + str(int(Tools.get_num(val2)) + int(Tools.get_num(val1))) + self.target + "^({})".format(Tools.extract_exponent(val1))
                return str(int(Tools.get_num(val1)) - int(Tools.get_num(val2))) + self.target + "^({})".format(Tools.extract_exponent(val1))
    
    def legit(self, val1, val2):
        print(val1)
        print(val2)
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

    def distibute(self, val1, val2, op):
        if op == "*":
            return self.multiplication(val1, val2)
        elif op == "/":
            return self.division(val1, val2)
        else:
            return self.basic(val1, val2)
    
    def processing(self):
        length = len(self.ops)
        new_expression = ""
        mul_div_id = []
        if ("*" in self.ops) or ("/" in self.ops):
            for j in range(len(self.ops)):
                mul_div_id.append(j)
        if mul_div_id:
            for i in mul_div_id:
                if self.eq[i] != "_":
                    if self.legit(self.eq[i], self.eq[i+1]):
                        if self.eq[i] != "_":
                            self.eq[i] = self.distibute(self.eq[i], self.eq[i+1], self.ops[i])
                            self.eq[i+1] = "_"
                            self.ops[i] = "_"
                else:
                    j = i
                    while self.eq[j] == "_":
                        j -= 1
                    self.eq[j] = self.distibute(self.eq[l], self.eq[i+1], self.ops[i])
        else:
            while "_" in self.ops:
                self.ops.remove("_")
            while "_" in self.eq:
                self.eq.remove("_")
            for l in range(len(self.ops)):
                if self.legit(self.eq[l], self.eq[l+1]):
                    self.eq[l] = self.distibute(self.eq[l], self.eq[l+1], self.ops[l])
                    self.ops[l] = "_"
        return self.eq, self.ops