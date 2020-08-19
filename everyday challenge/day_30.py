#Task: Sqrt(x) from Leetcode

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        
        ans = math.sqrt(x)
        final = math.trunc(ans)
        
        return final
    
    
#Task: Valid Perfect Square from Leetcode
#src:https://www.geeksforgeeks.org/check-if-a-number-is-perfect-square-without-finding-square-root/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
     #cannot use sqrt() function
    
        itr = 1
        
        while(itr * itr <= num):
            if ((num % itr == 0) and (num/itr == itr)):
                return True
            itr += 1
            
        return False


        
        
        

