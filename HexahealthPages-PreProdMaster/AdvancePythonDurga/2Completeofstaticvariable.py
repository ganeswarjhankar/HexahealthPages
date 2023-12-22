"""What are hte various place the static variable can be declared"""

##within the class directly but from outside of any method
##Insid constructor by using classname
#Inside hte instance method by using Clssname
##inside classmthod  by usng cls vaiable or classname
##inside stactic method by using class name
##outside of claas using class name

class Test:
    a=10
    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c=30

    @classmethod
    def m2(cls):
        cls.d=32
        Test.e=44
    @staticmethod
    def m3():
        Test.f=54


t=Test()
t.m1()

Test.g=70
print(Test.__dict__)

