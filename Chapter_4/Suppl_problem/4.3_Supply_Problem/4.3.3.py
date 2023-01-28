''' Find the maximum in an set and the position
    (a) Where it first occurs
    (b) Where it last  occurs  '''


def MaxOccur(list):
    MaxEle = list[0]
    firstOcc = 0
    lastOcc = 0
    for i in range(1, len(list)):
        if MaxEle < list[i]:
            MaxEle = list[i]
            # For first Occurance
            firstOcc = i 
        
        # For last Occurance
        if MaxEle == list[i]:
            lastOcc = i
    print("The First Ocuurance of maximum is : ",firstOcc)
    print("The Last  Ocuurance of maximum is : ",lastOcc)
    return MaxEle


list = [5,1,2,3,4,5]
print("The  Maximum Element is : ", MaxOccur(list))
