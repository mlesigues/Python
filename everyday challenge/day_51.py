#Task: Insert Interval from Leetcode
#src: https://www.youtube.com/watch?v=NWM4e4yda0w
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for x in intervals:
            if x[1] < newInterval[0]:
                result.append(x)
            elif newInterval[1] < x[0]:
                result.append(newInterval)
                newInterval = x
            else:
                newInterval[0] = min(newInterval[0], x[0])
                newInterval[1] = max(newInterval[1], x[1])
                
        result.append(newInterval)
        
        return result
                

        
        
#Task: Day 5: Poisson Distribution from Hackerrank
import math
x_mean = float(input())
want_probs = int(input())

#factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

#poisson dist: P(k, lambda) = (lambda)^(k) * e^(-lambda) / k!
def poisson(k, lamb):
    res = (lamb**k) * (math.e**-lamb) / fact(k)
    return res

result = poisson(want_probs, x_mean)
result = round(result, 3)
print(result)




#Task: Day 5:
