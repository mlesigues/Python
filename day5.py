#TASK: 
#The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following:
#123...n (without whitespaces in between)
#for example, n = 5 => 1235. Constraints: 1 <= n <= 150.

if __name__ == '__main__':
    n = int(input())

    #using python 3
    #create a for loop that starts from the beginning and ends in N+1
    #the end="" prints the number without new lines after each other
    for i in range(1, n+1):
        print (i, end="")
        
print("--------------------------------------------")
print("--------------------------------------------")
print("--------------------------------------------")

#data structure: insertion sort
#given an array of numbers, create a function that sorts them from least to greatest

def insertionSort(arrOfChars):
  #insertion loop 
  for index in range(1, len(arrOfChars)):
    #current char to insert
    cur = arrOfChars[index]
    #start at previous char 
    prev = index - 1
    #while arrOfChars[index] is out of order 
    while prev >= 0 and (arrOfChars[prev] > cur):
      #move arrOfChars[prev] to the right
      arrOfChars[prev + 1] = arrOfChars[prev]
      #decrement prev by 1
      prev -= 1
    
    #proper place for the cur 
    arrOfChars[prev + 1] = cur


#call function to test
arrOfChars = [2, 5, 8, 9, 3, 1]
insertionSort(arrOfChars)
print(arrOfChars)

charsToTest = [9, 6, 1, 2, 3, 4]
insertionSort(charsToTest)
print(charsToTest)

print("--------------------------------------------")
print("--------------------------------------------")
print("--------------------------------------------")

#recreating my CSE30 lab 2 array1 exercise

#NOTE: THIS IS NOT CORRECT, WILL CORRECT IT SOON!

#familiarizing arrays

#we want to check if an array of numbers input by the user is increasing. This happens if each element of the array contains a value that is larger than the value contained in previous elements.

#First, you should ask the user to enter the size of the array
userInput = int(input("Enter the size of the array: "))

#If the user enters an incorrect size, you should output the error message 
if userInput <= 0:
  print("ERROR: you entered an incorrect value for the array size!")
  exit
else:
  userNumber = []
  #If the input is a valid size for the array, ask the user to enter the data, by outputting: 
  userNumber = int(input("Enter the numbers in the array and press enter: "))

  condition = 0

  if (condition == 1):
    print("This IS an increasing array!")
  else:
    print("This is NOT an increasing array!")


  #Once the input is complete, check if the array is increasing
  for i in range(len(userNumber)):
    #if the current value is less than or equal to the next value, return true
    if(userNumber[i] <= userNumber[i+1]):
      condition = 1
    else:
      condition = 2


