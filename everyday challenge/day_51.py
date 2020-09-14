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
                

        
        
#Task: Day 5: Poisson Distribution I from Hackerrank
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




#Task: Day 5: Poisson Disctributio II from Hackerrank
values = list(map(float, input().split(' ')))

A_mean = values[0]
B_mean = values[1]

#cost of A operation: 160+40X^2; 
#X^2 would be change to A_mean + A_mean^2
#why? because this: https://www.hackerrank.com/challenges/s10-poisson-distribution-2/forum/comments/293964
A_operation = 160 + 40 * (A_mean + A_mean**2)
A_operation = round(A_operation, 3)
print(A_operation)

#cost of B operation: 128+40Y^2
#Y^2 would be change to B_mean + B_mean^2
B_operation = 128 + 40 * (B_mean + B_mean**2)
B_operation = round(B_operation, 3)
print(B_operation)




#Task: Day 5: Normal Distribution I from Hackerrank
import math

values = list(map(int, input().split(' ')))
X_mean = values[0]
X_std_dev = values[1]
question1 = float(input())
question2 = list(map(int, input().split(' ')))
q2_lower_range = question2[0]
q2_upper_range =question2[1]


#cumulative distribution function (cdf) for normal distribution:
#Phi_X(x) = 1/2 * (1 + erf(x - mu / sigma sqrt(2)))
def phi(x, mean, stdDev):
    
    sqrt = math.sqrt(2)
    res = (0.5) * (1 + math.erf( (x - mean) / (stdDev * sqrt) ))
    return res


res1 = phi(question1, X_mean, X_std_dev)
res1 = round(res1, 3)
print(res1)

res2 = phi(q2_upper_range, X_mean, X_std_dev) - phi(q2_lower_range, X_mean, X_std_dev)
res2 = round(res2, 3)
print(res2)




#Task: Day 5: Normal Distribution II
import math

mean, stdDev = map(int, input().split(' '))
q1 = int(input())
threshold = int(input())

#cumulative distribution function (cdf) for normal distribution:
#Phi_X(x) = 1/2 * (1 + erf(x - mu / sigma sqrt(2)))
def phi(x, mean, stdDev):
    
    sqrt = math.sqrt(2)
    res = (0.5) * (1 + math.erf( (x - mean) / (stdDev * sqrt) ))
    return res

#note: need to convert to percentage! so multiply it by 100
res1 = (1- phi(q1, mean, stdDev)) * 100
res1 = round(res1, 2)
print(res1)

res2 = (1- phi(threshold, mean, stdDev)) * 100
res2 = round(res2, 2)
print(res2)

res3 = phi(threshold, mean, stdDev) * 100
res3 = round(res3, 2)
print(res3)
