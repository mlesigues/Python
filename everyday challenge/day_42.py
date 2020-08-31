#Task: Mutation from Hackerrank
def mutate_string(string, position, character):
    #string = list(string)
    #string[position] = character
    #return ''.join(string)
    
    #can also do this:
    new_pos = position + 1
    string = string[:position] + character + string[new_pos:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

    
#Task: Nested Lists

if __name__ == '__main__':
    
    record = []
    lowest_name = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
        scores.add(score)

    #sort the grades, get the 1st index (not 0)
    lowest_score = sorted(scores)[1]

    #print(scores)
    #print(lowest_score)

    for name, score in record:
        if score == lowest_score:
            lowest_name.append(name)

    for name in sorted(lowest_name):
        print(name, end="\n")






        


