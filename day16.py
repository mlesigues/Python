#TASK: Power of Four from Leetcode!
import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        #we're only checking if a given integer is power of 4
        #src:https://www.geeksforgeeks.org/check-if-a-number-is-power-of-another-number/
        #src: https://python-reference.readthedocs.io/en/latest/docs/float/is_integer.html
        
        #check if num is a positive or negative, if negative, return false
        if num <= 0:
            return False
        else:
            res1 = math.log(num) // math.log(4) 
            res2 = math.log(num) / math.log(4) #this is for double
            
            res1_c = res1.is_integer()
            res2_c = res2.is_integer()
            
            #compare if res1 = res2
            if (res1_c == res2_c):
                return True
            else:
                return False