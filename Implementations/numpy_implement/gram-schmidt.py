import numpy as np

def l2_norm_calculate(vector):
    return np.sqrt(sum([i**2 for i in vector]))

def elementwise(vector1, vector2):
    value = 0
    for i in range(len(vector1)):
        value += vector1[i]*vector2[i]
    return value

def construct_q_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp += [matrix[j][i]]
        new_matrix += [temp]

    return new_matrix

def construct_r_matrix(matrix, es):
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            if j < i:
                temp += [0]
            else:
                temp += [elementwise(matrix[j], es[i])]
        new_matrix += [temp]
    
    return new_matrix

def qr_decomposition(arr):
    e1 = [i/l2_norm_calculate(arr[0]) for i in arr[0]]
    en = [e1]
    for i in range(1, len(arr)):
        u_temp = arr[i]
        for j in en:
            multiplied_with_previous = elementwise(arr[i], j)
            temp_u = [k*multiplied_with_previous for k in j]
            for k in range(len(u_temp)):
                u_temp[k] -= temp_u[k]
        en += [[l/l2_norm_calculate(u_temp) for l in u_temp]]

    return construct_q_matrix(en), construct_r_matrix(arr, en)



matrix = [[3.2, 5.9, 8.1], [1.6, 2.54, 7.1], [4.4, 5.6, 1.4]]

q, r = np.linalg.qr(matrix)

print(" Q ", q)
print(" R ", r)

q, r = qr_decomposition(matrix)

print(" Q ")

for i in range(len(q)):
    for j in range(len(q)):
        print(q[i][j], end=" ")
    print()

print(" R ")

for i in range(len(r)):
    for j in range(len(r)):
        print(r[i][j], end = " ")
    print()
    