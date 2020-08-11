#Task: Write a program that accepts a user's name as an input
#and calculates the numeric value of the name. The numeric value
#is calculated by summing each letter of the name, assuming a = 1, b = 2,
#and so on,. The case of the letter does not matter, that is a = 1 and A = 1.

def calcName(str):

    #userInput = input("Enter name: ")
    userInput = input(str)

    #this will count the overall sums
    sums = 0

    #to ensure that we stick to 97+, convert the letters to lower case
    name = userInput.lower()

    #use ord() and sum function
    for x in str:
        print(x)
        sums += ord(x) - 96

    print("-----")
    print(sums)

    return sums


#call function
calcName("name")


#BELOW IS ANOTHER VERSION THAT DOES NOT ACCEPT AN ARGUMENT
def calcName():

    userInput = input("Enter name: ")

    #this will count the overall sums
    sums = 0

    #to ensure that we stick to 97+, convert the letters to lower case
    name = userInput.lower()

    #use ord() and sum function
    for x in userInput:
        sums += ord(x) - 96
        print() #newline

    print("-----")
    print(sums)

    return sums


#call function
calcName()
