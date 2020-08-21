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
        
        