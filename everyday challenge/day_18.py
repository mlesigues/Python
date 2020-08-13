import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
print(arr)

#Task: Find All Duplicates in an Array from Leetcode
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
         
        # count = [] #counts if the element appears twice
        # for i in range(len(nums)):
        #     k = i + 1
        #     for j in range(k, len(nums)):
        #         if nums[i] == nums[j] and nums[i] not in count:
        #             count.append(nums[i])
        #         return count 
        
        #src:https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python
        return [k for k,v in Counter(nums).items() if v>1]
        
     
        
       
        
            
        
