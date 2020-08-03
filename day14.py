#familiarize with python annotation -> this will be useful for leetcode :P

#TASK: reverse integer problem from leetcode

class Solution:
    #src: https://www.geeksforgeeks.org/reverse-digits-integer-overflow-handled/
    def reverse(self, x: int) -> int:
        negFlag = False
        if x < 0:
            negFlag = True
            x = -x
        
        prevRevNum = 0 
        revNum = 0
        while (x != 0):
            curr = x % 10
            revNum = (revNum * 10) + curr
            
            #check if out of bounds: +/- 2^31 = +/- 2147483648
            if (revNum <= -2147483648 or revNum >= 2147483648):
                revNum = 0
            if ((revNum - curr) // 10 != prevRevNum):
                return 0
            
            prevRevNum = revNum
            x = x // 10
            
        return -revNum if (negFlag == True) else revNum
        
        