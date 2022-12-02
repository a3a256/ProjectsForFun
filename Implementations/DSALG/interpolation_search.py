def search(arr, lo, hi, target):
    if lo == hi:
        if arr[lo] == target:
            return lo
        else:
            return -1
    mid = lo + (target - arr[lo]) * (hi - lo)//(arr[hi] - arr[lo])
    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return search(arr, lo, mid-1, target)
    
    elif arr[mid] < target:
        return search(arr, mid+1, hi, target)


arr = [1, 4, 6, 8, 9, 12, 16]

print(search(arr, 0, len(arr)-1, 9))