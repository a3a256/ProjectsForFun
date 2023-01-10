def eye(size):
    res = []
    if isinstance(size, tuple):
        for i in range(size[0]):
            temp = []
            for j in range(size[1]):
                if i == j:
                    temp += [1]
                else:
                    temp += [0]
            res += [temp]

        return res

    elif isinstance(size, int):
        for i in range(size):
            temp = []
            for j in range(size):
                if i == j:
                    temp += [1]
                else:
                    temp += [0]
            res += [temp]

        return res



def sign(arr):
    if isinstance(arr, int) or isinstance(arr, float):
        if arr == 0:
            return 0
        elif arr < 0:
            return -1
        else:
            return 1

    if isinstance(arr, list):
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] += [0]
            elif arr[i] < 0:
                arr[i] += [-1]
            else:
                arr[i] += [1]


    return arr



def norm(vector):
    _sum = 0
    for i in vector:
        _sum += i**2
    return _sum**(0.5)


def transpose(arr):
    res = []
    for i in range(len(arr[0])):
        temp = []
        for j in range(len(arr)):
            temp += [arr[j][i]]
        res += [temp]

    return res


def mult(arr1, arr2):
    print(len(arr1))
    print(len(arr2))
    ans = []
    for i in range(len(arr1)):
        t = []
        for j in range(len(arr2[0])):
            value = 0
            for k in range(len(arr1[0])):
                print(k)
                value += arr1[i][k]*arr2[k][j]
            t.append(value)
        ans.append(t)
    return ans




def decompose(arr):
    q = eye(len(arr))
    r = arr



    for j in range(len(arr[0])):
        to_norm = []
        for i in range(j, len(r[0])):
            to_norm += [r[i][j]]

        normx = norm(to_norm)

        s = -sign(r[j][j])

        u1 = r[j][j] - s*normx

        w = [i/u1 for i in to_norm]

        w[0] = 1

        tau = -s*u1/normx

        for k in range(len(w)):
            w[k] *= tau

        t = 0
        v = mult([w], transpose([w]))[0][0]
        for k in range(len(to_norm)):
            to_norm[k] *= v


        for k in range(j, len(r[0])):
            r[i][j] -= to_norm[t]
            t += 1

        q_change = []
        for z in range(len(q)):
            temper = []
            for k in range(j, len(q[0])):
                temper += [q[z][k]]
            q_change += [temper]
        q_t = [tu*tau for tu in w]
        print(transpose([w]))
        print(mult(q_change, transpose([w])))

        h_q = mult(transpose(mult(q_change, transpose([w]))), transpose([q_t]))
        print(h_q)
        # for z in range(len(q)):
        #     for k in range(j, len(q[0])):
        #         q[z][k] 

    print(r)
        



import numpy as np

print(np.linalg.norm([1,2,3,4,5]))

print(norm([1,2,3,4,5]))

decompose([[1,2,3], [4,5,6], [7,8,9]])
