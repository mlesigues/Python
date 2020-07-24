#THIS WAS AN EASY CHALLENGE, I had to work OT and this is the only thing I can practice!
#I'll do something better next time!

#TASK:
#The provided code stub reads two integers, a and b, from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division, a/b.
#No rounding or formatting is necessary.

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

#integer division
result1 = int(a/b)
print(result1)

#float division
result2 = float(a/b)
print(result2)
