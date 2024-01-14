

string = input("Enter a string: ")
st = ""

for ch in string:
    if (ch.islower()):
        st += ch.upper()
    elif (ch.isupper()):
        st += ch.lower()
    else:
        st += ch

print(st)
