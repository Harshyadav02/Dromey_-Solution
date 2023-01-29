def absDifference(list):
   
    abs_diff = abs(list[1]-list[0])
    for i in range(2,len(list)-1):
        diff = abs(list[i]-list[i+1])
        abs_diff = max(abs_diff,diff)
        
    print("The maximum absolute difference B/W two element is : ",abs_diff)
     

list = [6,1,2,3,4,0]
absDifference(list)