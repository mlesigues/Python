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



