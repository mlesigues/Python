#Task: Find Minimum in Rotated Sorted Array from Leetcode

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #assume no duplicate exists in the array
        
        #some strategies: (Naive way)
        #since the sorted array is going to be rotated by some unknown pivot,
        #sort it again(asc), and the first index should be the minimum element
        #another way is to use binary search!
    
        nums.sort()
        
        if len(nums) == 0:
            return 0
        
        return nums[0]

#Task: Find Minimum in Rotated Sorted Array II from Leetcode
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #array may contain duplicates
        
        #some strategies: (NAIVE WAY)
        #sort the list again, and should we worry about the repeated element?
        #since we're only concern for the minimum element, this minimum element
        #would be the first element
        #(thoughts) i'm gonna completely ignore the repeated elements, and we'll see ===> it worked lol!!!
        
        #for better performance, use binary search!
        
        nums.sort()
        
        if len(nums) == 0:
            return 0
        
        minElem = nums[0]
        
        return minElem
    