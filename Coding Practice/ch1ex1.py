#let's do it in python way, where we could do some shortcuts ==> make this into a function
#put "word" in a set to remove any duplicates
def noDups(word):
    storage = set()
    for letter in word:
        storage.add(letter)
    
    print(storage)
    
    if len(storage) == len(word):
        print("This is unique")
    else:
        print("This is not unique")

word = "cat"
noDups(word)
