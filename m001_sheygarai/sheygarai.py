'''
# ToDo: Insert here some words about this project
'''


class Student:
    def __init__(self):
        self.fname = input('enter your fname = ')
        self.lname = input('enter your lname = ')
        self.field = input('enter your field = ')
        self.code = int(input('enter your code = '))
        self.grade = float(input('enter your grade = '))

    def __str__(self):
        return f'daneshjoo name : {self.fname} {self.lname}'

    def is_fail(self):
        return False if self.grade >= 12 else True


my_students = []
for i in range(3):
    i = Student()
    my_students.append(i)

for std in my_students:
    if std.is_fail():
        print(std)