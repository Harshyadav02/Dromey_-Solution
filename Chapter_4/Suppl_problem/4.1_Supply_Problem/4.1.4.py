def EvenOddSuff(list):
    for i in list:
        if i%2 != 0:
            list1.append(i)
        else:
            list2.append(i)
    
list1 = [] # this list for odd
list2 = [] # this list for even 
list = [1,2,3,4,5,6,7,8,2,2,6,9,9,9,9]
EvenOddSuff(list)
list1.extend(list2) # Extending one list to another
print(list1)