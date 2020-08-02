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

userInput1 = int(input("Enter the length of the 1st array: "))
userInput2 = int(input("Enter the length of the 2nd array: "))
result = []

if range(userInput1) != range(userInput2):
    print("Error: the two arrays are not equal in length!")
else:
    #ask to input elements
    userLength1 = list(map(int, input("Enter 1st array elements, with space: ").split()))
    userLength2 = list(map(int, input("Enter 2nd array elements, with space: ").split()))
    #result = [userInput1[userInput2]]
    #iterate through rows
    # for i in range(len(userLength1)):
    #     #iterate through cols
    #     for j in range(len(userLength1)):
    #         result[i][j] = userLength1[i][j] + userLength2[i][j]
    # print(result)
    #iterate through rows
    for i in range(userInput1):
        firstArr = []
        for j in range(userInput2):
            firstArr.append(int(input()))
        result.append(firstArr)

    #print 
    for i in range(userInput1):
        for j in range(userInput2):
            print(result[i][j], end="")
        print()

