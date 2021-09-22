#guess the number! Use of random
import random

def guess_game(num):
  print(f"Your guess number is {num}.")
  
  randNum = random.randint(1, num)
 
  if (num != randNum):
    if (randNum > num):
      print(f"Your guess is too low!")
      userInput = int(input("Guess again: "))
      guess_game(userInput)
    elif (randNum < num):
      print(f"Your guess is too high!")
      userInput = int(input("Guess again: "))
      guess_game(userInput)
  else: 
    print(f"You guessed the right number!")
  
#main 
user = int(input("Put a number: "))
guess_game(user)
