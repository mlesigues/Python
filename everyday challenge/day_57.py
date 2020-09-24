#Task: Majority Element II from Leetcode
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
         #element should appear n/3 times
        
        #base case
        #if len(nums) == 0:
        #    return []
        
        if not nums:
            return []
        listLen = len(nums)
        candidate1, count1 = None, 0
     
        candidate2, count2 = None, 0
        
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
                
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            
            else:
                count1 -= 1
                count2 -= 1
               
                
        return [x for x in [candidate1, candidate2] if nums.count(x) > (listLen//3)]
    
