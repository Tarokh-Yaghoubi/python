
def countWord(char, string):
    count = 0
    for c in string:
        if (c == char):
            count += 1

    return count

string = input("Enter a string: ")
char = ' '
num = countWord(char, string) + 1
print(num)
