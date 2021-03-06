#Task: Distribute Candies to People from Leetcode
#src: https://www.youtube.com/watch?v=IX4iFnEXrhM


class Solution:
    def distributeCandies(self, candies, num_people):
        x = 0
        candy_list = [0] * num_people
        
        while candies > 0:
            candy_list[x % num_people] += min((x+1), candies)
            x += 1
            candies -= x 
        
        return candy_list
            

#Task: Single Number from Leetcode

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = []
        
        for i in nums:
            if i not in check:
                check.append(i)
            else:
                check.remove(i)
                
        return check.pop()
            
            
        
        