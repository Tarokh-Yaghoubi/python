
from array import *
b = array('i', [])
for i in range(11):
    x = int(input("Enter a number: "))
    b.append(x)

print(b)

for i in range(len(b)-1, -1, -1):
    print(b[i])
