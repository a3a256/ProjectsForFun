def permutations(lis):
    if len(lis) == 1:
        return [lis]

    output = []
    *front, last = lis
    
    for perm in permutations(front):
        print(perm)
        print("Step")
        for i in range(len(perm) + 1):
            print(i)
            new = perm[:i] + [last] + perm[i:]
            output.append(new)

    return sorted(output)


lst = [1,2,3]
for perm in permutations(lst):
    print(perm)