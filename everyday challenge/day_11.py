#TASK: concatenate strings based on user's string input and n times we concatenate it

#function that concatenate/combine the strings
def stringsTogether(userString, numTimes):
    #src: https://www.journaldev.com/23689/python-string-append#:~:text=If%20you%20simply%20want%20to,to%20get%20the%20result%20string.
    output = " "
    i = 0
    while i < numTimes:
        output += userString
        i += 1
    return output

userString = input("Enter a string: ")
numTimes = int(input("Enter a number of times: "))

#ask user to enter a string
if numTimes > 0:
    # userString = input("Enter a string: ")
    # numTimes = int(input("Enter a number of times: "))
    #stringsTogether(userString, userRepeat)
    print("The resulting string is:", stringsTogether(userString, numTimes))
else:
    print("Error: you entered a wrong value/s! ")


#TASK: sort array (high to low or low to high); SORT USING SELECTION SORT!
#      user will input array size and elements, and ask if user wants ascending or descending order

#function for ascending selection sort
def ascSelectionSort(arrElems, userInput):
    for i in range(len(arrElems)):
        #minimum element in the array
        minElem = i
        for j in range((i+1), len(arrElems)):
            if arrElems[minElem] > arrElems[j]: #is the minimum element larger than the current j?
                minElem = j #sets j as the current minimum value
        
        #swap the found minimum element with the first element
        arrElems[i], arrElems[minElem] = arrElems[minElem], arrElems[i]
    
    a = "Sorted array from lowest to highest: "
    b = arrElems
    print("{}{}".format(a, b))


#function for descending selection sort
def descSelectionSort(arrElems, userInput):
    for i in range(len(arrElems)):
        #maximum element in the array
        maxElem = i
        for j in range((i+1), len(arrElems)):
            if arrElems[maxElem] < arrElems[j]:
                #maxElem = j 
                temp = arrElems[j]
                arrElems[j] = arrElems[i]
                arrElems[i] = temp
        
    arrElems[i], arrElems[maxElem] = arrElems[maxElem], arrElems[i]

    a = "Sorted array from highest to lowest: "
    b = arrElems
    print("{}{}".format(a, b))


#ask user to enter array size and its elements
userInput = int(input("Enter array size: "))
if userInput <= 0:
    print("Error: you entered incorrect value/s! ")
else:
    arrElems = list(map(int, input("Enter array elements, with space: ").split()))
    
    #ask the user if they want to sort it in ascending or descending order
    userChoice = int(input("Sort in ascending(0) or descending(1) order: "))

    if userChoice == 0:
        #ascending order
        ascSelectionSort(arrElems, userInput)
    
    elif userChoice == 1:
        #descending order
         descSelectionSort(arrElems, userInput)

    else:
        print("Error: you entered an incorrect choice! ")
