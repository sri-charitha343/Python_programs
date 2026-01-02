# Q2. Design a class Product that:
# Maintains a base tax rate applicable to all products.
# Each product has a name and base price.
# Has a method to compute final price including tax.
# Can change tax rate for all products using one method.
# Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.Creating multiple products.
# 2.Changing the tax rate.
# 3.Showing updated prices and validity checks.
class Product:
    tax = 5
    def __init__(self,name,base_price):
        self.name = name
        self.base_price = base_price
    def final_price(self):
        if Product.is_valid_price(self.base_price):
            print("Product name:",self.name)
            final_price = self.base_price + (self.base_price * Product.tax / 100)
            print("Product Price",final_price)
        else:
            print("Not a valid Price")
    @classmethod
    def change_tax_rate(cls,new_tax):
        cls.tax = new_tax
    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        return False

p1 = Product("bread",50)
p1.final_price()
print("______AFTER CHANGE_______")
p1.change_tax_rate(10)
p1.final_price()