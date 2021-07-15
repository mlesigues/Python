#the following code produces the word "HI" in brute force
"""
import turtle

turtle.penup()
turtle.backward(100)
turtle.penup()
turtle.left(90)
turtle.pendown()
turtle.forward(100)
turtle.left(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.pendown()
turtle.forward(100)

turtle.penup()
turtle.left(90)
turtle.forward(50)

turtle.left(90)
turtle.pendown()
turtle.forward(100)
""""
#============================================

#Important step: import the turtle module
import turtle

#task 1: draw a square. How? Remember that a square has equal sides or in nerdy math: square has 90 degrees sides!

#step 1: draw a line
turtle.forward(50)

#step 2: change the "cursor" direction. Turn left?
turtle.left(90)

#step 3: so now, we're on the right direction. We can move forward.
turtle.forward(50)

#step 4: repeat step 2.
turtle.left(90)

#step 5: repeat step 3.
turtle.forward(50)

#step 6: repeat step 2.
turtle.left(90)

#step 7: repeat step 3.
turtle.forward(50)

#============================================

#task 2: draw a square BUT use LOOPS!
count = 0
while count < 4:
  turtle.forward(50)
  turtle.left(90)
  count = count + 1
  
#============================================

#task 3: draw a rectangle. Length = 100, Width = 50.
count = 0

while count < 2: #if we don't put 2 here, just 1 it only makes an "L" shape
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(50)
  turtle.left(90)
  count = count + 1
  
