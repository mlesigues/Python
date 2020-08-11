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

#Below is the reverse of this
#Task: Find excel column name from a given column number
#Example:
""" 
    Input       Output
     26          z
     51          AY
     52          AZ
     80          CB
"""

"""
    Process: 
    Take the modulo of n using 26. If the modulo is 0, then put 'Z' and 
    new n would be (n/26) - 1 because 26 is 'Z' while it's actually 25th in respect
    to 'A'.

    If modulo is non-zero, then insert the char accordingly in the string and do
    n = (n/26).

    Then reverse the string and print.
"""

MAX = 50

def printExcelCol(n):

    storage = ["\0"] * MAX

    curr = 0

    while n > 0:
        remainder = n % 26

        if remainder == 0:
            storage[curr] = 'Z' 
            curr += 1
            n = (n / 26) - 1

        else:
            storage[curr] = chr((remainder - 1) + ord('A'))
            curr += 1
            n = (n / 26)
            
    storage[curr] = '\0'

    storage = storage[::-1] #reverse string
    finalRes = "".join(storage)
    return finalRes

#test
colNum = 26
corVal = printExcelCol(colNum) 
print("The column number is {}, and the corresponding letter is: {} " .format(colNum, printExcelCol(colNum)))
#printExcelCol(26) 
#printExcelCol(51) 
colNum = 51
corVal = printExcelCol(colNum) 
print("The column number is {}, and the corresponding letter is: {} " .format(colNum, printExcelCol(colNum)))




    


            
        