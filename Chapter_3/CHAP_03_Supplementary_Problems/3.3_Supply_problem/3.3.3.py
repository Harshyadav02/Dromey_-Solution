#### Find the Greatest Common Divisor Of two Interger
list = [] 
choice = int(input("Enter the  number of choice "))
for i in range(0,choice):
    value = int(input("Enter the   value : "))
    list.append(value)
list.sort()
print(list)
def gcd(list):
    
    rem = list[1]%list[0]
    for j in range(1,len(list)-1):
        if rem  == 0:
           rem = list[i+1]%list[0]
        else:    
            while(rem!=0):
                list[j] = list[i]
                list[i] = rem
                rem = list[j]%list[i]
                    
    return  list[i]
ans = gcd(list)
print("The Greatest Common Divisor Of Given two Interger is {}".format(ans))
print(list)