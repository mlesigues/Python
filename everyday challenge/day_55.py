#Task: MaximumSubarray from Leetcode
#src: (for kadane's algo understanding) https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
from sys import maxsize

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm
        max_so_far = -maxsize - 1
        max_end_here = 0
        
        for i in range(0, len(nums)):
            max_end_here = max_end_here + nums[i]
            if (max_so_far < max_end_here):
                max_so_far = max_end_here
            
            if (max_end_here < 0):
                max_end_here = 0
                
        return max_so_far
