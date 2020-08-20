#Task: Reverse String from Leetcode
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        return (s.reverse())
        

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
  