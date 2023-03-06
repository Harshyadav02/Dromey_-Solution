# find Smallest Common multiple of two numbers except one
# This is 3.3.7 and 3.3.8 question solution

value1,value2 = int(input("enter first number: ")),int(input("enter second number: "))
list1 = []
list2 = []
list3 = []
def smlldiv(x):
    global list1
    for i in range(2,x+1): ##  for one start range from 1 
        if(x%i == 0):
           list1.append(i) 
smlldiv(value1)
smlldiv(value2)

list1.sort()
# Checking Duplicate element
for i in range(0,len(list1)) :
  for j in range(i+1,len(list1)):
      if list1[i] == list1[j]:
        list2.append(list1[i])
  

if list2 :
  print("The Smallest common Multiple of  both the number is : ",list2[0])
else:
  # for prime number
  print("The Smallest common Multiple of  both the number is : ",1)
