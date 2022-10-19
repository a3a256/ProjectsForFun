
def insertion_sort(arr):
    length = len(arr)
    i = 1
    while i<length:
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        i += 1
    return arr

def sort(arr): #insertion sort by myself no correct version from internet
    length = len(arr)
    for i in range(1, length):
        if arr[i] < arr[i-1]:
            j = i-1
            while arr[j] > arr[i] and j >= 0:
                j -= 1
            if j == 0:
                a = arr.pop(0)
                arr = [a] + arr
            else:
                j += 1
                a = arr.pop(i)
                arr = arr[:j] + [a] + arr[j:]
    return arr


print(sort([8,3,1,11,5,6,4,5]))
print(insertion_sort([8,3,1,11,5,6,4,5]))
