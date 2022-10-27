def get_nums(n):
    mid = n//2
    mp = dict()
    for i in range(1, mid):
        if n%i == 0:
            a = n//i
            b = abs(a-i)
            mp[b] = [i, a]
    return mp[min(mp.keys())]


print(get_nums(24456))