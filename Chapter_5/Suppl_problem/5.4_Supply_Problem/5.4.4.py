class sort:
    def __init__(self,arr) -> None:
        self.arr = arr
    def insertion_sort_binary(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            left = 0
            right = i - 1
            
            while left <= right:
                mid = (left + right) // 2
                if self.arr[mid] < key:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            for j in range(i - 1, left - 1, -1):
                self.arr[j + 1] = self.arr[j]
                
            self.arr[left] = key

        return self.arr
arr = [6,1,0,3,2]
s = sort(arr)
print(s.insertion_sort_binary())