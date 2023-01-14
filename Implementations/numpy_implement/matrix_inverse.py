import numpy as np

matrix = [[1.2, 3.1, 6.7], [5.3, 6.6, 1.9], [4.5, 7.2, 8.9]]

print(np.array(matrix))

print(np.linalg.inv(matrix))

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

def row_closest(arr, row, column, ie):
    close_row = None
    close_column = None
    dd = dict()
    for i in range(len(arr)):
        if i != row:
            diff = arr[row][column] - arr[i][column]
            if diff not in dd:
                if arr[i][column] != 0:
                    dd[diff] = [[i, column]]
            else:
                if arr[i][column] != 0:
                    dd[diff] += [[i, column]]

    sorted_keys = sorted(dd, key=lambda x: x)
    print(sorted_keys)
    index = sorted_keys[0]

    close_row = dd[index][0][0]

    close_column = dd[index][0][1]

    # print(close_column)

    value = arr[close_row][close_column]

    coef = arr[row][column]/value if value > arr[row][column] else value/arr[row][column]

    if arr[row][column] > 0 and value > 0:
        coef *= -1
    elif arr[row][column] < 0 and value < 0:
        coef *= -1

    temp_real = [arr[close_row][k]*coef for k in range(len(arr))]

    temp_eye = [ie[close_row][k]*coef for k in range(len(arr))]

    for k in range(len(arr[0])):
        ie[row][k] += temp_eye[k]
        arr[row][k] += temp_real[k]

    return arr, ie

def augment(arr, ide):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i != j:
                if arr[i][j] != 0:
                    arr, ide = row_closest(arr, i, j, ide)
                    print(ide)

    return ide

def inverse(arr):
    identity = eye(len(arr))
    return augment(arr, identity)


ans = inverse(matrix)

print(np.array(ans))
