# find the Maximum Number in an set
import math
def MaxNum(list):
    greatNum = -math.inf
    for i in range(0,len(list)):
        greatNum  = max(greatNum ,list[i])
    return greatNum
list = [0,8,9,-1,11]
print("The greatest Number is : ",MaxNum(list))
