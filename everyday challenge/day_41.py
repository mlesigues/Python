#Task: Find the Percentage from Hackerrank
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    #some strategies:
    #know what the query name is, so we can quickly find it in the dict
    #student_marks is already contained
    #maybe use get()? nvm, use items()
    #src: https://www.w3schools.com/python/python_dictionaries.asp
    #src: https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops

    for name, score in student_marks.items():
        #print("{0} corresponds to {1}".format(name, score))
        
        #compare name and query_name to find which student needs an average
        if name == query_name:
            #get sum of scores, then divide by 3
            avg = sum(score) / 3
            print ('{:0.2f}'. format(avg)) #2 decimal places

            
            
#Task: Lists from Hackerrank
if __name__ == '__main__':
    N = int(input())

    #NOTE: poorly worded, kind of confusing on how to start at first
    #read the first word to match the commands, use split()

    res = []

    for elem in range(N):
        #split to get the commands; make sure to only read the str arguments
        com = input().strip().split(" ")
        
        if com[0] == "insert":
            res.insert(int(com[1]), int(com[2]))

        elif com[0] == "print":
            print (res)

        elif com[0] == "remove":
            res.remove(int(com[1]))

        elif com[0] == "append":
            res.append (int (com[1]))

        elif com[0] == "sort":
            res.sort()

        elif com[0] == "pop":
            res.pop()

        else:
            #do reverse
            res.reverse()
        
        
#Task: Tuples from Hackerrank
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    #convert the integer_list into a tuple
    t = tuple(integer_list)

    #do the hash
    res = hash(t)

    print (res)
      




    
