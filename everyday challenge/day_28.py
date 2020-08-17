#Task: Palindrome Number from Leetcode
#src: https://www.geeksforgeeks.org/python-program-to-check-if-number-is-palindrome-one-liner/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        userInput = str(x)
        
        result = userInput == userInput [::-1] #compare the two 
        
        return result

#Task: Remove Duplicates from Sorted Array 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #the array is already sorted
        
        #check if nums is empty
        if len(nums) == 0:
            return 0
        
        counter = 0
        
        for i in range(len(nums)):
            if nums[i] != nums[counter]:
                counter += 1
                nums[counter] = nums[i]
                
        return (counter + 1)
        
                
        
