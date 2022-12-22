### Produce a list of all exact divisior of given positive Integer

list = [] ## empty list
value = int(input("Enter the value Whose smallest Divisor is Required "))

def smlldiv(x):
   for i in range(2,x+1):
        if(x%i == 0):
           list.append(i) 

smlldiv(value)        
print("All exact divisor of the given value are :",list)