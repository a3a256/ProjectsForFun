class Search:
    def __init__(self, array, target):
        self.target = target
        self.array = array

    def iterative_searching(self):
        arr = self.array
        right = 0
        left = len(arr) - 1
        mid = 0
        while right <= left:
            mid = (right+left)//2
            if arr[mid] == self.target:
                return mid

            if arr[mid] < self.target:
                right = mid+1

            if arr[mid] > self.target:
                left = mid - 1

        return -1

    def recursive_searching(self, arr, left, right, target):
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return self.recursive_searching(arr, mid+1, right, target)
        if arr[mid] > target:
            return self.recursive_searching(arr, left, mid-1, target)
        return -1

    
def main():
    arr = [1, 4, 5, 7, 9, 13, 17]
    s = Search(arr, 5)
    print(s.iterative_searching())
    print(s.recursive_searching(arr, 0, len(arr), 5))


if __name__ == '__main__':
    main()
