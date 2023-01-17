import numpy as np
from copy import deepcopy

def out_matrix(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

def transpose(arr):
    new_matrix = []
    for i in range(len(arr[0])):
        temp = []
        for j in range(len(arr)):
            temp += [arr[j][i]]
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


def normalize(vector):
    return np.sqrt(sum([i**2 for i in vector]))


def allclose(one, two, tol=0.00001):
    if abs(one-two) <= tol:
        return True
    else:
        return False


def aproximate(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if allclose(arr[i][j], 0):
                arr[i][j] = 0
    return arr


def house_holder_reflections(matrix):
    length = len(matrix)
    es = []
    r = deepcopy(matrix)
    common_length = len(matrix)

    for i in range(len(matrix)):
        sliced_matrix = []
        e = eye(length)
        for j in range(i, len(r)):
            temp = []
            for k in range(i, len(r)):
                temp += [r[j][k]]
            sliced_matrix += [temp]
        a = [matrix[k][i] for k in range(len(matrix))]
        l2 = normalize(a)
        # v = [sliced_matrix[k][0] + e[k][0] * l2 for k in range(len(e))]
        v = [sliced_matrix[k][0] + e[k][0] * l2 if r[i][i] >=0 else sliced_matrix[k][0] - e[k][0] * l2 for k in range(len(e))]
        upper = dot(transpose([v]), [v]) #if i > 0 else dot(transpose([a]), [a])
        lower = dot([v], transpose([v]))[0][0] #if i > 0 else dot([a], transpose([a]))[0][0]
        # out_matrix(upper)
        # print(lower)
        for j in range(len(upper)):
            for k in range(len(upper[0])):
                e[j][k] -= 2*(upper[j][k]/lower)
        # out_matrix(e)
        # print("-----")
        si = 0
        ref_e = []
        for k in range(common_length):
            temp = []
            sj = 0
            for j in range(common_length):
                if k >= i:
                    if j >= i:
                        temp += [e[si][sj]]
                        sj += 1
                    else:
                        temp += [0]
                else:
                    if k == j:
                        temp += [1]
                    else:
                        temp += [0]
            ref_e += [temp]
            if k >= i:
                si += 1
        # out_matrix(ref_e)
        # print()
        cop = dot(ref_e, r)
        r = deepcopy(aproximate(cop))
        es += [deepcopy(r)]
        length -= 1
    out_matrix(dot(es[0], es[1]))
    q = dot(dot(es[0], es[1]), es[2])

    for i in es:
        out_matrix(i)
        print("-"*10)

    return q, r


matrix = [[2, -2, 18], [2, 1, 0], [1, 2, 0]]

q, r = house_holder_reflections(matrix)

qq, rr = np.linalg.qr(matrix)
print("Q ", qq)

print("R ", rr)

print("Q")
out_matrix(q)

print("R")
out_matrix(r)