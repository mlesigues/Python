#Task: Length of Last Word from Leetcode
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #base case (i think the 1st if is repetitive?)
        if len(s) == 0 or s == '' or s == ' ':
            return 0
        
        if len(s) == 1:
            return 1
        
        
        #split string, then start from the back 
        s = s.split()
        if not s: 
            #meaning s empty; 
            #src: https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty#:~:text=Empty%20strings%20are%20%22falsy%22%20which,should%20use%20myString%20%3D%3D%20%22%22%20.
            return 0
        else:
            res = len(s[-1])
            
            return res
                
                
                
                    
        
