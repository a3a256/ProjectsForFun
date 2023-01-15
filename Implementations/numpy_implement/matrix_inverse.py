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
            if abs(diff) not in dd:
                if arr[i][column] != 0:
                    dd[abs(diff)] = [[i, column]]
            else:
                if arr[i][column] != 0:
                    dd[abs(diff)] += [[i, column]]

    sorted_keys = sorted(dd, key=lambda x: x)
    # print("ff" ,dd)
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
    # print(ie)
    return arr, ie

def augment(arr, ide):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i != j:
                if arr[i][j] != 0:
                    arr, ide = row_closest(arr, i, j, ide)
                    # print(ide)

    return ide

def inverse(arr):
    identity = eye(len(arr))
    return augment(arr, identity)

def determinant(arr):
    if len(arr) == 1:
        return arr[0][0]
    det = 0
    coef = -1
    for i in range(len(arr)):
        new_arr = []
        for j in range(1, len(arr)):
            temp = []
            for k in range(len(arr)):
                if k != i:
                    temp += [arr[j][k]]
            new_arr += [temp]
        det += arr[0][i]*coef**(1+(i+1))*determinant(new_arr)

    return det

def find_cofactor(arr):
    new_matrix = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr)):
            temp_matrix = []
            for z in range(len(arr)):
                if z != i:
                    temp_row = []
                    for k in range(len(arr)):
                        if k != j:
                            temp_row += [arr[z][k]]
                    temp_matrix += [temp_row]
            row += [determinant(temp_matrix)]
        new_matrix += [row]
    return new_matrix

def transpose(arr):
    new_matrix = []
    for i in range(len(arr[0])):
        temp = []
        for j in range(len(arr)):
            temp += [arr[j][i]]
        new_matrix += [temp]
    return new_matrix

def cofactor_inverse(arr):
    arr_d = determinant(arr)
    cofactor = transpose(find_cofactor(arr))
    for i in range(len(cofactor)):
        for j in range(len(cofactor[0])):
            cofactor[i][j] /= arr_d

    return cofactor


ans = cofactor_inverse(matrix)

print(np.array(ans))
