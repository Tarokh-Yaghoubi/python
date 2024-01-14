
class student:
    number = 0.0
    name = ""
    avg = 0.0

    def say_hello(self):
        print(f"hello from {self.name}")

    def select_lesson(self):
        return "Test Student"

    def __str__(self):
        string = f"Name is {self.name}, number is {self.number},\navg is {self.avg}"
        return string


student_1 = student()

student_1.name = "tarokh"
student_1.number = 9105664867
student_1.avg = 17.75
student_1.say_hello()
print(student_1.select_lesson())
print(str(student_1))
