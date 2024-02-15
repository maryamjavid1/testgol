'''
# ToDo: Insert here some words about this project
'''


class Student:
    def __init__(self, fname, lname, field, code, grade):
        self.fname = fname
        self.lname = lname
        self.field = field
        self.code = code
        self.grade = grade

    def set_info(self, fname, lname, field, code, grade):
        self.fname = fname
        self.lname = lname
        self.field = field
        self.code = code
        self.grade = grade

    def readALL(self):
        self.fname = input("name khodra vared konid:")
        self.lname = input("name khanevadegi:")
        self.field = input("reshte:")
        self.code = int(input("shomare daneshjoi:"))
        self.grade = int(input("term chand:"))

    def __str__(self):
        return f"daneshjo neme: {self.fname + ' ' + self.lname}\n daneshjo code:{self.code}\n daneshjo field:{self.field}"

    def is_fail(self):
        grade = self.grade
        return (False if grade >= 12 else True)

s1 = Student('mrym', 'javid', 'computer', 12, 16.5)
s2 = Student('Non', 'Non', 'Non', 0, 0)

fname = input("esm:")
lname = input("famil:")
field = input("reshte:")
code = int(input("cod"))
grade = float(input("nomre:"))

s2.set_info(fname, lname, field, code, grade)
s3 = Student('Non', 'Non', 'Non', 0, 0)
s3.readALL()

print("\n------------------\n")
if s1.is_fail():
    print(s1)
    print("\n------------------\n")
if s2.is_fail():
    print(s2)
    print("\n------------------\n")
if s3.is_fail():
    print(s3)





