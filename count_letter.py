

def countLetter(char, string):
    count = 0
    for c in string:
        if (c == char):
            count += 1
    return count

string = input("Enter a string: ")
char = input("Enter a character: ")
print(countLetter(char, string))
