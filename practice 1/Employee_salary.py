# Q7. Create a class Employee with:
# instance attributes: name, base_salary
# class variable: bonus_rate = 0.1
# instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# class method: update_bonus(cls, new_rate) → updates bonus for all employees
# static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.

class Employee:
    bonus_rate = 0.1
    def __init__(self,name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def final_salary(self):
        if Employee.is_valid_rate(self.base_salary):
            base_salary = self.base_salary + (self.base_salary * Employee.bonus_rate)
            print(base_salary)
        else:
            print("not valid")
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate = new_rate
    @staticmethod
    def is_valid_rate(sal):
        # if sal > 0:
        #     return True
        # else:
        #     return False
        return sal > 0

emp = Employee("charitha",50000)
emp.final_salary()
emp1 = Employee("Sri", 50000)
emp1.update_bonus(10)
emp1.final_salary()
