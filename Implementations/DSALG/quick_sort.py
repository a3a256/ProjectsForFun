def sort(left, right, pivot):
    return left + [pivot] + right

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    r = []
    l = []
    pivot = arr.pop()
    for i in arr:
        if i > pivot:
            r += [i]
        else:
            l += [i]
    return sort(quickSort(l), quickSort(r), pivot)


arr = [9, 6, 2, 9, 1]

print(quickSort(arr))