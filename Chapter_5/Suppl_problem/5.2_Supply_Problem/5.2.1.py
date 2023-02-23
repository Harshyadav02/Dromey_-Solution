''' sort the array into desinding order'''
class sort:
    def __init__(self) :
        pass
    def selection_sort(self,arr):
        for i in range(0,len(arr)-1):
            min = i
            for j in range(i+1,len(arr)):
                if arr[min] < arr[j]:
                    min = j
            arr[i] ,arr[min] = arr[min] , arr[i] #swaping
        return arr
arr= [-1,8,7,0,1]
s = sort()
print(s.selection_sort(arr))


