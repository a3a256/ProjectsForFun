from copy import deepcopy

one = [[4, 1], [1, 3]]
two = [[1], [2]]

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


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp += [matrix[j][i]]
        new_matrix += [temp]

    return new_matrix


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


    return x



print(conjugate(one, two))
