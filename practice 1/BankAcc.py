# Q9. Create a class BankAccount with:
# class variable bank_name
# instance variables holder and balance
# instance method deposit(amount)
# class method change_bank_name(cls, new_name)
# static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.

class BankAccount:
    bank_name = "HDFC"
    def __init__(self,holder,balance):
        self.name = holder
        self.balance = balance
        print("Holder Name:",holder, "Current balance:",balance)
    def deposit(self,amt):
        self.amt = amt
        print("Deposite Amount:",amt)
        if BankAccount.validate_amount(amt):
            balance = self.balance +amt
            print("Current Balance:",balance)
            print("Bank:",BankAccount.bank_name)
        else:
            print("less than 0 is not allowed")
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name
    @staticmethod
    def validate_amount(amt):
        if amt > 0:
            return True
        else:
            return False

acc = BankAccount("charitha",5000)
acc.deposit(250)

acc1 = BankAccount("sri",3000)
acc1.change_bank_name("SBI")
acc1.deposit(300)
