#Task: Non-overlapping Intervals from Leetcode
#src: https://www.youtube.com/watch?v=nXBQJoS1W8A

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        Note:
            1. You may assume the interval's end point is always bigger than its start point
            2. Intervals like [1, 2] and [2, 3] have borders 'touching' but don't overlap each other

        intervals = List[List[int]] ==> the variable 'intervals' is a list of list of integers
        """

        """
        Approach: can sort out the lists from desc - asc, then have a counter variable. Go through the
        assorted lists, if we find a duplicate/overlapped value, increase the counter variable. 
        -- we know that the starting point is always smaller than the end point so, we could compare the 
        endpoint of the first pair to the next pair, and if the endpoint of the first pair is bigger than the
        second pair, it overlaps.
        """

        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x:x[1]) #sort by the endpoints, not starting point!

        maxNum = float('-inf')
        result = 0

        for start, end in intervals:
            if start >= maxNum:
                maxNum = end
            else:
                result += 1
        
        return result

#Task: Two Sum from Leetcode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #check for empty list
        if len(nums) == 0:
            return 0
        
        #brute force approach; 
        #loop through each element and use subtraction to get the remaining number 
        
        seen = {} #store the values to keep track
        
        for first, value in enumerate(nums):
            remaining = target - value
            
            if remaining in seen:
                return [seen[remaining], first]
            else:
                seen[value] = first
            
            #return []
    
        

        
