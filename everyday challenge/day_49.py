#Task: Day 1: Interquartile Range from Hackerrank Statistics
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_elems = int(input())
#X_arr = [int(i) for i in input().split(' ')]
X_arr = list(map(int,input().split(' ')))
F_arr = list(map(int,input().split(' ')))
S = []

#first, create data set S
for elem in range(0, num_of_elems): #getting indices here of the X_arr
    for freq in range(0, F_arr[elem]):
        S.append(X_arr[elem])

S.sort()


def median(elements_list):
    i = len(elements_list)
    #even
    if i % 2 == 0:
        return (elements_list[(i//2 - 1)] + elements_list[(i//2)]) / 2
    else: #odd
        return (elements_list[(i//2)])


#even data set, S
if len(S) % 2 == 0:
    lower_half = S[:len(S)//2]
    upper_half = S[len(S)//2:]
    
    """
    mid_lower_half = lower_half[int(len(lower_half)/2)]
    before_lower_half = lower_half[int(len(lower_half)/2 - 1)]
    mid_upper_half = upper_half[int(len(upper_half)/2)]
    after_mid_upper_half = upper_half[int(len(upper_half)/2 - 1)]
    
    q1 = (mid_lower_half + before_lower_half)/2
    q3 = (after_mid_upper_half + mid_upper_half)/2
  
    interquartile = q3 - q1
    interquartile = round(interquartile, 1)
    
    print(interquartile)
    """
    
    q1 = median(lower_half)
    q3 = median(upper_half)

else:
    lower_half = S[:len(S)//2]
    upper_half = S[len(S)//2+1:]
    q2 = S[len(S)//2]
    
    """
    mid_lower_half = lower_half[int(len(lower_half)/2)]
    before_lower_half = lower_half[int(len(lower_half)/2 - 1)]
    mid_upper_half = upper_half[int(len(upper_half)/2)]
    after_mid_upper_half = upper_half[int(len(upper_half)/2 - 1)]

    q1 = (mid_lower_half + before_lower_half)//2
    q3 = (mid_upper_half + after_mid_upper_half)//2

    interquartile = q3 - q1
    interquartile = round(interquartile, 1)

    print(interquartile)
    """

    q1 = median(lower_half)
    q3 = median(upper_half)

interquartile = float(q3 - q1)
#interquartile = round(interquartile, 1)
print(interquartile)

