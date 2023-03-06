# find the Number of times the maximum element occur in an array of n element .
# Note:- only one pass through the array should be done

def MaxOccur(list):
    MaxEle = list[0]
    for i in range(1, len(list)):
        MaxEle = max(MaxEle, list[i])  # Finding maximum element
    return list.count(MaxEle)


list = [1, 2, 5, 5, 5, 6, 2, 3, 5, 6]
print("The Number of Occurance of the Maximum Element is : ", MaxOccur(list))
