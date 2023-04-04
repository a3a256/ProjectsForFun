import numpy as np
from copy import deepcopy

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

def is_triangular(arr):
    arr = aproximate(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if j < i:
                if arr[i][j] != 0:
                    return False
    return True

def out_matrix(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

def diag(matrix):
    vector = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                vector += [matrix[i][j]]

    return vector

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

def transpose(matrix):
    arr = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp += [matrix[j][i]]
        arr += [temp]

    return arr


def dot(one, two):
    new_matrix = []
    for i in range(len(one)):
        temp = []
        for j in range(len(two[0])):
            value = 0
            for k in range(len(one[0])):
                # print(type(two[k][j]))
                value += one[i][k]*two[k][j]
            temp += [value]

        new_matrix += [temp]

    return new_matrix


def determinant1(matrix):
    if len(matrix) == 1:
        print(matrix)
        print()
        return matrix[0][0]


    det = 0

    coef = -1
    for i in range(len(matrix)):
        new_ = []
        for j in range(1, len(matrix)):
            temp = []
            for k in range(len(matrix[0])):
                if k != i:
                    temp += [matrix[j][k]]
            new_ += [temp]
        out_matrix(new_)
        print()
        det += matrix[0][i]*coef**(i+1)*determinant(new_)

    return det

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


def matrix_equations(matrix, answers):
    matrix.pop()
    answers.pop()

    arguments = [1]

    for i in range(len(matrix)):
        answers[i] = matrix[i].pop(0)
        answers[i] = answers[i]*(-1)

    orig_det = deepcopy(determinant(matrix))

    temp = []

    for i in range(len(matrix)):
        temp = deepcopy(matrix)
        for j in range(len(matrix)):
            temp[j][i] = answers[j]

        arguments += [determinant(temp)/orig_det]

    return arguments


def cofactor_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            temp_matrix = []
            for k in range(len(matrix)):
                if k != i:
                    temp_row = []
                    for l in range(len(matrix[0])):
                        if l != j:
                            temp_row = [matrix[k][l]]
                    temp_matrix += [temp_row]
            out_matrix(temp_matrix)
            print("Check, flag")
            temp += [determinant(temp_matrix)]
        new_matrix += [temp]

    return new_matrix


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



def inverse(matrix):
    det = determinant(matrix)
    cofactor = transpose(find_cofactor(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            cofactor[i][j] /= det


    return cofactor


def l2_norm(vector):
    return np.sqrt(sum([i**2 for i in vector]))


def qr(matrix):
    length = len(matrix)
    common_length = len(matrix)
    es = []
    r = deepcopy(matrix)
    for i in range(len(matrix)):
        e = eye(length)
        sliced_matrix = []
        for j in range(i, len(matrix)):
            temp = []
            for k in range(j, len(matrix)):
                temp += [r[i][j]]
            sliced_matrix += [temp]
        a = [matrix[k][i] for k in range(len(matrix))]
        l2 = l2_norm(a)


        v = [sliced_matrix[k][0] + l2*e[k][0] if r[i][i] >= 0 else sliced_matrix[k][0] - l2*e[k][0] for k in range(len(e))]
        upper = dot(transpose([v]), [v])
        lower = dot([v], transpose([v]))[0][0]
        for k in range(len(upper)):
            for j in range(len(upper)):
                e[k][j] -= 2*(upper[k][j]/lower)


        si = 0
        ref_e = eye(common_length)
        for j in range(common_length):
            sj = 0
            for k in range(common_length):
                if j >= i:
                    if k >= i:
                        ref_e[j][k] = e[si][sj]
                        sj += 1
            if j >= i:
                si += 1
        
        cop = dot(ref_e, r)
        r = deepcopy(cop)
        es += [deepcopy(ref_e)]
        length -= 1

    q = deepcopy(es[0])
    for i in es[1:]:
        q = dot(q, i)

    return q, r



def eigenvalues(matrix, iter=500):
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


        for i in range(len(temp_a)):
            for j in range(len(temp_a)):
                temp_a[i][j] -= shift[i][j]

        q, r = qr(temp_a)

        reverse = dot(r, q)

        for i in range(len(ak)):
            for j in range(len(ak)):
                ak[i][j] = reverse[i][j] + shift[i][j]

        qq = dot(qq, q)

        if is_triangular(ak):
            print(iter)
            break

    return diag(ak)


def qr_algorithm(matrix, iter=5000):
    # qq, _ = house_holder_reflections(deepcopy(matrix))
    qq = eye(len(matrix))
    ak = deepcopy(matrix)
    save = []
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

        q, r = qr(temp_a)
        reverse = dot(r, q)
        for i in range(len(ak)):
            for j in range(len(ak[0])):
                ak[i][j] = reverse[i][j] + shift[i][j]

        qq = dot(qq, q)
        save += [deepcopy(q)]

        if is_triangular(deepcopy(ak)):
            break

    # end = save[0]

    # for i in save[1:]:
    #     end = dot(end, i)


    return ak, qq



def eigenvector(matrix, iter=10):
    values = eigenvalues(matrix)
    vectors = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            temp += [1]
        vectors += [temp]

    
    for i in range(len(values)):
        for _ in range(iter):
            iden = eye(len(matrix))
            first = []
            for j in range(len(matrix)):
                temp = []
                for k in range(len(matrix)):
                    temp += [matrix[j][k] - values[i]*iden[j][k]]
                first += [temp]
            vector = [vectors[i][k] for k in range(len(matrix))]
            inv = inverse(first)
            upper = dot(inv, transpose([vector]))
            vals = [upper[k][0] for k in range(len(matrix))]
            lower = l2_norm(vals)
            for k in range(len(upper)):
                for j in range(len(upper[0])):
                    vectors[k][i] = upper[k][j]/lower

    

    return vectors


def vectors(matrix):
    values = eigenvalues(matrix)
    vecs = []
    count = 1
    single = []
    for i in values:
        temp_matrix = deepcopy(matrix)
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if j == k:
                    temp_matrix[j][k] -= i
        single = matrix_equations(temp_matrix, [0]*len(matrix))
        if count == 1:
            for j in range(len(single)):
                single[j] *= -1
            count += 1
        vecs += [single]

    for i in range(len(vecs)):
        d = l2_norm(vecs[i])
        for j in range(len(vecs)):
            vecs[i][j] = vecs[i][j]/d

    return vecs






# matrix = [[1.2, 3.1, 6.7, 7.7], [5.3, 6.6, 1.9, 2.2], [4.5, 7.2, 8.9, 6.6], [3.7, 8.1, 9, 1]]

# q, r = qr(matrix)

# out_matrix(q)

# q, r = np.linalg.qr(matrix)

# print(q)

# v, _ = qr_algorithm(matrix)

# print(diag(v))

# vectors_implemented = eigenvector(matrix)

# vals, vectors_real = np.linalg.eig(matrix)

# print(vals)

# print("***Implemented***")

# out_matrix(vectors_implemented)

# print()

# print("***Real***")

# out_matrix(vectors_real)

matrix = [[-16, -28, -19], [42, 69, 46], [-42, -72, -49]]

a = eigenvalues(matrix)

print("Implemented eigvalues\n", a)

vvs = vectors(matrix)

print("Implemented eigvectors\n")

out_matrix(transpose(vvs))

a, r = np.linalg.eig(matrix)

print("Real eigvalues using numpy\n", a)

print("Real eigvectors using numpy\n", r)


pp = [[-21, -28, -19], [42, 64, 46], [-42, -72, -53]]

print(matrix_equations(pp, [0, 0, 0]))

print(matrix_equations([[1, 4], [-4, -7]], [0, 0]))

print(np.linalg.eig([[0, 1], [-2, -3]]))
