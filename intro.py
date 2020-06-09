#introduction to python

#print function = it prints anything you put on inside the parentheses. Ex:
print ("Hello, World")
print ("Hello, my name is Ate Marielle")

#indentation is very important. It tells the compiler which block of codes belong together, 
#if you misplace/skip an indentation, your code might cause an error or it might do something 
#else. Ex:
def my_function():
  print("this is the my_function") 

my_function()

#this will cause an error, why?
#def my_function2():
#print("this is my_function2")

#variable = reserves a space in the computer memory. Ex:
x = 1
y = 'dog'

#comments = a good habit to practice when coding because it makes reading/
#understanding what each block of your code does. To put a comment, use '#'
#then put your comments after

#Data Types = they are used alongside the variables. Different data types do 
#different things. Python has the following default data types:
    #Text type = str
    #Numeric types = int, float, complex
    #Sequence types = list, tuple, range
    #Mapping type = dict
    #Set types = set, frozenset
    #Boolean type = bool
    #Binary types = bytes, bytearray, memoryview

#Focus: 3 numeric types
#int or integer is a whole number, positive or negatice with unlimited length.
#Ex:
var1 = 3
var2 = 10
print (var1)
print (var2)
#float or floating decimals is a number, positive or negative, containing one or 
#more decimals. Ex:
var3 = 3.45
var4 = 5.9833
print(var3)
print(var4)
#complex will be skipped because it is used for mathematical equations

#Strings = can be printed using the print function surrounded with either a single 
#or double quotation marks. Can also assign a string to a variable. Ex:
stringVar = "hello, world"
print(stringVar)

#can also combine/concatenate two strings using the "+" operator. Ex:
stringVar1 = "hello!"
stringVar2 = "world"
print(stringVar1 + stringVar2)


