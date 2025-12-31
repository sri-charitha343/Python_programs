class MathOps:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
    def even_im(self,num):
        if MathOps.is_even(num):
            print("even_im")
        else:
            print("odd_im")
    @classmethod
    def even_cm(cls,num):
        if cls.is_even(num):
            print("even_cm")
        else:
            print("odd_cm")
n = MathOps()
n.even_im(20)?""
n.even_cm(61)
n1 = MathOps()
n1.even_im(33)
n1.even_cm(66)





