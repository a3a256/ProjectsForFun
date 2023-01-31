import numpy as np
from copy import deepcopy


def mean(arr):
    return sum(arr)/len(arr)


def variance(arr):
    return sum([(i - mean(arr))**2 for i in arr])/len(arr)


def covar(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    upper = [(i-mean_x)*(j-mean_y) for i, j in zip(x, y)]
    return sum(upper)/len(x)


def cov(arr):
    res = []
    row = []
    x = []
    y = []
    for k in range(len(arr[0])):
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                if i == k:
                    x += [arr[j][i]]
                else:
                    x += [arr[j][k]]
                    y += [arr[j][i]]
            if i == k:
                row += [variance(x)]
            else:
                row += [covar(x, y)]
            x = []
            y = []
        res += [row]
        row = []

    
    return res

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
    # qq, _ = house_holder_reflections(deepcopy(matrix))
    # qq = eye(len(matrix))
    ak = deepcopy(matrix)
    save = []
    for _ in range(iter):
        s = ak[-1][-1]
        iden = eye(len(matrix))
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

        # qq = dot(qq, q)
        save += [deepcopy(q)]

        if is_trangular(deepcopy(ak)):
            break

    end = save[0]

    for i in save[1:]:
        end = dot(end, i)


    return ak, end


def conjugate(a, b):
    x = [[1]*len(a)]
    x = transpose(x)
    ans = dot(a, x)
    p0 = []
    for i in range(len(ans)):
        temp = []
        for j in range(len(ans[0])):
            temp += [b[i][j] - ans[i][j]]
        p0 += [temp]
    r0 = deepcopy(p0)
    alpha = dot(transpose(p0), p0)[0][0]/dot(dot(transpose(p0), a), p0)[0][0]
    for i in range(len(x)):
        x[i][0] += alpha*p0[i][0]
    for _ in range(1, len(b)):
        mp = dot(a, p0)
        second = transpose([[alpha*mp[k][0] for k in range(len(mp))]])
        r_next = transpose([[r0[k][0] - second[k][0] for k in range(len(second))]])
        beta = dot(transpose(r_next), r_next)[0][0]/dot(transpose(r0), r0)[0][0]
        p_next = transpose([[r_next[k][0] + beta*p0[k][0] for k in range(len(r_next))]])
        alpha = dot(transpose(r_next), r_next)[0][0]/dot(dot(transpose(p_next), a), p_next)[0][0]
        for i in range(len(x)):
            x[i][0] += alpha*p_next[i][0]

        r0 = deepcopy(r_next)
        p0 = deepcopy(p_next)


    return transpose(x)[0]


def zeros(size):
    zero = []
    if isinstance(size, int):
        for i in range(size):
            temp = []
            for j in range(size):
                temp += [0]
            zero += [temp]

        return zero

    if isinstance(size, tuple):
        for i in range(size[0]):
            temp = []
            for j in range(size[1]):
                temp += [0]

            zero += [temp]

        return zero



def eigenvector(matrix):
    vals, _ = qr_algorithm(matrix)

    values = diag(vals)

    vectors = []

    for k in range(len(values)):
        temp = deepcopy(matrix)

        zero = zeros((len(matrix), 1))
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    temp[i][j] -= values[k]

        _val = conjugate(deepcopy(temp), zero)

        vectors += [deepcopy(_val)]

    return vectors


def eigenvector1(matrix):
    vals, _ = qr_algorithm(matrix)

    values = diag(vals)

    vectors = []

    for k in range(len(values)):
        temp = deepcopy(matrix)

        zero = zeros((len(matrix), 1))
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    temp[i][j] -= values[k]

        _val, _ = qr_algorithm(temp)

        vectors += [diag(_val)]


    return vectors


# matrix = [[1.2, 3.1, 6.7, 7.7], [5.3, 6.6, 1.9, 2.2], [4.5, 7.2, 8.9, 6.6], [3.7, 8.1, 9, 1]]

# a, q = qr_algorithm(matrix)

# # gg = eigenvector(matrix)

# # out_matrix(a)

# print()

# print("***Implemented***Eigenvalue")
# print(diag(a))
# print("***Implemented***Eigenvector")
# out_matrix(q)

# print()

# vals, vecs = np.linalg.eig(matrix)

# print("***Real***Eigenvalue")
# print(vals)

# print("***Real***Eigenvector")
# out_matrix(vecs)



matrix = [[-16, -28, -19], [42, 69, 46], [-42, -72, -49]]

covd = cov(matrix)

out_matrix(covd)

a, q = qr_algorithm(covd)

r, t = qr_algorithm(covd)

print(diag(a))

print("-"*10)

out_matrix(t)

vv = eigenvector(matrix)

# out_matrix(vv)

a, b = np.linalg.eig(covd)

print(a, b)

print("Cov", np.cov(transpose(matrix)))
