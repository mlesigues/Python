#TASK: write a while loop that verifies that the user enters a positive integer value

userInput = int(input("Enter an integer value: "))

while (userInput > 0):
    print("This is a POSITIVE integer")
    #this prevents infinite loop
    break 
else:
    print("This is a NEGATIVE integer")

print("------------------------------------------------") 
print("------------------------------------------------") 
print("------------------------------------------------") 
       
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

print("------------------------------------------------") 
print("------------------------------------------------") 
print("------------------------------------------------") 

#TASK 3: write a method that accepts three integer that represents the lengths of the sides
#of the triangle. The method returns true if the triangle is isosceles but not equilateral
#and false otherwise.

#isosceles triangle = two sides are equal in length

def isIsosceles(side1, side2, side3):
    #print out the sides
    print("The sides are: " + str(side1) + ", " + str(side2) + " and " + str(side3))

    #possible sides that can be equal: side1 = side2, side2 = side3, side3 = side1

    #checks if 2 sides are equal
    if side1 == side2 or side2 == side3 or side3 == side1:
        print("This is an isosceles triangle")
        return True
    else:
        print("This is not an isosceles triangle")
        return False

#tester
side1 = 5
side2 = 6
side3 = 5
isIsosceles(side1, side2, side3)

side1 = 50
side2 = 65
side3 = 57
isIsosceles(side1, side2, side3)
