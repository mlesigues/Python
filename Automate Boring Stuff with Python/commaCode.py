#comma code 
#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. Test for any list value and empty list

def commaAnd(listName):
  #we need to check if the argument is an empty list or not 
  if len(listName) == 0:
    return listName
  elif len(listName) == 1:
    return listName[0]
  else:
    #the list will be modified, so add an extra empty element 
    #need to put 'and' before the last element
    listName.insert(-1, 'and')
    #print(listName)


  #converting the list into string
  temp = ' '
  return (temp.join(listName))
  


#x = ['apples', 'bananas', 'tofu', 'cats']
x = ['apples']
print(commaAnd(x))
