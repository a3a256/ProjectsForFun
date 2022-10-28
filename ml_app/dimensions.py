def get_dimensions(n):
    mid = n//2
    mp = dict()
    for i in range(1, mid+1):
        if n%i == 0:
            a = n//i
            b = abs(a-i)
            if b not in mp:
                mp[b] = [a, i]
    return mp[min(mp.keys())]