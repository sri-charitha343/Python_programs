# Q10. Create a class Student with:
# class variable passing_marks = 40
# instance attributes name, marks
# instance method result() → prints pass/fail using class variable
# class method update_passing_marks(cls, new_marks)
# static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.Creates students
# 2.Updates the passing criteria
# 3.Displays grade category and result

class Student:
    passing_marks = 40
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= Student.passing_marks:
            print("pass")
        else:
            print("fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks = new_marks
    @staticmethod
    def grade_category(marks):
        if marks > 80 or marks <= 100:
            return "A"
        elif marks > 40 or marks <= 79:
            return "B"
        else:
            return "C"

s1 = Student("Chariths", 78)
s2 = Student("Sri", 35)
s3 = Student("Cherry", 62)

print(s1.name,"Grade ->", Student.grade_category(s1.marks))
s1.result()

print(s2.name, "Grade ->",Student.grade_category(s2.marks))
s2.result()

print(s3.name,"Grade ->", Student.grade_category(s3.marks))
s3.result()

Student.update_passing_marks(50)
print("\nafter updation")
s1.result()
s2.result()
s3.result()

