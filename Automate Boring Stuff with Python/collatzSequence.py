#collatz sequence

def collatz(number):
  if number % 2 == 0:
    #even
    #return print(number//2)
    print (number//2)
    return (number//2)
  if number % 2 == 1:
    #odd
    #return print(3 * number + 1)
    print (3 * number + 1)
    return (3 * number + 1)


#modify: Add try and except statements; In the except clause, print a message to the user saying they must enter an integer.
try:
  user = input("enter a number: ")
  while user != 1:
    user = collatz(int(user))
except ValueError:
  print("Invalid input. Enter only integers.")



