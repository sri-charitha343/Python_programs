class Temperature:
    def __init__(self,temp):
        self.celsius = temp
    def show_conversion(self):
        print(self.celsius)
        print(Temperature.to_fahrenheit(self.celsius))
    @staticmethod
    def to_fahrenheit(celsius):
        fahrenheit = (celsius *(9/5) )+ 32
        return fahrenheit
T = Temperature(45)
T.show_conversion()