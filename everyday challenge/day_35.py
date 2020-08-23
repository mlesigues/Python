#NOTE: Going over the Arrays Module on Leetcode
#Task: Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #some strategies:
        #we can create a list, called oneList that holds only the value of 1s, if the next value in 
        #the nums is not 1, delete (kinda like start over) the elements in oneList and add that new
        #element and get the length of the oneList
        
        #what if we just created a counter that counts how many 1s/gets the next element in the list?
        
        #from gfg: have a counter and a maximum variables, counter will count/keep track of 1s,
        #and compare it with maximum, if the next value is not 1, reset the counter to 0
        #src: https://www.geeksforgeeks.org/maximum-consecutive-ones-or-zeros-in-a-binary-array/
        
        oneCounter = 0
        maximumOne = 0
        
        for ones in range(0, len(nums)):
            #reset the counter to 0, if not 1
            if nums[ones] == 0:
                oneCounter = 0
            #if 1 is found, increment oneCounter, and update maximum if oneCounter keeps increasing
            #use max()
            else:
                oneCounter += 1
                maximumOne = max(maximumOne, oneCounter)
                
        return maximumOne
                
            
