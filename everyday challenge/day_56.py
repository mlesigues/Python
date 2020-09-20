#Task: Missing Number from Leetcode
#src: https://www.tutorialspoint.com/missing-number-in-python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #strategy: arithemtic series! ==> n(n+1)/2 or binary search
        #binary search: sort list, length of the list = high, low = 0
        
        nums.sort()
        low = 0
        high = len(nums)
        
        while low < high:
            mid = low + (high-low)//2 #floor division
            if nums[mid] > mid: #search high side
                high = mid
            else: #search low side
                low = mid + 1
                
        
        return low
        
