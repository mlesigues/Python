#Task: Longest Palindrome from Leetcode
#src: https://programmersought.com/article/85471148012/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        #use hashmap or dict to store how many times a character appears in the input
        dict = {}
        
        count = 0
        nextChar = 0 #is there a next character in the string input
        
        for occur in s:
            #the occurances of a character in the string input
            if occur in dict:
                dict[occur] += 1
            else:
                dict[occur] = 1
                
        for b in dict:
            if dict[b] % 2 == 0:
                count += dict[b]
            else:
                count += dict[b] - 1
                nextChar = 1
        
        count = count + nextChar
        return count
                