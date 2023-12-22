"""Declaring variable inside class"""
class MyClass():
    a,b=100,200 #class variables #indorder to use these class variables
                # we must use Self keyword

    def add(self): #instance method
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)


mc=MyClass()  #Object Is Created  #Object Variables
mc.add()
mc.mul()