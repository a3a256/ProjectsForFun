from copy import deepcopy

def determinant(arr):
    if len(arr) == 1:
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
        det += arr[0][i]*coef**(1+(i+1))*determinant(new_row)

    return det


def matrix_equations(matrix, answers):
    orig_det = determinant(matrix)

    arguments = []

    temp = []

    for i in range(len(matrix)):
        temp = deepcopy(matrix)
        for j in range(len(matrix)):
            temp[j][i] = answers[j]

        arguments += [determinant(temp)/orig_det]

    return arguments


matrix = [[8, 4], [5, 11]]
ans = [4, 12]

print(matrix_equations(matrix, ans))