#InnerClass
#1.The class which is declared inside another class is called inner class
#2.Without existing one type of object if there is no chance of existing another
#type of object then we should go for inner class
#3.
#car and Engine

class Outer:
    def __init__(self):
        print("Outer class object creation...")
    class Inner:
        def __init__(self):
            print("Inner class object creation...")

        def m1(self):
            print("Inner class method")
o=Outer()
i=o.Inner()
i.m1()


#or we can use as
#            Outer().Inner().m1()






