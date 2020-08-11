#Task: Excel Sheet Number from Leetcode
class Solution:
    #def titleToNumber(self, s: str) -> int:
    def titleToNumber(self, s):
        #src: https://www.geeksforgeeks.org/find-excel-column-number-column-title/
        result = 0
        
        for letter in range(len(s)):
            result *= 26
            result += ord(s[letter]) - ord('A') + 1
        
        return result
