#How to modfy the Static variable
#within the class we should use classname, cls variable
# from outside the clasas

class Test:
    a=10
    def __init__(self):
        Test.a=20


    @classmethod
    def m2(cls):
         cls.a=30
         Test.a=40
    @staticmethod
    def m3():
        Test.a=50

t=Test()
t.m2()
t.m3()
t.a=60 ## instance varible
print(Test.a)
print(t.a)
print(t.a)





