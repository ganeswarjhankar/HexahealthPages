class Test:
    a=10
    def __init__(self):
        print("Inside Constructor")

        print(Test.a)
        print(self.a)

    def m1(self):
        print("Inside Instance Method")
        print(Test.a)
        print(self.a)

    @classmethod
    def m2(cls):
        print("inside Class method")
        print(Test.a)
        print(cls.a)

    def m3():
        print("Inside Static Method")
        print(Test.a)



obj=Test()
obj.m1()
obj.m2()
obj.m3()
