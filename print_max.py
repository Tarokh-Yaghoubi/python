

from array import *

b = array('i', [])

for i in range(5):
    x = int(input("Enter a number: "))
    b.append(x)

mx = max(b)
loc = b.index(mx)

print(f"{mx} has location {loc}")
