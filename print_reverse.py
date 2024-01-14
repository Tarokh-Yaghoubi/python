

import os

number = int(input("Enter a number: "))

while (number > 0):
    print(number % 10, end="")
    number //= 10

print()
