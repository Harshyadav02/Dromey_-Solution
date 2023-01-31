# Remove the duplicate element form an orderd array
def removeDupli(list):
    i = 0
    while i < len(list) - 1:
        if list[i] == list[i+1]:
            list.remove(list[i])
        else:
            i += 1
    return list

list = [1,1,3,3,3,3,3,3,3,5,5,5,5,5,5,6,6,6,6,8,8,8,8]
print(removeDupli(list))
   


