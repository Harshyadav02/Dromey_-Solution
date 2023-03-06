list = [] ## empty list
#value = int(input("Enter the value Whose smallest Divisor is Required "))

def smlldiv():
    
    for Number in range(1,101):
        # count = 0
        for i in range(2, Number + 1):
            
            if(Number%i == 0):
                list.append(Number)   
                    
'''def con(x):
        count = 0
        for j in range(0,len(list)-1):
            if x[j] == x[j+1]:
                count += 1 
        list.append(count)       '''          
                
                
smlldiv()
# con(list)  
# list.sort()  
print(list)
#print("Exact biggest Divisor of the given value is :",list[-1])## minius 1 return the last index 