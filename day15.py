class Solution:
#function returns true if the given string is a palindrome, otherwise false empty string as valid palindrome
    def isPalindrome(self, s: str) -> bool:
        empStr = '' #creates empty string  
    
        if s == '': 
            return True
        else:
            for i in range(0, len(s)):
                if ((s[i] >= 'a' and s[i] <= 'z') or s[i] >= '0' and s[i] <= '9' or (s[i] >= 'A' and s[i] <= 'Z')):
                    empStr += s[i]
            empStr = empStr.lower()      

        #src: https://www.geeksforgeeks.org/sentence-palindrome-palindrome-removing-spaces-dots-etc/
        for i in range(0, int(len(empStr)/2)):
             if (empStr[i] != empStr[len(empStr) - 1 - i]):
                 return False
             return True
