'''Given a randomly ordered array of n element ,partition the element into two subset 
such that elements <= x are in one subset and element > x are in the other subset

Condition:- 1. Don't use sort method 
            2. Ordered sub-array is not required 
'''
def partarr(arr,x):
    i = 0
    j = len(arr)-1
    while(i < j):
        if arr[i] == x:
            temp = arr[i]
            arr.remove(arr[i])
            print(arr)
            i = 0
            j = len(arr)-1
        if arr[i] > x:
            if arr[j] < x:
                arr[i] ,arr[j] = arr[j] ,arr[i]
                j -=1
            else:
                j -=1
        else:
            i += 1
    x = int(len(arr)-1 /2)
    arr.insert(x,temp)
    return arr
arr = [200,1,2,7,3,9,2,100,300,400,800,750]
print(partarr(arr,200))

''' Note :- This code not full code. The pivoit element didn't 
    come in the middle where we can diffenciate b/w elements '''