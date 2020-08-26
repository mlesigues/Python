#Task: Length of Last Word from Leetcode

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #some strategies:
        #(easy) split the string, then read from the back
        
        
        splitStr = s.split()
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        for letter in range(0, len(splitStr)):
            return (len(splitStr[-1])) #read from the back
        
        """
        for char in range(0, len(fromBack)):
            while s[char] != ' ':
                wordCount += 1
                break
        return wordCount
        """
        