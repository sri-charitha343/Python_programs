class Car:
    wheels = 4
    def __init__(self, mileage):
        self.mileage = mileage
    def display_specs(self):
        print(self.mileage,self.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels = new_wheels
        print("wheels",cls.wheels)
c = Car(450)
c.display_specs()
c1 = Car( 650)

c1.change_wheels(5)
c1.display_specs()