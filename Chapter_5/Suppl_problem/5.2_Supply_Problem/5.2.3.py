class sort:
    def __init__(self) :
        pass
    def selection_sort(self,arr):
        for i in range(0,len(arr)//2):
            min = i
            max = len(arr)-1-i
            if arr[min] > arr[max]:
                arr[min],arr[max] = arr[max],arr[min]
            for j in range(i+1,len(arr)-1-i):
                if arr[min] > arr[j]:
                    min = j
                elif arr[j] > arr[max]:
                    max = j
            arr[i] ,arr[min] = arr[min] , arr[i]
            arr[len(arr)-1-i] ,arr[max] = arr[max] , arr[len(arr)-1-i]
            
        return arr
arr= [-1,8,7,0,1,-5,-5]
s = sort()
print(s.selection_sort(arr))


