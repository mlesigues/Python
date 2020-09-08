#Task: Word Pattern from Leetcode
#src: https://www.youtube.com/watch?v=XC0dpyntbyA
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        #some strategies:
        #since each letter in the pattern maps to a word in str, we can use hashmap
        #need to make sure that the values of a and b are different from eaach other 
        
        words = str.split()
        
        if len(words) != len(pattern): #the words can never follow the pattern
            return False
        
        d = {}
        
        for x in range(len(words)):
            if pattern[x] not in d: #whatever pattern x is in not one of the keys
                if words[x] in d.values(): #check if any of the pattern values hold that word
                    return False
                d[pattern[x]] = words[x] #pattern does not exist yet
            else: 
                #now make sure that pattern[x] should only equal to a 1 word
                #remember that each pattern can only hold 1 word
                if d[pattern[x]] != words[x]:
                    return False
                
        return True
