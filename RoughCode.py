
class Myclass():
    def m1(self):
        print("It is a instance method/variable")

    @staticmethod
    def m2():
        print("@static method ,static method")

mc=Myclass()
mc.m1()

Myclass.m2()

