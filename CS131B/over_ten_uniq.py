'''
Write a program that shows ten unique random words, all over ten characters long, that occur in the text 
/users/.../.../urantia.txt
'''
# -*- coding: utf-8 -*-
import string
import random
    
#function that split the text into words, then put them in a set to remove duplicates
def split_text(fhand):
    counts = dict()
    for line in fhand:
        line = line.rstrip().strip() #remove newlines and whitespaces
        line = line.translate(line.maketrans('', '', string.punctuation)) #remove punctuations
        line = line.lower()
        words = line.split() #or split(' ') ?
        for word in words: #counting word occurrence
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

    uniq_words = set() #put words in the set so it'll remove the duplicates
    for key, value in counts.items(): #key contains the actual words
        #before we add words, we need to make sure that it is a string, NOT AN INTEGER/FLOAT
        if isinstance(key, int): #if the word is an int, remove it on the set
            uniq_words.remove(key)
        else:
            uniq_words.add(key)
    
    return uniq_words
    
#validates if a word is >= 10 characters
def ten_chars_long(uniq_words):
    valid_words = [] #contains the more than or equal to 10 character words
    for element in uniq_words:
        char_len = len(element) #looks for the character length
        if char_len >= 10: #checks if the word has >= 10 words
            valid_words.append(element) #put the WORD in the list
    
    return valid_words

#shows 10 random unique 10-character words
def random_words(valid_words):
    #only show 10 random words from the word_len list (we can use random funct here)
    rand_words = random.sample(valid_words, 10)

    # Remove square brackets from list using str() + list slicing
    #src: https://www.geeksforgeeks.org/python-remove-square-brackets-from-list/
    final_words = str(rand_words)[1:-1]


    #print("Here are the 10 random unique words: ",rand_words)
    print("Here are the 10 random unique words: ",final_words)


if __name__ == '__main__':
    #open file
    fname = '/users/.../.../urantia.txt'
    try:
        fhand = open(fname)
        print("File is now open.")
    except:
        print('File cannot be opened:', fname)
        exit()
    
    #call functions
    words = split_text(fhand)
    #print(res)
    valid = ten_chars_long(words)
    random_words(valid)

    fhand.close()
    print("The file is now closed.")

