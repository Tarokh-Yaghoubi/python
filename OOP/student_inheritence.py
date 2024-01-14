

class Person:
    def __init__(self, firstname, lastname, birth):
        self.firstname = firstname
        self.lastname = lastname 
        self.birth = birth

    def test(self):
        print(f"I am a person, my name is {self.firstname}")

    def __del__(self):
        print(f"Good by dear student {self.firstname}")

    def __str__(self):
        string = f"Firstname is : {self.firstname}\nLastname is {self.lastname}\n birth: {self.birth}"
        return string 


class Student(Person):

    def test(self):
        super().test()
       # print("I am a student")

    def __init__(self, firstname, lastname, birth, code, programmingLang):
        super().__init__(firstname, lastname, birth)
        self.code = code
        self.programmingLang = programmingLang

    def __str__(self):
        string = super().__str__()
        string += f"\n Code is {self.code}\n programming language is : {self.programmingLang}"
        return string


st = Student("Tarokh", "Yaghoubi", 2004, 88679, "C/JS/C++")
st.test()
print(st)

