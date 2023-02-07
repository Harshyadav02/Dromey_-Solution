def kth_Smallele(arr,k):
    arr.sort()
    count = 0
    i = 0
    while(count != k-1):
        if  count == len(arr)-1:
            print("the last indexed element is the kth smallest element so,")
            break
        if arr[i] < arr[i+1]:
            count +=1
            i +=1
    return arr[i]
arr = [1,100,200,2,3,5,8]
print("The kth smallest element is: ",kth_Smallele(arr,100))