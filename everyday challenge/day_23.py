#Task: H-index from Leetcode
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #src: https://medium.com/leetcode-cracker/274-h-index-ef70c8735df

        #hint: sort the array first
        #hint: max value of h is the amount of paper we have
        
       
        #check if the list is empty 
        if len(citations) == 0:
            return 0
        
        #sorts the list into descending order
        citSort = sorted(citations, reverse=True)
            
        result = 0
            
        while result < len(citSort) and citSort[result] >= result + 1:
            result += 1
                
        return result 

                
                    
        
            
        
        