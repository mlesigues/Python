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
  
#============================================
  
#task 4: squares or more likely Squareception.

#reuse the code before but we will need to make a function or 
#a group of related statements that do a specific task when called
def squareCeption(userSize):
  count = 0
  while count < 4:
    turtle.forward(userSize)
    turtle.left(90)
    count = count + 1
    
    
#enter the "main" stuff below 
squareCeption(10)
squareCeption(30)
squareCeption(50)
squareCeption(70)

#============================================

#task 4: tilted squares. Hint: we will reuse the previous funtion that we did
#titled squares
#reuse the code before
def squareCeption(userSize):
  count = 0
  while count < 4:
    turtle.forward(userSize)
    turtle.left(90)
    count = count + 1
    

#enter the "main" stuff below 
turtle.left(10)
squareCeption(50)

turtle.left(20)
squareCeption(50)

turtle.left(30)
squareCeption(50)


#============================================
#can we change the colors? sure!
#we will change the pen color
turtle.pencolor("blue")

#then draw the square, just call the function!
squareCeption(50)

#task 5: draw the tilted squares but with different colors
#tilted square but with diffent squares
turtle.pencolor("red")
turtle.left(10)
squareCeption(50)

turtle.pencolor("blue")
turtle.left(20)
squareCeption(50)

turtle.pencolor("green")
turtle.left(30)
squareCeption(50)
turtle.pencolor("yellow")
