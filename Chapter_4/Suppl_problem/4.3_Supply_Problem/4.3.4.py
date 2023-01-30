def absDifference(list):
   
    abs_diff = 0
    for i in range(0,len(list)):
        if i == len(list)-1:
            break
        else:
            diff = abs(list[i]-list[i+1])
            abs_diff = max(abs_diff,diff)
        
    print("The maximum absolute difference B/W two element is : ",abs_diff)
     

list = [6,1,2,3]
absDifference(list)