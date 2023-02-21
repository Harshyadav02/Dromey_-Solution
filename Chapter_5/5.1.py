class sort:
    def __init__(self) :
        pass
    def merge(self,left,right):
        i = 0
        j = 0
        
        temp = []
        while(i <=len(left)-1 and j <= len(right)-1):
            if left[i] <= right[j]:
                temp.append(left[i])
                i =+1
                
            else:
                temp.append(right[j])
                j =+1
                
        temp += left[i:]
        temp += right[j:]
        return temp
    def findmid(self,arr):
        
        if (len(arr) <= 1):
            return arr
        else:    
            
            mid = int(len(arr)/2)
            left = self.findmid(arr[:mid])
            right = self.findmid(arr[mid:])
            result = self.merge(left,right)
        return result
arr= [1,2,-1]
s = sort()
print(s.findmid(arr))

    

