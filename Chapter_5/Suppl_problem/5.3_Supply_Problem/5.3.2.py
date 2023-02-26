''' Another version of bubble sort '''

class sort:
    def __init__(self,arr) :
        self.arr = arr
    def bubble_sort(self):
        
        for i in range(0,len(self.arr)-1):
           for j in range(i+1,len(arr)):
               if self.arr[i] > self.arr[j]:
                   self.arr[i] ,self.arr[j] = self.arr[j] ,self.arr[i]
                   
        return self.arr
    
arr = [5,1,9,3,2,-1]
s = sort(arr)
print(s.bubble_sort())