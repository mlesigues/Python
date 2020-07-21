#TASK:
#Given and integer n, perform the following conditional actions:
#if n is odd, print Weird
#if n is even and in inclusive range of 2 to 5, print Not Weird
#if n is even and in inclusive range of 6 to 20, print Weird
#if n is even and greater than 20, print Not Weird

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

#function that checks in n is:
#odd = print weird
#even and inclusive range 2 - 5, print Not Weird
#even and inclusive range 6 - 20, print Weird
#even and greater than 20, print Not Weird

x = range(2, 5)
y = range (6, 20)

if n % 2 == 1:
    print("Weird")
else:
    if (n % 2 == 0 and x):
        print("Not Weird")
    elif (n % 2 == 0 and y):
        print("Weird")
    elif (n % 2 == 0 and n >= 20):
        print("Not Weird")
    else:
        exit

# BELOW IS THE CORRECT ANSWER

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
else:
    exit

 
