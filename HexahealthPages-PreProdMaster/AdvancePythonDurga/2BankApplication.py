"""x=100  # static variable"""
class Test:
    x=777  ##static Variable
    def m1(self):
        x=888   ##local variable
        print(self.x)
        print(x)

    def m2(self):
        print(Test.x)
        print(x)

t=Test()
t.m2()

