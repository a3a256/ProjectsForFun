import numpy as np
from copy import deepcopy

def diag(arr):
    new_matrix = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                new_matrix += [arr[i][j]]

    return new_matrix

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
            if j < i:
                if allclose(arr[i][j], 0):
                    arr[i][j] = 0
    return arr

def is_trangular(arr):
    arr = aproximate(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if j < i:
                if arr[i][j] != 0:
                    return False
    return True


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
        for j in range(len(upper)):
            for k in range(len(upper[0])):
                e[j][k] -= 2*(upper[j][k]/lower)
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
        cop = dot(ref_e, r)
        r = deepcopy(cop)
        es += [deepcopy(ref_e)]
        length -= 1
    q = deepcopy(es[0])
    for i in es[1:]:
        q = dot(deepcopy(q), deepcopy(i))

    return q, r


def qr_algorithm(matrix, iter=5000):
    qq = eye(len(matrix))
    ak = deepcopy(matrix)
    for _ in range(iter):
        s = ak[-1][-1]
        iden = eye(len(qq))
        shift = []
        for i in range(len(iden)):
            temp = []
            for j in range(len(iden)):
                temp += [iden[i][j]*s]
            shift += [temp]
        temp_a = deepcopy(ak)
        for i in range(len(ak)):
            for j in range(len(ak[0])):
                temp_a[i][j] -= shift[i][j]

        q, r = house_holder_reflections(temp_a)
        reverse = dot(r, q)
        for i in range(len(ak)):
            for j in range(len(ak[0])):
                ak[i][j] = reverse[i][j] + shift[i][j]

        qq = dot(qq, q)

        if is_trangular(ak):
            break


    return ak, qq


def eigenvector(matrix):
    vals, _ = qr_algorithm(matrix)

    values = diag(vals)

    vectors = []

    for _ in range(len(values)):
        temp = deepcopy(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    temp[i][j] -= values[i]

        _val, k = qr_algorithm(temp)

        vectors += [diag(_val)]


    return vectors


matrix = [[1.2, 3.1, 6.7], [5.3, 6.6, 1.9], [4.5, 7.2, 8.9]]

a, q = qr_algorithm(matrix)

print("***Implemented***Eigenvalue")
print(diag(a))
print("***Implemented***Eigenvector")
out_matrix(eigenvector(matrix))

print()

vals, vecs = np.linalg.eig(matrix)

print("***Real***Eigenvalue")
print(vals)

print("***Real***Eigenvector")
print(vecs)
