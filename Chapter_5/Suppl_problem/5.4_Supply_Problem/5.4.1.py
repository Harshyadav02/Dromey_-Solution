class sort:
    def __init__(self,arr) -> None:
        self.arr = arr
    def insertion_sort(self):
        count = 0
        for i in range(1,len(arr)):
            currnt = self.arr[i]
            prev = i-1
            # finding out the currnt position
            while( prev >= 0 and currnt < self.arr[prev]):
                self.arr[prev+1] = self.arr[prev]
                prev -= 1
                count +=1
            # insertion
            
            self.arr[prev+1] = currnt
            
        print("In insertion sort the number of moves are {},".format(count))

        return self.arr
    def selection_sort(self):
        n = len(arr)
        updates = 0
        
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                updates += 1
        print("In Selection sort the number of moves are {},".format(updates))
        return self.arr
        

arr = [6,1,3,0,2,4,9,1,99,33,4,5,6,1,2,4,2,2,8,9,0,75,4,5]
s = sort(arr)
# print(s.insertion_sort())
print(s.selection_sort())


''' 
    1) Number of swaps is more in insertion sort as compared to selection sort . 
   
    2) The choice between insertion sort and selection sort depends on the specific 
    characteristics of the input data. If the array is small or nearly sorted, 
    insertion sort is generally a good choice. If the array is large or very unsorted,
    selection sort may be a better choice. '''