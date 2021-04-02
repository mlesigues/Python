'''
From Crack the Coding Interview (CTCI) Ch. 1 Arrays and Strings
Implement an algorithm to determine if a string has all unique characters. What if you can not
use additional data structures?
'''

def chars_unique(words):
    #read the given words, then identify their values using ord
    #since 'a' is not the same as 'A'
    #find if any of those values are repeating, we can use set and 
    #compare the length of set by the store_vals

    store_vals = []
    uniq = set()

    for letter in words:
        val = ord(letter)
        #after knowing the values, store those values
        store_vals.append(val)
        #also add on the set
        uniq.add(val)
    
    print (store_vals)
    #print(uniq)

    #now convert uniq into a list, then compare its length to store_vals
    uniq_l = list(uniq)
    print(uniq_l)
    if len(uniq_l) == len(store_vals):
        print("these characters are unique")
    else:
        print("these characters are not unique")

#tester func
def testing(string_input):
    chars_unique(string_input)


#call here
if __name__ == '__main__':

    words = ['b', 'B', 'a']
    testing(words)
    #chars_unique(words)