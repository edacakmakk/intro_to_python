"""
Have the function LargestPair(num) take the num parameter being passed and 
determine the largest double digit number within the whole number. For example: 
if num is 4759472 then your program 
should return 94 because that is the largest double digit 
number. The input will always contain at least two positive digits.
"""

def LargestPair(num):
    x=0
    for i in range(len(str(num)))[:len(str(num))-1]:
      if int(str(num)[i] + str(num)[i + 1]) > x:
          x=int(str(num)[i]+str(num)[i+1])
    return x 


print (LargestPair(int(input())))