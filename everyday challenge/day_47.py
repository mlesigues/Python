#Task: String Validators from Hackerrank
if __name__ == '__main__':
    s = input()

    """
    for elem in s:
        #if any(elem == elem.isalnum()):
        #    print(elem.isalnum())
        any(s.isalnum())
        if elem == elem.isalpha():
            print(elem.isalpha())
        if elem == elem.isdigit():
            print(elem.isdigit())
        if elem == elem.islower():
            print(elem.islower())
        if elem == elem.isupper():
            print(elem.isupper())
        """

    print(any(elem.isalnum() for elem in s))
    print(any(elem.isalpha() for elem in s))
    print(any(elem.isdigit() for elem in s))
    print(any(elem.islower() for elem in s))
    print(any(elem.isupper() for elem in s))

    
    
#Task: Day 0: Mean, Median and Mode from Hackerrank Statistics!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_of_elems = int(input())
#arr_elems = list(map(int, input().split()))
arr_elems = [int(i) for i in input().split()]
arr_elems.sort()

#calculate mean and answer should have 1 decimal place
avg = sum(arr_elems)/len(arr_elems)
mean = round(avg, 1)
print(mean)

#calculate median
#some thoughts: what if we have even elements?
if len(arr_elems) % 2 != 0:
    #get the middle element and the one before it
    mid = arr_elems[int(len(arr_elems)/2)]
    before_mid = arr_elems[int(len(arr_elems)/2 - 1)]
    mode = (mid + before_mid)/2
    print(mode)
else:
    #still get the half element, floor it? or ceil it?
    uneven_mid = arr_elems[int(len(arr_elems)//2)] #this is flooring
    uneven_before_mid = arr_elems[int(len(arr_elems)//2 - 1)]
    mode = (uneven_mid + uneven_before_mid)/2
    print(mode)
    

#calculate mode
mode = sorted(sorted(Counter(arr_elems).items()), key = lambda x:x[1], reverse = True)[0][0] #src: https://www.hackerrank.com/challenges/s10-basic-statistics/forum/comments/239762
print(mode)
#-----this code below fails the 3rd test case!-----
#for elem in arr_elems:
    #print(elem, "\t:", arr_elems.count(elem))
    #occur = arr_elems.count(elem)
#print(arr_elems[0])
