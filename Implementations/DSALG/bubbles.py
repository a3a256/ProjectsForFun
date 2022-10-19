def bubble_sort(arr):
    swapped = False
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return

arr = [8,3,1,11,5,6,4,5]

bubble_sort(arr)

print(arr)