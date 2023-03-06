# find the Maximum Number in an set
import math
def MaxNum(list):
    greatNum = list[0]
    for i in range(1,len(list)):
        greatNum  = max(greatNum ,list[i])
    return greatNum
list = [0,8,9,-1,11]
print("The greatest Number is : ",MaxNum(list))
