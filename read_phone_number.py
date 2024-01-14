
people = open("people", "w")

count = 1;

while (count <= 3):
    name = input("Enter your name: ")
    phone = input("Enter your phone: ") 
    s = name + '\t' + phone + '\n'
    people.write(s)
    count += 1

people.close()


