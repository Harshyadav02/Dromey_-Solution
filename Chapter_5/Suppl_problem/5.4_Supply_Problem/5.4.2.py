class sort:
    def __init__(self,arr) -> None:
        self.arr = arr
    def insertion_sort(self):
        for i in range(1, len(self.arr)-1):
            currnt  = self.arr[i]
            prev = i-1
            nextele = self.arr[i+1]
            next = i+1
            if self.arr[next] < currnt:
                    arr[next] = self.arr[prev+1]  
                    self.arr[next-1] = nextele
                    next -=i 
            while(prev >=0 and currnt < self.arr[prev]):
                self.arr[prev+1] = self.arr[prev]
               
                prev -=1
            self.arr[prev+1] = currnt
            
        return self.arr
arr = [6,1,3,0,2]
s = sort(arr)
print(s.insertion_sort())
            