#link: https://pythonprinciples.com/challenges/

#1. Python Challenge: Write a function named capital_indexes. The function takes a single parameter, which is a string. 
#Your function should return a list of all the indexes in the string that have capital letters.

def capital_indexes(userInput):
    res = []
    for ind, elem in enumerate(userInput):
        #print(ind, "==" ,elem)
        if (elem.isupper() == True):
            res.append(ind)
    return res
        
#main   
userInput = "HeLlO"
capital_indexes(userInput)



#2. Python Challenge: Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. 
#If there is no middle letter, your function should return the empty string.

import math

def mid(userInput):
  if (len(userInput) % 2 == 0):
    print(" ") #even
    #explicitly return it
    return " "
    
  else:
    #print("odd")
    for ind, elem in enumerate(userInput):
      middleElem = (len(userInput)/2) - 1
      midElem = math.ceil(middleElem)
      res = userInput[midElem]
    print(res)

    #explicitly return it
    return res

#main
userInput = "aba"
mid(userInput)




#3. 




#4. Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.
#Calling the function multiple times should (usually) return different numbers.

import random

def random_number():
  res = random.randint(1, 100) #inclusive
  print(res)
  return res

random_number()


