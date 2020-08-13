#Task: Rotten Oranges from Leetcode
#src: https://www.youtube.com/watch?v=TzoDDOj60zE
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        #create a storage to store fresh and rotten oranges; can use a hashmap/dict
        freshOrange = set()
        rottenOrange = set()
        
        #if not grid or not grid[0]:
        #    return -1
        
        #set up the grid, and "populate"
        row, col = len(grid), len(grid[0])
        for i in range (row):
            for j in range(col):
                if grid[i][j] == 1:
                    #fresh orange
                    freshOrange.add((i, j))
                elif grid[i][j] == 2:
                    #rotten orange
                    rottenOrange.add((i, j))
        
        if freshOrange == 0:
            return 0
        if not freshOrange:
            return 0
        if not rottenOrange:
            return -1
        
            
        minute = 0
        directions = [(-1, 0),(1, 0),(0, 1),(0, -1)]
        
        while len(rottenOrange) > 0:
            #minute += 1
            new_rottenOrange = set()
            for i, j in rottenOrange:
                #check all directions
                for di, dj in directions:
                    r = i + di 
                    c = j + dj
                    if (r,c) in freshOrange:
                        new_rottenOrange.add((r,c))
                
            if not new_rottenOrange:
                return -1
            
            if len(rottenOrange) == 0:
                return -1
                
            freshOrange -= new_rottenOrange
            minute += 1
            rottenOrange = new_rottenOrange
                
            if not freshOrange:
                return minute
            
            #return minute
  



