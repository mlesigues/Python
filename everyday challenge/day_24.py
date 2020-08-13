#Task: Pascal's Triangle I from Leetcode
#src: 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        #if row is 0
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle


        
        
        