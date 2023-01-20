import numpy as np
from copy import deepcopy

def eye(size):
    new_matrix = []
    for i in range(size):
        temp = []
        for j in range(size):
            if i == j:
                temp += [1]
            else:
                temp += [0]
        new_matrix += [temp]


    return new_matrix


def out_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp += [matrix[j][i]]
        new_matrix += [temp]

    return new_matrix


def dot(one, two):
    new_matrix = []
    for i in range(len(one)):
        temp = []
        for j in range(len(two[0])):
            value = 0
            for k in range(len(one[0])):
                value += one[i][k]*two[k][j]

            temp += [value]
        new_matrix += [temp]

    return new_matrix


def l2_norm(x):
    return np.sqrt(sum([i**2 for i in x]))



def hessenberg(matrix):
    a = deepcopy(matrix)
    memory = []

    for i in range(len(matrix)-2):
        x = [a[k][i] for k in range(i+1, len(matrix))]
        w = [l2_norm(x)]
        w += [0]*(len(x)-1)
        v = [w[k] - x[k] if a[i+1][i+1] < 0 else w[k] + x[k] for k in range(len(x))]
        upper = dot(transpose([v]), [v])
        lower = dot([v], transpose([v]))[0][0]
        for j in range(len(upper)):
            for k in range(len(upper)):
                upper[j][k] /= lower

        h_hat = eye(len(upper))
        for j in range(len(upper)):
            for k in range(len(upper)):
                h_hat[j][k] -= 2*upper[j][k]

        h_ref = eye(len(matrix))
        si = 0
        for k in range(len(matrix)):
            temp = []
            sj = 0
            for j in range(len(matrix)):
                if k > i:
                    if j > i:
                        h_ref[k][j] = h_hat[si][sj]
                        sj += 1
            if k > i:
                si += 1
        
        cop = dot(dot(h_ref, a), h_ref)
        a = deepcopy(cop)
        out_matrix(h_ref)
        memory += [deepcopy(h_ref)]


    # a = memory[0]

    # for i in memory[1:]:
    #     a = dot(deepcopy(a), deepcopy(i))

    return a



matrix = [[1.2, 3.1, 6.7, 7.7], [5.3, 6.6, 1.9, 2.2], [4.5, 7.2, 8.9, 6.6], [3.7, 8.1, 9, 1]]

matrix1 = [[1, 0, 2, 3], [-1, 0, 5, 2], [2, -2, 0, 0], [2, -1, 2, 0]]

matrix3 = [[-149 ,   -50,   -154], [537  ,  180 ,   546], [-27  ,   -9  ,  -25]]


hess = hessenberg(matrix3)


out_matrix(hess)