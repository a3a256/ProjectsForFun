def build_tower(n, source, destination, auxiliary):
    if n == 0:
        return source+"-"+destination

    val = build_tower(n-1, source, auxiliary, destination) + " "
    val += source+"-"+destination
    val += " " + build_tower(n-1, auxiliary, destination, source)

    return val


def tower(a, b, c):
    struc = build_tower(len(a)-1, "a", "b", "c")
    vals = struc.split()
    for i in vals:
        g = i.split("-")
        if g[0] == "a" and g[1] == "b":
            b = [a.pop(0)] + b
            # print(a, b, c)
        elif g[0] == "a" and g[1] == "c":
            c = [a.pop(0)] + c
        elif g[0] == "b" and g[1] == "c":
            c = [b.pop(0)] + c
        elif g[0] == "b" and g[1] == "a":
            a = [b.pop(0)] + a
        elif g[0] == "c" and g[1] == "b":
            b = [c.pop(0)] + b
        elif g[0] == "c" and g[1] == "a":
            a = [c.pop(0)] + a

    return a, b, c

    



matrix = [1, 2, 3, 4, 5]

print(tower(matrix, [], []))