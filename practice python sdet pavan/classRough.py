"""Static method and instance method"""
class Myclass():
    def m1(self):
        print("It is a instance method/variable")

    @staticmethod
    def m2(self):
        print("@static method ,static method")

mc=Myclass()
mc.m1()

Myclass.m2(10)

