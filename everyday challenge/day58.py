#Check If Two String Arrays are Equivalent from Leetcode

/*
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
*/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        #all lowercase
        
        #thinking: add all the string in word1, do the same for word2
        #compare each element in word1 into word2, if the placing of 
        #the strings are the same, return true, else false
        
        temp1 = "".join(word1)
        temp2 = "".join(word2)
        
        if temp1 == temp2:
            return True
        else:
            return False
