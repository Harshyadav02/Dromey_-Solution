''' Find the  kth Smallest element form the given list '''
def kth_Smallele(arr,k):
    arr.sort()
    count = 0
    i = 0
    while(count != k-1):
        if  count == len(arr)-1:
            print(" No other element is present in the list therefore,",end="")
            break
        elif k >0:
            if arr[i] < arr[i+1]:
                count +=1
                i +=1
        else:
            print("Negative kth element cannot be found ")
            return -1
            
    return arr[i]
arr = [1,100,200,2,3,5,8]
print("The kth smallest element is: ",kth_Smallele(arr,8))