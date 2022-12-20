import numpy as np

matrix = [[40, -30, 60, -35], [-30, 300, -675, 420], [60, -675, 1620, -1050], [-35, 420, -1050, 700]]

def maxind(k, matrix):
    m = 0
    for i in range(1, len(matrix)):
        if matrix[k][i] > matrix[k][m]:
            m = i
    return m

def update(k, t, changed, state, value):
    y = value[k]
    value[k] = y + t
    if changed[k] and y == value[k]:
        changed[k] = False
        # print("check")
        state -= 1
    elif not changed[k] and y != value[k]:
        changed[k] = True
        state += 1
    return changed, state

def rotate(k, l, i, j, c, s, matrix):
    m = [[c, -s], [s, c]]
    s = [[matrix[k][l]], [matrix[i][j]]]
    result = []
    for i in range(len(m)):
        temp = []
        for p in range(len(s[0])):
            _sum = 0
            for k in range(len(m)):
                _sum += m[i][k]*s[k][p]
            temp += [_sum]
        result += [temp]

    return result[0][0], result[1][0]

def jacobi(matrix):
    vector = []
    eigenvals = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            if i == j:
                temp += [1]
            else:
                temp += [0]
        vector += [temp]
    state = len(matrix)

    indk = []
    changed = []
    for i in range(len(matrix)):
        indk += [maxind(i, matrix)]
        eigenvals += [matrix[i][i]]
        changed += [True]
    count = 0
    flag = True
    while flag:
        m = 0
        for i in range(len(matrix)):
            if(matrix[i][indk[i]] > matrix[m][indk[m]]):
                m = i
        k = m
        l = indk[m]
        p = matrix[k][l]
        y = (eigenvals[l]-eigenvals[k])/2
        d = abs(y)+np.sqrt(p**2 + y**2)
        r = (d**2+p**2)**(0.5)
        c = d/r
        s = p/r
        t = p**2/d
        if y > 0:
            s = -s
            t = -t
        matrix[k][l] = 0
        print(k, l)
        print(matrix)
        changed, state = update(k, -t, changed, state, eigenvals)
        changed, state = update(l, t, changed, state, eigenvals)
        for i in range(k-1):
            matrix[i][k], matrix[i][l] = rotate(i, k, i, l, c, s, matrix)
        for i in range(k+1, l-1):
            matrix[k][i], matrix[i][l] = rotate(k, i, i, l, c, s, matrix)
        for i in range(l+1, len(matrix)):
            matrix[k][i], matrix[l][i] = rotate(k, i, l, i, c, s, matrix)
        for i in range(len(matrix)):
            vector[i][k], vector[i][l] = rotate(i, k, i, l, c, s, vector)
        for i in range(len(matrix)):
            indk[i] = maxind(i, matrix)
        # print(eigenvals)
        enemy = False
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         if i != j:
        #             if matrix[i][j] != 0:
        #                 enemy = True
        # if not enemy:
        #     flag = False
        if count > 10:
            break
        count  += 1
    return vector, eigenvals

def isDiagonal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i != j:
                if arr[i][j] != 0:
                    return False
    return True

print(np.diagflat(np.diag(matrix)))
# print(jacobi(matrix))
print(isDiagonal([[1, 0, 0], [0, 2, 0], [0, 5, 3]]))
print(np.linalg.eig(matrix))