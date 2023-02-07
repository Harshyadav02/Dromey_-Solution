'''Given a randomly ordered array of n element ,partition the element into two subset 
such that elements <= x are in one subset and element > x are in the other subset

Condition:- 1. Don't use sort method 
            2. Ordered sub-array is not required 
'''
def partarr(arr,x):
    i = 0
    j = len(arr)-1
    while(i < j):
        
        if arr[i] > x:
            if arr[j] <= x:
                arr[i] ,arr[j] = arr[j] ,arr[i]
                j -=1
            else:
                j -=1
        else:
            i += 1
    return arr
arr = [200,-1,300,100,250,150,400,0,900,1000,201]
print(partarr(arr,200))

''' Note :- This code not full code. The pivoit element didn't 
    come in the middle where we can diffenciate b/w elements '''