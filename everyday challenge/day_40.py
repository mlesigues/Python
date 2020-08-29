class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        #whenever a zero appears, duplicate it by 1 then move the nonzero element to the right
        #if there are remaining elements that does not fit in the array, remove them(?)
        """
        #case: if there are no zero in the list
        for elem in range(0, len(arr)):
            if arr[elem] != 0:
                return arr
        """    
        
        #case: there are zero elements in the list
        #main problem here is the overwriting of the elements
                                                                                      
        possible_dups = 0
        length_ = len(arr) - 1
        
        #zeros to be duplicated
        for left in range(length_ + 1):
            if left > length_ - possible_dups:
                break
                
            #count zeros
            if arr[left] == 0:
                if left == length_ - possible_dups:
                    arr[length_] = 0
                    length_ -= 1
                    break
                possible_dups += 1
                
            #start from last element
            last = length_ - possible_dups
            """
            #copy zero 2x, non-zero 1x
            for i in range(last, -1, -1):
                if arr[i] == 0:
                    arr[i + possible_dups] = 0
                    possible_dups -= 1
                    arr[i + possible_dups] = 0
                else:
                    arr[i + possible_dups] = arr[i]
            """
            
              # Copy zero twice, and non zero once.
            for i in range(last, -1, -1):
                if arr[i] == 0:
                    arr[i + possible_dups] = 0
                    possible_dups -= 1
                    arr[i + possible_dups] = 0
                else:
                    arr[i + possible_dups] = arr[i]
                        
        

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        
