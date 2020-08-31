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
