
from array import *

b = array('i', [])

for i in range(10):
    x = int(input("Enter a number: "))
    b.append(x)

smallest = min(b)
loc_smallest = b.index(smallest)
b.pop(loc_smallest)
smallest = min(b)
loc_smallest = b.index(smallest)
print(f"the second smallest number is {smallest}, its location is {loc_smallest}")
