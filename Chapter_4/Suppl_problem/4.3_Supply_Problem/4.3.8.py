def MinElem(list):
    MinNum = list[0]
    for i in range(1,len(list)):
        MinNum = min(MinNum,list[i])
    return list.count(MinNum)

def MaxOccur(list):
    MaxEle = list[0]
    for i in range(1, len(list)):
        MaxEle = max(MaxEle, list[i])  # Finding maximum element
    return list.count(MaxEle)

list = [1,1,1,2,2,6,6,7,8,8]
print("The minimum element Occarance in Array is : ",MinElem(list))
print("The Maximum element Occarance in Array is : ",MaxOccur(list))