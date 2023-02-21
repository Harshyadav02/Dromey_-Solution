def merge(left,right):
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
def findmid(arr):
    

    if (len(arr) <= 1):
        return arr
    
    else:    
        
        mid = int(len(arr)/2)
        left = findmid(arr[:mid])
        right = findmid(arr[mid:])
        result = merge(left,right)
    return result
arr = [1,2,3,-1,0,5,3,-2]
print(findmid(arr))

    

