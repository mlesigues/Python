#Task: String Validators from Hackerrank
if __name__ == '__main__':
    s = input()

    """
    for elem in s:
        #if any(elem == elem.isalnum()):
        #    print(elem.isalnum())
        any(s.isalnum())
        if elem == elem.isalpha():
            print(elem.isalpha())
        if elem == elem.isdigit():
            print(elem.isdigit())
        if elem == elem.islower():
            print(elem.islower())
        if elem == elem.isupper():
            print(elem.isupper())
        """

    print(any(elem.isalnum() for elem in s))
    print(any(elem.isalpha() for elem in s))
    print(any(elem.isdigit() for elem in s))
    print(any(elem.islower() for elem in s))
    print(any(elem.isupper() for elem in s))
