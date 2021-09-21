#madlibs game in python

#storage = {} #will store the keys(question number) 
            #and values (user answers to the question)
#user_ans = [] #store the user answers

user_cond = input("Are you ready? Y or N: ")
if user_cond == "Y" or user_cond == "N" or user_cond == "y" or user_cond == "n":
    if user_cond == "N" or user_cond == "n":
        print("You are not ready to play. Exiting the program.")
    if user_cond == "Y" or user_cond == "y":
        print("Please answer the following questions.")
    while (user_cond == "Y" or user_cond == "y"):
        numb = input("enter a number: ")
        specTime = input("enter a measure time: ")
        modeTranspo = input("enter mode of transportation: ")
        madlib = f"It was about {numb} {specTime} ago when I came into the hospital in a {modeTranspo}."
        break
    print(madlib)
else:
    print("Invalid answer. Exiting the program.")
