''' Bubble_sort design which incorporates exchages in reverse direction '''
class sort:
    def __init__(self,arr) -> None:
        self.arr = arr
    def bubble_sort(self):
        for i in range(0,len(self.arr)-1):
            for j in range(0,len(self.arr)-1-i):
                if self.arr[j] < self.arr[j+1]:
                    self.arr[j],self.arr[j+1] = self.arr[j+1] ,self.arr[j]
        return self.arr
arr = [5,1,9,3,2,-1]
s = sort(arr)
print(s.bubble_sort())
