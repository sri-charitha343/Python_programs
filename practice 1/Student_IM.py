class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if self.marks>40:
            return True
        else:
            return False
Std = Student("Charitha", 90)
Std1 = Student("Sri", 30)
print(Std.is_passed())
print(Std1.is_passed())
n