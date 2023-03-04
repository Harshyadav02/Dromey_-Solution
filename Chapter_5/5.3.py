class sort:
    def __init__(self) -> None:
        pass
    def exchange_sort(self,arr):
        for i in range(0,len(arr)-1):
            for j in range(0,len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1] ,arr[j]
        return arr
arr = [5,4,3,2,1,-1,108]
s = sort()
print(s.exchange_sort(arr))                
