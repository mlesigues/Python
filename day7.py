#TASK: Write a for loop to print all multiples of 3 that are less than 100
for x in range(0, 100):
    if x % 3 == 0:
        print "This number is a multiple of 3: " , x

#TASK: The provided code stub reads and integer, n, from STDIN. For all non-negative integers
#i < n, print i^2.
if __name__ == '__main__':
    n = int(input())

    #n must be less than or equal to 20, so check if it's bounded
    if n > 0 and n > 20: 
        exit
    else:
        for x in range(n):
           #this is the i^2 part
           x = x*x 
           print(x)

#TASK: Given a year, determine whether it is a leap year. If it is a leap year, 
#return the Boolean True, otherwise return False.
#Note that the code stub provided reads from STDIN and passes arguments to 
#the is_leap function. It is only necessary to complete the is_leap function.
def is_leap(year):
    leap = False
    
    # Write your logic here

    #The three conditions used to identify leap years:
    #The year can be evenly divided by 4, is a leap year, unless:
        #The year can be evenly divided by 100, it is NOT a leap year, unless:
            #The year is also evenly divisible by 400. Then it is a leap year.
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
    return leap

year = int(input())
print(is_leap(year))

