# Q1. Create a class Student that:
# Keeps track of the total number of students created.
# Determines whether a student passed or failed based on a shared passing mark.
# Provides a method to curve marks by increasing everyone’s marks by a percentage.
# Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# Demonstrate:
# 1.Creating multiple students.
# 2.Applying a grading curve.
# 3.Displaying updated results with letter grades.

class Student_marks:
    total = 0
    shared_pass_mark = 50
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student_marks.total += 1
    @staticmethod
    def is_passed(marks):
        if marks >= Student_marks.shared_pass_mark:
            return True
        return False