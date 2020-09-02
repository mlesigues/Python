#Task: Largest Time for Given Digits from Leetcode
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        #src: https://www.youtube.com/watch?v=sn6r0ZV_2y4
        res = ""
        
        for i in range(len(A)):
            for j in range(len(A)):
                for k in range(len(A)):
                    #i,j,k should not be the same value
                    if i == j or j == k or k == i:
                        continue
                    hh = str(A[i]) + str(A[j]) #concatenate
                    mm = str(A[k]) + str(A[6-i-j-k])
                    t = hh + ":" + mm
                    if (hh < "24" and mm < "60" and t > res):
                        res = t
        return res
                            