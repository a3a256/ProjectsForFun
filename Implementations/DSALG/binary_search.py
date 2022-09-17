class Search:
    def __init__(self, array, target):
        self.target = target
        self.array = array

    def searching(self):
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

    
def main():
    arr = [1, 4, 5, 7, 9, 13, 17]
    s = Search(arr, 5)
    print(s.searching())


if __name__ == '__main__':
    main()