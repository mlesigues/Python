#Write a code to reverse a C-style string. This means that "abcd" is represented as 5 characters.

store = ['a', 'b', 'c']

rev = store[::-1] #string reversal
res = len(rev) + 1 #added plus 1 because that will act as the count for the null character

print(rev)
print(res)
