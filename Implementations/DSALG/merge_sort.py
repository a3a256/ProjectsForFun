def merge(left, right):
    i = 0
    j = 0
    res = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            res += [left[i]]
            i += 1
        else:
            res += [right[j]]
            j += 1

    if j < len(right):
        res += right[i:]
    if i < len(left):
        res += left[i:]

    return res


def mergeSort(arr):
    if len(arr)==1:
        return arr


    middle = len(arr)//2

    return merge(mergeSort(arr[:middle]), mergeSort(arr[middle:]))


m = [9, 6, 2, 9, 1]
print(mergeSort(m))