def permutations(lis):
    if len(lis) == 1:
        return [lis]

    output = []
    *front, last = lis
    
    for perm in permutations(front):
        for i in range(len(perm) + 1):
            new = perm[:i] + [last] + perm[i:]
            output.append(new)

    return sorted(output)

lst = [1, 2, 3, 4]
n = 2
arr = []
for i in range(len(lst)):
    q = [lst[i]]
    for j in range(len(lst)):
        if i != j:
            q.append(lst[j])
            c = q.copy()
            if c not in arr:
                if len(c) < len(lst):
                    arr.append(c)
print(arr)

for perm in permutations(lst):
    pass
    # print(perm)
