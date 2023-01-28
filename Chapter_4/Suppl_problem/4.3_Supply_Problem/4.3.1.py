# Find the minimum element in an array 

def MinElem(list):
    MinNum = list[0]
    for i in range(1,len(list)):
        MinNum = min(MinNum,list[i])
    return MinNum

list = [1,-2,2,3,-1,4,5,6]
print("The minimum element in given Array is : ",MinElem(list))