def partarr(arr, x):
    i = 0
    j = len(arr)-1
    while (i < j):
        if arr[i] <= x:
            i =+ 1
        elif arr[j] > x:
            j =-1
        else:
            arr[i] ,arr[j] = arr[j],arr[i]
            i +=1
            j -=1
            
    return arr
arr = [15,12,19,11,8,4,5]
print(partarr(arr,5))