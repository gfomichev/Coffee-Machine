class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + birth_year


_name = input()
_last_name = input()
_birth_year = input()
student = Student(_name, _last_name, _birth_year)

print(student.id)
