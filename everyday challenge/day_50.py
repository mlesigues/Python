#Task: Day 4: Binomial Distribution I
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




#Task: Day 4: Binomial Distribution II
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

values = list(map(int,input().split(' ')))
n = values[1]

#p is 12%, so 12/100
p = 12/100


#a batch of 10 pistons will contain no more than 2 rejects
no_more_two = 0
for x in range(n):
    if x < 3:
        no_more_two += binom(x, n, p)
no_more_two = round(no_more_two, 3)
print(no_more_two)

#a batch of 10 pistons will contain at least 2 rejects
at_least_two = 0
for x in range(n):
    if x >= 2:
        at_least_two += binom(x, n, p)
at_least_two = round(at_least_two, 3)
print(at_least_two)

 
    
    
#Task: Day 4: Geometric Distribution I
defects = list(map(int,input().split(' ')))
n = int(input())

#geometric: g(n,p) = q^(n-1)*p
def geo(n, p):
    #q = (1-p)^(n-x), here x would be 1
    return (1-p)**(n-1)*p
    
p = defects[0]/defects[1]

res = geo(n, p)
res = round(res, 3)
print(res)




#Task: Day 4: Geometric Distribution II
defects = list(map(int,input().split(' ')))
n = int(input())

#geometric: g(n,p) = q^(n-1)*p
def geo(n, p):
    #q = (1-p)^(n-x), here x would be 1
    return (1-p)**(n-1)*p
    
p = defects[0]/defects[1]


#what is the probability that the 1st defect is found during the first 5 inspections
#so add p(1) + p(2) + ... p(5)
#note: this is okay for smaller inspections, but what if we have larger numbers?

find_defect = 0
for x in range(n+1):
    if x > 0:
        find_defect += geo(x, p) #note: instead of geo(n,p) it's geo(x, p)! why?
        
find_defect = round(find_defect, 3)
print(find_defect)
