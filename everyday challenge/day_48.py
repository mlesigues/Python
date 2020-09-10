#Task: Day: 0 Weighted Mean from Hackerrank Statistics!
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


#Task: Day: 1 Quartiles from Hackerrank Statistics!
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
num_of_elems = int(input())
X_arr = list(map(int, input().split(' ')))

#sort the elements
X_arr.sort()
#print(X_arr)
#if odd number of elements, the middle element (median) would be Quartile 2
#then remove it(?) to calculate 1st and 3rd Quartile
#if even number of elements, split equally and calculate 1st and 3rd Quartile, the 2nd Quartile is the median

#even elements
if num_of_elems % 2 == 0:
    split_left = X_arr[:len(X_arr)//2] #get the left half of the total array
    split_right = X_arr[len(X_arr)//2:] #get the right half of the total array
    
    q1_mid = split_left[int(len(split_left)/2)] #get the median (mid val) in this sublist
    
    #q1_after_mid = split_left[int(len(split_left)/2-1)]
    #print(q1_after_mid)
    #q1 = math.ceil((q1_mid + q1_after_mid)//2)
    q2 = (split_left[-1] + split_right[1])//2
    q3_mid = split_right[int(len(split_right)/2)]
    
    q3_before_mid = split_right[int(len(split_right)/2-1)]
    q3 = math.ceil((q3_before_mid+q3_mid)/2)

    print(q1_mid)
    print(q2)
    print(q3)
else:
    #odd elements
    q2 = X_arr[int(len(X_arr)/2)] #quartile 2

    split_left = X_arr[:len(X_arr)//2] #this is flooring (so round down)
    split_right = X_arr[len(X_arr)//2 + 1:] #added '+1' because it reads the mid val
    q1_mid = split_left[int(len(split_left)/2)]
    q1_before_mid = split_left[int(len(split_left)/2-1)]
    q1 = (q1_mid + q1_before_mid)//2
    q3_mid = split_right[int(len(split_right)/2)]
    q3_before_mid = split_right[int(len(split_right)/2-1)]
    q3 = (q3_before_mid + q3_mid)//2

    print(q1)
    print(q2)
    print(q3)


