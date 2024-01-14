

import os

multi = open("multi", "w")

for i in range(1, 11):
    for j in range(1, 11):
        multi.write(str(i * j))
        multi.write("\t")
    multi.write("\n")

multi.close()
