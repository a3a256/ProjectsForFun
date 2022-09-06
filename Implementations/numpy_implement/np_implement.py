from distutils.log import error
class array:
    def __init__(self, arr):
        self.arr = arr
        column = len(arr[0])
        for i in range(len(arr)):
            if len(arr[i]) != column:
                raise Exception("Number of columns is inconsistent")

    def show(self):
        return self.arr
        
    def shape(self):
        arr = self.arr
        m = len(arr[0])
        n = len(arr)
        return (n, m)

    def T(self):
        arr = []
        m, n = self.shape()
        for i in range(n):
            t = []
            for j in range(m):
                t.append(self.arr[j][i])
            arr.append(t)
        self.arr = arr
        return arr


class dot:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def show(self):
        ans = []
        arr1 = self.arr1
        arr2 = self.arr2
        shape1 = arr1.shape()
        shape2 = arr2.shape()
        if shape1[1] != shape2[0]:
            raise Exception("Wrong dimensionality")
        else:
            for i in range(shape1[0]):
                t = []
                for z in range(shape2[1]):
                    value = 0
                    for j in range(shape1[1]):
                        value += arr1.show()[i][j]*arr2.show()[j][z]
                    t.append(value)
                ans.append(t)
        return ans
    
    
class zeros:
    def __init__(self, rows, columns):
        self.n = rows
        self.m = columns

    def create(self):
        all = []
        for i in range(self.n):
            l = [0]*self.m
            all.append(l)
        arr = array(all)
        return arr.show()


class ones:
    def __init__(self, rows, columns):
        self.n = rows
        self.m = columns

    def create(self):
        all = []
        for i in range(self.n):
            l = [1]*self.m
            all.append(l)
        arr = array(all)
        return arr.show()


def logarithm_power(x, y):
    count = 1
    while y > x:
        y = y//x
        count += 1
    return count


def log(base, target):
    if target == 0:
        raise Exception("Wrong target number, cannot be 0")
    if base == target:
        return 1
    if target == 1:
        return 0
    count = 0
    if base < target:
        return logarithm_power(base, target)
    else:
        return 1/(logarithm_power(target, base))


def lg(target):
    if target == 1:
        return 0
    count = 1
    while target > 10:
        target = target//10
        count += 1
    return count
