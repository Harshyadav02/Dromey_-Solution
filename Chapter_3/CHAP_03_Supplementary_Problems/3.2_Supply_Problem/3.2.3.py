#### Find biggest divisor of the given positve integer

list = [] ## empty list
range1 = int(input("enter the range : "))
# value = int(input("Enter the value Whose smallest Divisor is Required "))
for i in range(0,range1):
    i = int(input("Enter the value: "))
    list.append(i)
def smlldiv(x):
   for jis in range(0,len(list)-1):
        if(list[i] % j == 0):
           list.append(i) 

smlldiv(value)  
list.sort()      
print("Exact biggest Divisor of the given value is :",list[-1])## minius 1 return the last index 