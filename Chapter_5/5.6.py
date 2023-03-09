'''This is Quick sort it takes same time complexity as merge sort i.e O(nlogn)
    But it doesn't take any kind of extra space 
    in worst case time complexity can go upto O(n**2)'''

class sort:
    def __init__(self) :
        pass
    def quick_sort(self,arr,start,last):
        if start < last:
            indx = self.partion(arr,start,last)
            self.quick_sort(arr,start,indx-1)
            self.quick_sort(arr,indx+1,last)
        return arr
    def partion(self,arr,start,last):
        pivot = arr[last]

        ''' This i will make space for the element which are smaller then the pivoit element '''
        i = start -1 
        for j in range(start,last):
            if arr[j] <=pivot:
                i +=1 
                arr[i],arr[j] = arr[j] ,arr[i] 
        arr[i+1], arr[last] = arr[last], arr[i+1]
        return i+1
array = [6,1,3,0,2,8,-1]
s = sort()

print(s.quick_sort(array, 0, len(array) - 1))  
