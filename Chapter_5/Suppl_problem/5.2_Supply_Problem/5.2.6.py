class sort:
    def __init__(self) :
        pass
    def selection_sort(self,arr):
        n = len(arr)
        count_swap =0
        for i in range(0,len(arr)-1):
            
            min = i
            for j in range(i+1,len(arr)):
                if arr[min] > arr[j]:
                    min = j
                    count_swap +=1 
            arr[i] ,arr[min] = arr[min] , arr[i] #swaping
        if count_swap == 0 and count_swap == n*(n-1)/4:
            return True
        else:
            return False
   
arr= [1,2,3,4]
s = sort()
print(s.selection_sort(arr))


