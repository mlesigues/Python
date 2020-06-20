#continuation of python part 1

#how to ask for user input? and save their input?
# user = input("What is your name?")
# print(user)

#conditional statements

#if statement
# food = "spam"

# if food == "spam":
#     print("Ummm, my favorite!")
#     print("I feel like typing it 10 times...")
#     print(10 * (food + "! "))

#run the code, what's happening?
#what happens if you change the food variable?
print("----------------------------------------------------------")

#if else statement
# food1 = "eggs"

# if food1 == "spam":
#     print("Umm, my favorite!")
# else:
#     print("No, I won't have it!")
# #try to execute the else part of the statement
# print("----------------------------------------------------------")

#chained conditional = if we want to express more than two possibilities
#and need more than two branches
# food2 = "rice"

# if food2 == "spam":
#     print("this is spam!")
# elif food2 == "egg":
#     print("this is an egg")
# else:
#     print("sorry, invalid choice")

# print("----------------------------------------------------------")

# #nested conditional = another way to express multiple branches
# #REMINDER: if using a nested conditional, a coder must be careful
# #to properly  write this as this could cause a confusion if another
# #coder is reading your code
# food3 = "egg"

# if food3 == "spam":
#     print("this is spam!")
# else:
#     if food3 == "egg":
#         print("this is an egg")
#     else:
#         print("sorry, invalid input")

# print("----------------------------------------------------------")
# print("----------------------------------------------------------")
# print("----------------------------------------------------------")
# print("----------------------------------------------------------")
# print("----------------------------------------------------------")

# #exercise: create a function that checks if a user input is divisible by 2.
def isItdivisible():
    userInput = input("Enter number: ")
    if (userInput % 2) == 0:
        print(str(userInput) + " is divisible by 2")
    else:
        print(str(userInput) + " is not divisible by 2")

isItdivisible()


