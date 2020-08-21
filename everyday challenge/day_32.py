#Task: Contains Duplicate
#Src: https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        #add contents of list in a set; set only contains unique chars/vals
        numSet = set(nums)
    
        numLenSet = len(numSet)
        
        if len(nums) == numLenSet:
            return False
        
        return True
            
    
        
            