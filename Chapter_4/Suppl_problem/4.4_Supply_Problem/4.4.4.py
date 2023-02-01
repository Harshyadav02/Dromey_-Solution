def sorting(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-1-i):# -i because in each etration one element will be at correct position
            if list[j]  > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return(list)
list = [1,1,5,6,3,3,2,0,9,0]
print("List after sorting is : ",sorting(list))