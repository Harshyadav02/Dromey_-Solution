'''Given a randomly ordered array of n element ,partition the element into two subset 
such that elements <= x are in one subset and element > x are in the other subset

Condition:- 1. Don't use sort method 
            2. Ordering of sub-array is not required 
            3. syntex should be in below manner
                -----------------------------------------------------
               |  smaller element | pivoit element | larger element |
               ------------------------------------------------------
'''
def partarr(arr, x):
    i = 0
    j = len(arr)-1
    while (i < j):
        if arr[i] == x:
            
            arr.remove(arr[i])
            i = 0
            j = len(arr)-1
        elif arr[j] == x:
            
            arr.remove(arr[j])
            i = 0
            j = len(arr)-1
        if arr[i] > x:
            if arr[j] < x:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
            else:
                j -= 1
        else:
            i += 1

    y = 0
    while (x > arr[y]):
        y += 1
    else:
        arr.insert(y, x)

    return arr
arr = [2,1,3,8,4,1,0,8,4,7]
print(partarr(arr, 4))


