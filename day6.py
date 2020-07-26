#TASK: write a while loop that verifies that the user enters a positive integer value

userInput = int(input("Enter an integer value: "))

while (userInput > 0):
    print("This is a POSITIVE integer")
    #this prevents infinite loop
    break 
else:
    print("This is a NEGATIVE integer")

