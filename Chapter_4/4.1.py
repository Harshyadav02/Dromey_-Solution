def reverseList(list):
    # r is Number of swap required  
    r = int(len(list)/2)
    
    for i in range(0,r): # Here the time complexity will be O(n/2)
        temp =  list[i]
        list[i] = list[len(list)-1-i] 
        list[len(list)-1-i] = temp
    return list
list = [1,2,3]
print("List before reversing: ",list)
print("List After reversing: ",reverseList(list))

