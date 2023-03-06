# find all common prime divisor of two Number
value1,value2 = int(input("enter first number: ")),int(input("enter second number: "))
list1 = []
list2 = []
list3 = []
def smlldiv(x):
    global list1
    for i in range(1,x+1):
        if(x%i == 0):
           list1.append(i) 



smlldiv(value1)
smlldiv(value2)

list1.sort()

# Reaptation of Number
for i in range(0,len(list1)) :
  for j in range(i+1,len(list1)):
      if list1[i] == list1[j]:
        list2.append(list1[i])

# prime number
for i in list2:
    for j in range(2,(i)):
        if i %j == 0:
            break
        
    else:
        list3.append(i)
print("The common prime Number B/w both the number are : ",list3)
