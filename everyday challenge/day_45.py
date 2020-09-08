#Task: Symmetric Difference from Hackerrank
#Note: it works(passed all tests), but the newline printing could be better!
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input().split(' ')
#arrElems_M = [int(i) for i in input().split(' ')]
arrElems_M = set([int(i) for i in input().split(' ')])
n = input().split(' ')
arrElems_N = set([int(i) for i in input().split(' ')])

#goal: symmetric difference in asc order, one per line

#symmetric difference: indicates those values that exist in either M or N, but not both
partial = arrElems_M.union(arrElems_N)
res_m = arrElems_M.difference(arrElems_N) #Values which exist in m but not in n
res_n = arrElems_N.difference(arrElems_M) #Values which exist in n but not in m

#convert sets to lists
res_m = list(res_m)
res_n = list(res_n)
res = sorted(res_m + res_n) #asc sort
for elem in res:
    print(elem)
print('\n')


#Task: Image Overlap from Leetcode
    #solution w/explanationjn: https://leetcode.com/discuss/explore/september-leetcoding-challenge/832236/image-overlap-python-3-solution


