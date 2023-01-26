'''Implement the list (array) reversal algo ,where start = 0 and 
Last = len(list)-1 ,with each iteration start is incresed and last is decresed  for start < last '''

def reverseList(list):
    start = 0
    last = len(list) -1
    while(start < last):
        temp = list[start]
        list[start] = list[last]
        list[last] = temp
        start += 1
        last -= 1
    return list
list = [1,2,3,4,5,6,7,8,9,10]
print("List before reversing: ",list)
print("List after reversing: ",reverseList(list))


