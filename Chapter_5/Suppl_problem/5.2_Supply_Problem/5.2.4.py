class sort:
    def __init__(self) :
        pass
    def selection_sort(self,arr):
        count_random =0
        for i in range(0,len(arr)-1):
            
            min = i
            for j in range(i+1,len(arr)):
                if arr[min] > arr[j]:
                    min = j
                    count_random +=1 
            arr[i] ,arr[min] = arr[min] , arr[i] #swaping
        return arr,count_random
   
arr= [6,5,4,3,2,1]
s = sort()
print("The sorted array  and the updations are ",s.selection_sort(arr))


