#TASK: write a while loop that verifies that the user enters a positive integer value

userInput = int(input("Enter an integer value: "))

while (userInput > 0):
    print("This is a POSITIVE integer")
    #this prevents infinite loop
    break 
else:
    print("This is a NEGATIVE integer")

#TASK 2: write a method that accepts a character parameter and returns true if 
#that char is either an uppercase or lowercase letter
def isAlpha(userChar):
    print ('The letter is: ' + userChar)
    #print(userChar)

    if userChar.islower() == True:
        print("The letter " + userChar + " is a lowercase")
        #print(userChar.islower())
        print("This is False")
    else:
        print("The letter " + userChar + " is an upperrcase")
        #print(userChar.isupper())
        print("This is True")


#tester
userChar = "A"
isAlpha(userChar)

userChar1 = "x"
isAlpha(userChar1)

