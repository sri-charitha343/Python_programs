class Employee:
    company_name = "TechCorp"
    def __init__(self,name):
        self.name=name
    def employee(self):
        print(self.name,self.company_name)
    @classmethod
    def change_company(cls,new_name):
        cls.company_name = new_name
        print(cls.company_name)
emp = Employee("charitha")
emp1 = Employee("sri")
emp.change_company("CVCorp")
emp.employee()
emp1.change_company("CV")
emp1.employee()


