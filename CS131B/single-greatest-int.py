'''
Write a program that indicates the single greatest integer in 
the text /users/abrick/resources/urantia.txt
'''

import re

#looks for the single greatest integer in Urantia and prints it
def greatestInt():
    #open file
    fname = '/users/.../.../urantia.txt' #change the file path to whatever needed

    #src: https://developers.google.com/edu/python/regular-expressions
    fileOpen = open(fname, "r")


    #using regex, find all the integers and store it in justInt list 
    justInt = re.findall(r'[0-9]+', fileOpen.read())

    #change the elements in justItnt -> ints
    justInts = [int(elem) for elem in justInt]

    #after finding all integers, get the biggest/largest integer
    maxElem = max(justInts)

    #let the user see the 5 largest integers
    justInts.sort()
    bigFive = justInts[-5:]

    print("The 5 biggest integers in Urantia are: ", bigFive)
    print("The single greatest integer in Urantia is: ", maxElem)

#main funct
if __name__ == '__main__':
    greatestInt()
