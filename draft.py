class Student:
    city = "Москва"

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def print_info(self):
        print(self.name, self.year)

v = Student('Вася', 19)
p = Student('Петя', 21)
Student.city = 'Питер'
v.print_info()
p.print_info()