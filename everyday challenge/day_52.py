#Task: House Robber from Leetcode
class Solution:
    def rob(self, nums: List[int]) -> int:
        #base cases
        if len(nums) == 0:
            return 0
        
        #if len(nums) == 1:
        #    return nums[0]
        
        if len(nums) <= 2:
            return max(nums)
        
        #3 houses at least below
        
        #brute force approach
        robHouse = [0] * len(nums)
        
        robHouse[0] = nums[0] #first house
        robHouse[1] = max(nums[0], nums[1])
        
        for x in range(2, len(nums)):
            robHouse[x] = max(robHouse[x-1], nums[x] + robHouse[x-2]) #we're doing x-2, to prevent robbing the adjacent houses
            
        return robHouse[-1] 
            
        
        #dynamic programming approach
        """
        previous = 0
        current = 0
        
        for elems in nums:
            temp = current
            previous = current
            current = max(temp + num, previous)
        
        return current
        """

        
        
#Task: Day 6: The Central Limit Theorem I from Hackerrank
import math

maxWeight_elevator = int(input()) #total number of 'trial', x
num_boxes = int(input()) #this would be the sample size, n
mean_weight = int(input()) #mean, mu
stdDev = int(input()) #standard deviation, sigma

sample_mean_sums = num_boxes * mean_weight
sample_std_dev = math.sqrt(num_boxes) * stdDev

#cumulative distribution function (cdf) for normal distribution:
#Phi_X(x) = 1/2 * (1 + erf(x - mu / sigma sqrt(2)))
def phi(x, mean, stdDev):
    
    sqrt = math.sqrt(2)
    res = (0.5) * (1 + math.erf( (x - mean) / (stdDev * sqrt) ))
    return res


res = phi(maxWeight_elevator, sample_mean_sums, sample_std_dev)
res = round(res, 4)
print(res)




#Task: Day 6: The Central Limit Theorem II
import math

last_min_tickets = int(input())
students_waiting = int(input())
mean_purchased_tickets = float(input())
std_dev = float(input())

sample_mean_sum = students_waiting * mean_purchased_tickets 
sample_std_dev = math.sqrt(students_waiting) * std_dev

#cumulative distribution function (cdf) for normal distribution:
#Phi_X(x) = 1/2 * (1 + erf(x - mu / sigma sqrt(2)))
def phi(x, mean, stdDev):
    
    sqrt = math.sqrt(2)
    res = (0.5) * (1 + math.erf( (x - mean) / (stdDev * sqrt) ))
    return res

"""
res = phi(last_min_tickets, sample_mean_sum, sample_std_dev)
res = round(res, 4)
print(res)
"""

res = round(phi(last_min_tickets, sample_mean_sum, sample_std_dev), 4)
print(res)




#Task: Day 6: The Central Limit Theorem III
import math

sample_size = int(input())
mean = int(input())
stdDev = int(input())
dist_percent = float(input()) #as decimal
z_value = float(input()) #z score

#why this? because: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/forum/comments/179271
sample_std_dev = stdDev / math.sqrt(sample_size) 

#value of A; lower limit? (both A & B are symmetrical)
A = mean - z_value * sample_std_dev
A = round(A, 2)
print(A)

#value of B; upper limit?
B = mean + z_value * sample_std_dev
B = round(B, 2)
print(B)
