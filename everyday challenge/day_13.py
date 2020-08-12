#TASK: Given a full name, your task is to capitalize the name appropriately.
#input: s is the full name

# Complete the solve function below.
def solve(s):
    #s[0] = s.capitalize()
    #cap = s.capitalize()
    # for i in len(range(s)):
    #     if s[i] == " ":
    #         s[i+1] = s.capitalize()
    # for i in range(0, len(s)):
    #     if [s+1] == " ":
    #         cap = s.capitalize()
    # strSplit = s.split(" ")
    # for i in range(0, len(s)):
    #     i[0] = s.capitalize()
    #     if s[i] == strSplit:
    #         if s[i+1] != strSplit:
    #             s[i+1] = s.capitalize()
    # return s

    #newString = s
    #new_string = newString.capitalize()

    newString = s
    new_string = ' '.join(map(str.capitalize, newString.split(' ')))

    return new_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#TASK: matrix addition.
#input: user will input the two arrays => can be converted to matrices
from array import *

#src: https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/
userInput_Row = int(input("Enter the number of rows: "))
userInput_Col = int(input("Enter the number of columns: "))
print("Enter entries in a single line (press enter after each element): ")
#result = list(map(int, input("Enter array elements: ").split()))
result = []

#putting values into a matrix
for i in range(userInput_Row):
    emp = []
    for j in range(userInput_Col):
        emp.append(int(input()))
    result.append(emp)

#print matrix
for i in range(userInput_Row):
    for j in range(userInput_Col):
        print(result[i][j], end=" ")
    print()
