#function that accepts two inputs and return true
#if the first input is greater than the second input
#otherwise, return False

def larger_funct(userInput_1, userInput_2):
  #userInput_1 = int(input("Enter 1st number: "))
  #userInput_2 = int(input("Enter 2nd number: "))

  if userInput_1 > userInput_2:
    print(userInput_1, " is greater than ", userInput_2)
    print("this is true")
    return True
  else:
    print(userInput_2, " is not greater than ", userInput_1)
    print("this is false")
    return False


#call function
larger_funct(55, 67)
larger_funct(1523, 978)
larger_funct(89, 98)
