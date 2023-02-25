class sort:
    def __init__(self) :
        pass
    def selection_sort(self,arr):
        
        for i in range(0,len(arr)-1):
            min = i
            for j in range(i+1,len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i] ,arr[min] = arr[min] , arr[i] # swaping
            for k in range(i +1,len(arr)):
                if arr[k] == arr[i]:
                    arr.pop(k) # k is the index not the element
        return arr

arr= [1,5,5,2,0]
s = sort()
print(s.selection_sort(arr))


