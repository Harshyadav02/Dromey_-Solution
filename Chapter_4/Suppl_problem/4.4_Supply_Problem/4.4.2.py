# Remove from an ordered list all numbers that occurs more than k times.

def removeElem(list,k):
    list1 =[]
    for i in range(0,len(list)):
        
        if list.count(list[i]) <= k  :
            list1.append(list[i])
    list.clear()
    list.append(list1)
    del list1    
    return list

list = [1,2,3,3,4,5,5,5]

print("List after removing all the elements that occurs more than K times : ",removeElem(list,2))

