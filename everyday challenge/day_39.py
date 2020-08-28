#Task: Remove Element from Leetcode
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #only in-place modification with O(1) extra memory
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            if nums[0] == val:
                return 0
        
        nums.sort()
        
        i = 0
        numsLen = len(nums)
        
        while i < numsLen:
            if (nums[i] == val):
                nums[i] = nums[numsLen - 1]
                numsLen -= 1 #reduce list/array size by 1
            else:
                i += 1
                
        return numsLen
        
        
        
    
        
            