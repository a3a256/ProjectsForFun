import numpy as np

matrix = [[1.2, 3.1, 6.7], [5.3, 6.6, 1.9], [4.5, 7.2, 8.9]]

# print(np.linalg.inv(matrix))

def eye(size):
    arr = []
    for i in range(size):
        temp = []
        for j in range(size):
            if i == j:
                temp += [1]
            else:
                temp += [0]
        arr += [temp]

    return arr

def is_diagonal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i != j:
                if arr[i][j] != 0:
                    return False
    return True

def row_closest(arr, row, column):
    close_row = None
    close_column = None
    dd = dict()
    for i in range(len(arr)):
        if i != row:
            diff = arr[row][column] - arr[i][column]
            if abs(diff) not in dd:
                if arr[i][column] != 0:
                    dd[abs(diff)] = [[i, column]]
            else:
                if arr[i][column] != 0:
                    dd[abs(diff)] += [[i, column]]

    sorted_keys = sorted(dd, key=lambda x: x)

def augment(arr, ide):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i != j:
                if arr[i][j] != 0:
                    pass

def inverse(arr):
    identity = eye(len(arr))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            while not is_diagonal(arr):
                pass
