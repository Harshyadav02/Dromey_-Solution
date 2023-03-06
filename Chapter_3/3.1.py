### Finding the square root root of an number

def squareroot(m):
	error = float((input("Enter the desired error: ")))
	g2=m/2
	g1=m/g2
    
    
	while abs(g1-g2) >error:
		
		g1=g2
		g2=float((g1+(m/g2)))/2	
	return g2
value = int(input("enter the desired value: "))
print(squareroot(value))
