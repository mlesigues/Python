#source: https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
#https://www.geeksforgeeks.org/python-arrays/

#sort arrays given by the user and find the index of an element
#user will give the length and the array's elements
from array import *

userInput = int(input("Enter array size: "))

if userInput <= 0:
    print("Error: Invalid input.")
else:
    #src: https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
    userElems = list(map(int, input("Enter array elements: ").split()))
    #print("Array elements: ",userElems)

    #find the index of a user given element
    findIt = int(input("Enter the element you want to find: "))
    for i in userElems:
        a = "The element "
        b = findIt
        c = " can be found at index: "
        d = userElems.index(findIt)
        print("{}{}{}{}".format(a, b, c, d))
        #print(userElems.index(findIt))
        break

    #sort the array from low to high
    for i in range(len(userElems)): #will start at index 0
        for j in range(i+1, len(userElems)): #will start at index 1
            if userElems[i] > userElems[j]:
                userElems[i], userElems[j] = userElems[j], userElems[i]
    
    a = "Sorted array from lowest to highest: "
    b = userElems
    print("{}{}".format(a, b))

    #sort array from high to low
    for i in range(len(userElems)):
        for j in range(len(userElems)):
            if userElems[j] < userElems[i]:
                cond = userElems[j]
                userElems[j] = userElems[i]
                userElems[i] = cond
    a = "Sorted array from highest to lowest: "
    b = userElems
    print("{}{}".format(a, b))
