#TASK: LIST COMPREHENSIONS! YOU ARE GIVEN THREE INTEGERS x, y, and z
#REPRESENTING THE DIMENSIONS OF A CUBOID ALONG WITH AN INTEGER n. PRINT
#A LIST OF ALL POSSIBLE COORDINATED GIVEN BY (i,j,k) ON A GRID 3D WHERE
#THE SUM OF i+j+k IS NOT EQUAL TO n. HERE, 0<=i<=x; 0<=j<=y, o<=k<=z. USE
#LIST COMPREHENSIONS RATHER THAN MULTIPLE LOOPS.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    #need to list all permutations of x,y,z using list
    # for i in range(x+1):
    #     print(x)
    #     for j in range(y+1):
    #        print(y)
    #         for k in range(z+1):
    #             if(i+j+k != n):
                    
    #                 print([i,j,k],end="")

    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

  #TASK: YOU ARE GIVEN A STRING. SPLIT THE STRING ON A " "(space) DELIMETER AND JOIN USING A "-" hypen.
def split_and_join(line):
        # write your code here
    newSplit = line.split(" ") #split by space delimeter
    newJoin = "-".join(newSplit) #join by hypen

    return newJoin


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)