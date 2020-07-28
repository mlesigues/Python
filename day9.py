#TASK: A left rotation operation on an array of size n shifts each of the 
#array's elements 1 unit to the left. Given an array of n integers and a 
#number, d, perform d left rotations on the array. Then print the updated
#array as a single line of space-separated integers.
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0]) #number or elements inside 

    d = int(nd[1]) #number of left rotations

    a = list(map(int, input().rstrip().split()))
    
    #a[d:] = equivalent to "d to end"
    #a[0:d] = equivalent to "zero to d"
    addElems = a[d:] + a[0:d] 
    for i in range(len(addElems)):
        print(addElems[i], end = " ")

#TASK: The provided code stub will read in a dictionary containing key/value
#pairs of name:[marks] for a list of students. Print the average of the marks
#array for the student name provided, showing 2 places after the decimal.
#CONSTRAINTS: 2<=n<=10, 0<=marks[i]<=100, length of marks arrays = 3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    listOfSomething = student_marks[query_name]
    #print(listOfSomething)

    # #divide scores by 3 (3 because the marks are always going to be 3 entries)
    #sumAll = scores[0] + scores[1] + scores[2]
    sumAll = sum(listOfSomething)
    avg = round((sumAll / 3), 2)
    #finalAvg = round(avg, 2)
    print("%.2f" % avg)

   


