#link: https://pythonprinciples.com/challenges/

#Python Challenge: Write a function named capital_indexes. The function takes a single parameter, which is a string. 
#Your function should return a list of all the indexes in the string that have capital letters.

def capital_indexes(userInput):
    res = []
    for ind, elem in enumerate(userInput):
        #print(ind, "==" ,elem)
        if (elem.isupper() == True):
            res.append(ind)
    return res
        
#main   
userInput = "HeLlO"
capital_indexes(userInput)
