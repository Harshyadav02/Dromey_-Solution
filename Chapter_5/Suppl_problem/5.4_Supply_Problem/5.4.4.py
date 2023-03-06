class sort:
    def __init__(self,arr) -> None:
        self.arr = arr
    def insertion_sort_binary(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            left = 0
            right = i - 1
            # Finding the element to insert it into its Right Postion
            while left <= right:
                mid = (left + right) // 2
                if self.arr[mid] < key:
                    left = mid + 1
                else:
                    right = mid - 1
            # Shifting the element to make the space         
            for j in range(i - 1, left - 1, -1):
                self.arr[j + 1] = self.arr[j]
            # Placing the Element into its right Position    
            self.arr[left] = key

        return self.arr
arr = [5,4,3,2,1]
s = sort(arr)
print(s.insertion_sort_binary())