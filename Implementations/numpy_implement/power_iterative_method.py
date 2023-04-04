import numpy as np

from copy import deepcopy

def diag(matrix):
    temp = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                temp += [matrix[i][j]]


    return temp

def allclose(one, two, tol=1e-6):
    return abs(one - two) <= tol

def approximate(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j < i:
                matrix[i][j] = matrix[i][j] if not allclose(matrix[i][j], 0) else 0
    return matrix

def is_triangular(matrix):
    matrix = approximate(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j < i:
                if matrix[i][j] != 0:
                    return False

    return True

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


def dot1(one, two):
    new_matrix = []
    for i in range(len(one)):
        temp = []
        for j in range(len(two[0])):
            value = 0
            for k in range(len(one[0])):
                value += one[i][k] * two[k][j]
            temp += [value]

        new_matrix += [temp]

    return new_matrix


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp += [matrix[j][i]]
        new_matrix += [temp]

    return new_matrix


def eye(size):
    new_matrix = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp += [1 if i == j else 0]

        new_matrix += [temp]

    return new_matrix


def l2_norm(vector):
    if isinstance(vector[0], int) or isinstance(vector[0], float):
        return np.sqrt(sum([i**2 for i in vector]))

    elif isinstance(vector[0], list):
        value = 0
        for i in vector:
            for j in i:
                value += j**2
        return np.sqrt(value)



def qr(matrix):
    es = []
    length = len(matrix)

    common_length = len(matrix)

    r = deepcopy(matrix)

    for i in range(len(matrix)):
        sliced_matrix = []
        for j in range(i, len(matrix)):
            temp = []
            for k in range(i, len(matrix)):
                temp += [r[j][k]]
            sliced_matrix += [temp]

        e = eye(length)

        a = [matrix[i][k] for k in range(len(matrix))]

        l2 = l2_norm(a)
        v = [sliced_matrix[k][0] - e[k][0]*l2 if r[i][i] < 0 else sliced_matrix[k][0] + e[k][0]*l2 for k in range(len(e))]
        upper = dot(transpose([v]), [v])
        lower = dot([v], transpose([v]))[0][0]

        for j in range(len(e)):
            for k in range(len(e)):
                e[j][k] -= 2*(upper[j][k]/lower)

        si = 0

        ref_e = []

        for j in range(common_length):
            temp = []
            sj = 0
            for k in range(common_length):
                if j >= i:
                    if k >= i:
                        temp += [e[si][sj]]
                        sj += 1
                    else:
                        temp += [0]
                else:
                    temp += [1 if k == j else 0]

            ref_e += [temp]
            if j >= i:
                si += 1
        
        r = deepcopy(dot(ref_e, r))
        es += [deepcopy(ref_e)]

        length -= 1

    q = es[0]

    for i in es[1:]:
        q = dot(q, i)


    return q, r


def qr_eigenvalues(matrix, iter=5000):
    qq = eye(len(matrix))
    ak = deepcopy(matrix)
    for _ in range(iter):
        s = ak[-1][-1]
        iden = eye(len(matrix))
        for i in range(len(iden)):
            for j in range(len(iden)):
                iden[i][j] *= s

        temp_a = deepcopy(ak)

        for i in range(len(temp_a)):
            for j in range(len(temp_a[0])):
                temp_a[i][j] -= iden[i][j]

        q, r = qr(temp_a)

        reverse = dot(r, q)

        for i in range(len(ak)):
            for j in range(len(ak)):
                ak[i][j] = reverse[i][j] + iden[i][j]


        qq = dot(qq, q)

        if is_triangular(ak):
            break

    return diag(ak), qq


def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def power_iteration(A, eig_value):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    original = eig_value
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - original) < 0.01:
            break

        v = v_new
        ev = ev_new

    return v_new
    
    # return ev_new, v_new


def power_iterative(matrix):
    values, _ = qr_eigenvalues(matrix)

    v = [1]*len(matrix)

    while True:
        av = dot(matrix, transpose([v]))

        l2 = l2_norm(av)

        v_new = [av[i][0]/l2 for i in range(len(matrix))]

        flag = True

        temp_a = dot(matrix, transpose([v_new]))

        for i in range(len(temp_a)):
            if not allclose(temp_a[i][0], v_new[i]*values[1]):
                flag = False
            
        if flag:
            break

        v = deepcopy(v_new)


    return v



matrix = [[-6, 3], [4, 5]]

qq, _ = qr_eigenvalues(matrix)

print(qq)

# vector = power_iteration(np.array(matrix), qq[1])

# print(vector.reshape(-1, 1))

# tt = []
# for i in range(len(matrix)):
#     temp = []
#     for j in range(len(matrix[0])):
#         if i == j:
#             temp += [matrix[i][j] + qq[i]]
#         else:
#             temp += [matrix[i][j]]
#     tt += [temp]

# print(dot(np.array(tt), vector.reshape(-1, 1)))


vals, vecs = np.linalg.eig(matrix)

print(power_iterative(matrix))