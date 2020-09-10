#Task: Day:0 Weighted Mean from Hackerrank Statistics!
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = list(map(int,input().split(' ')))
W = list(map(int, input().split(' ')))
#int(X)
#int(W)
#formula for weighted mean is multiply every element of X and W with each other, then add
#them all then divide it by the sum of W
#formula: sum(Xi * Wi)/sum(Wi)

products = []
for elem in range(0, len(X)):
    products.append(X[elem] * W[elem])

sumAll = sum(products)
sum_W = sum(W)

total = sumAll/sum_W
final_weighted_mean = round(total, 1)
print(final_weighted_mean)
