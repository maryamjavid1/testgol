'''
# To Do: Insert here some words about this project
'''


class daneshjo:
    def __int__(self, fname, lname, field, code, grade):
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
        return

