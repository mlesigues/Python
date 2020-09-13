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
                
