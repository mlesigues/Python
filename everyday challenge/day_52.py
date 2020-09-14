#Task: House Robber from Leetcode
class Solution:
    def rob(self, nums: List[int]) -> int:
        #base cases
        if len(nums) == 0:
            return 0
        
        #if len(nums) == 1:
        #    return nums[0]
        
        if len(nums) <= 2:
            return max(nums)
        
        #3 houses at least below
        
        #brute force approach
        robHouse = [0] * len(nums)
        
        robHouse[0] = nums[0] #first house
        robHouse[1] = max(nums[0], nums[1])
        
        for x in range(2, len(nums)):
            robHouse[x] = max(robHouse[x-1], nums[x] + robHouse[x-2]) #we're doing x-2, to prevent robbing the adjacent houses
            
        return robHouse[-1] 
            
        
        #dynamic programming approach
        """
        previous = 0
        current = 0
        
        for elems in nums:
            temp = current
            previous = current
            current = max(temp + num, previous)
        
        return current
        """
