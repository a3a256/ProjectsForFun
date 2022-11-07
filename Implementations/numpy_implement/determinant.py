class Array:
    def __init__(self, arr):
        self.arr = arr

    def vector(self):
        return self.arr

    def dims(self):
        return [len(self.arr), len(self.arr[0])]

    def det(self, arr):
        if len(arr) == 1:
            print(arr)
            return arr[0][0]
        coef = -1
        det = 0
        for i in range(len(arr[0])):
            new_row = []
            for j in range(1, len(arr)):
                temp = []
                for k in range(len(arr[0])):
                    if k!=i:
                        temp += [arr[j][k]]
                new_row += [temp]
            print(new_row)
            det += arr[0][i]*coef**(1+(i+1))*self.det(new_row)

        return det



if __name__ == "__main__":
    arr = Array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(arr.det(arr.vector()))