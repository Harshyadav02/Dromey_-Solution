#### Find the Greatest Common Divisor Of two Interger 

value1 = int(input("Enter the  greater value : "))
value2 = int(input("Enter the  Smaller value : "))

def gcd(x,y):
    rem = x%y
    if rem  == 0:
        return y
    else:    
        while(rem!=0):
            x = y
            y = rem
            rem = x%y
    return  y
ans = gcd(value1,value2)
print("The Greatest Common Divisor Of Given two Interger is {}".format(ans))