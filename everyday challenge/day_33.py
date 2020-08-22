#Task: Sort Array By Parity from Leetcode

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        #even numbers first, then odd numbers the end
        
        #some strategies; 
        #list Even will be contain the even numbers,  list Odd will contain odd numbers
        #join the two lists, containing list Even first then list Odd
        
        listEven = []
        listOdd = []
        
        #listEven = A.copy()
        #listOdd = A.copy()
        
        #put the even elements in listEven
        for num in A:
            if (num % 2 == 0):
                listEven.append(num)
            else:
                listOdd.append(num)
            
        #return listEven
        #return listOdd
        return listEven + listOdd


#Task: Plus One from Leetcode
#src: (on the else part)https://leetcode.com/problems/plus-one/discuss/24085/Simple-Python-solution-with-explanation-(Plus-One)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #if the list only contain 1 element
        #if len(digits) == 1 and digits[0] != 9:
        #    digits[0] = digits[0] + 1
        #    return digits
        
        #esp. case, if element is number 9 => should return as [1,0]
        if len(digits) == 1 and digits[0] == 9:
             return [1, 0]
            
        #if more than one element, go to the end of the list and add 1
        #else:
        for i in range(len(digits)):
            if i == (len(digits)-1) or digits[-1] != 9: #are we the end?
                digits[-1] = digits[-1] + 1 #we're at the last element, then add 1
                return digits
            else:
                #this handle if the nums is like this: [9, 9] or something like that 
                digits[-1] = 0
                digits[:-1] = self.plusOne(digits[:-1])
                return digits
            
        #esp. case, if element is number 9 => should return as [1,0]
        #if len(digits) == 1 and digits[0] == 9:
        #     return [1, 0]
            
        