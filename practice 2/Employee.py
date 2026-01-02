# Q3. Create an Employee class that:
# Keeps a minimum experience required for promotion (shared across all employees).
# Stores employee name, experience, and department.
# Has a method to check eligibility for promotion.
# Provides a function to update promotion criteria globally.
# Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.Creating employees from different departments.
# 2.Changing promotion criteria.
# 3.Displaying eligibility results and department validation.

class Employee:
    experience = 2
    def __init__(self,name,exp,department):
        self.name = name
        self.exp = exp
        self.department = department
    def check_eligibility(self):
        if Employee.is_department_valid(self.department):
            if self.exp >= Employee.experience:
                print("Name:",self.name)
                print("Experience:",self.exp)
                print("Department:",self.department)
                print("Status: eligible for promotion")
            else:
                print("Name:", self.name)
                print("Experience", self.exp)
                print("Department", self.department)
                print("Status: Not eligible for promotion")
        else:
            print("Not a valid department")
    @classmethod
    def change_criteria(cls,new_exp):
        cls.experience = new_exp
    @staticmethod
    def is_department_valid(dept):
        if dept == 'HR' or dept == "Admin" or dept == "Tech" or dept == "Sales":
            return True
        return False
e1 = Employee("charitha", 3, "Tech")
e1.check_eligibility()
print("____AFTER CHANGE____")
e1.change_criteria(5)
e1.check_eligibility()
