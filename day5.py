#TASK: 
#The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following:
#123...n (without whitespaces in between)
#for example, n = 5 => 1235. Constraints: 1 <= n <= 150.

if __name__ == '__main__':
    n = int(input())

    #using python 3
    #create a for loop that starts from the beginning and ends in N+1
    #the end="" prints the number without new lines after each other
    for i in range(1, n+1):
        print (i, end="")
