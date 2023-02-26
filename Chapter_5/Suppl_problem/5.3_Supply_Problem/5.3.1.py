class sort:
    def __init__(self,arr) -> None:
        self.arr = arr
    def exchange_sort(self): ## Also known as Bubble sort
        count = 0 # for number of exchanges
        for i in range(0,len(self.arr)-1):
            
            for j in range(0,len(self.arr)-1-i):
                
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j],self.arr[j+1] = self.arr[j+1] ,self.arr[j]
                    count +=1
        print("In Bubble sort the number of moves are {},".format(count))
        return self.arr
    def selection_sort(self):
        n = len(arr)
        count = 0
        
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                count += 1
        print("In Selection sort the number of moves are {},".format(count))
        return self.arr    
arr = [6,1,3,0,2,4,9,1,99,33,4,5,6,1,2,4,2,2,8,9,0,75,4,5]
s = sort(arr)
s.exchange_sort()
# s.selection_sort()                  

'''The Number of exchanges are more in exchange sort (BUBBLE SORT)  in comparsion with selection sort'''