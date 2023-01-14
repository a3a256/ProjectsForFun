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

def inverse(arr):
    identity = eye(len(arr))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            while not is_diagonal(arr):
                pass