def secondSmall(list):
    sec_small = list[0]
    for i in range(1,max(list)-1):
        small = list[i]
        sec_small = max(sec_small,small)
    return  sec_small

list = [2,3,4,5,1]
list.sort()
print(secondSmall(list))