#Task: Reverse String from Leetcode
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        return (s.reverse()) #can do it this way

        #another way
        #src: https://developers.google.com/edu/python/strings
        #copy the string and then reverse it
        s[:] = s[::-1]
        return s[:]

#To Lower Case from Leetcode
class Solution:
    def toLowerCase(self, str: str) -> str:
        return (str.lower())


#Defanging an IP address from Leetcode
#Note: A defanged IP address replaces every period "." with "[.]"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        result = address.replace(".", "[.]")
        return "". join(result)
  
