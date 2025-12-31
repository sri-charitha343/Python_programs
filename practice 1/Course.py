# Q8. Create a class Course with:
# class variable total_students
# instance variable student_name
# instance method enroll() → increments total_students
# class method show_total(cls) → prints total students
# static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.

class Course:
    total = 0
    def __init__(self,name):
        self.name = name
    def enroll(self):
        Course.total += 1
    @classmethod
    def show_total(cls):
        print(cls.total)
    @staticmethod
    def is_eligible(age):
        if age >= 18:
            return True
        else:
            return False

s = Course("Charitha")
s.enroll()
s.show_total()

s1 = Course("Sri")
s1.enroll()
s1.show_total()

s2 = Course("Cherry")
s2.enroll()
s2.show_total()