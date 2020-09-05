#Task: Introduction to Sets from Hackerrank
def average(array):
    # your code goes here

    #we only want the distinct numbers
    heights = set(array)
    numOfHeights = len(heights)

    avg = sum(heights)/numOfHeights

    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#Task: No Idea! from Hackerrank
#some strategies:
#we have to compare element per element in array to A, and array to B
n, m = input().split()
arrElems = [int(i) for i in input().split(' ')]
A = set([int(i) for i in input().split(' ')]) #like the integers here, +1
B = set([int(i) for i in input().split(' ')]) #does not like integers, -1

happiness = 0 #intial value
#check if we have empty array, A, B
if n == 0:
    happiness = 0
    print(happiness)
    
if len(A) == 0 and len(B) == 0:
    happiness = 0
    print(happiness)

for i in arrElems:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)

""" the code below is too slow for large elements!
for i in arrElems:
    for j in A:
        if i == j:
            happiness += 1
    for k in B:
        if i == k:
            happiness -= 1

    print (happiness)
"""


