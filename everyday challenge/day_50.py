#Task: Binomial Distribution I
#factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

#combinations: n! / x! (n-x!)
def comb(n, x):
    return fact(n)/(fact(x)*fact(n-x))


#binomial: combinations * p^x * q^(n-x); q = 1-p therefore (1-p)**(n-x)
#note: exponention is '**'
def binom(x,n,p):
    return comb(n, x) * (p**x) * (1-p)**(n-x)


values = list(map(float,input().split(' ')))
n = 6 #n is total # of trials

#p is basically like this:
#P(having boy) = P(boy)/1+P(boy) = 1.09/1+1.09 = 1.09/2.09
p = values[0] / (values[1] + values[0])

res = 0
#for x, we need to use 3, 4, 5, 6 (because it says at least 3 boys)
for x in range(3, 7): #3-7 because it'll loop 4 times
    res += binom(x,n,p)
res = round(res,3)
print(res)
