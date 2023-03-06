def findIndex(x ,list):
    start = 0
    end = len(list)-1
    while(start <= end):
        mid = int((start + end)/2)
        if x == list[mid]:
            return mid
        if x > list[mid]:
            start = mid + 1
        else: 
            end = mid -1
    return -1  # -1 represent that Number doesn't exist

list = [1,2,3,4,5]
print("The postion of give number is : ",findIndex(-1,list))
