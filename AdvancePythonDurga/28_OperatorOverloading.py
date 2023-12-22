#class
#object
#reference
#types of variables
#type of methods
#constructors
#self variable
#inner classes
#how to access members of one class from other class
#GC and destructors
#Polymorphism:
#Duck Typing philosophy of Python
#overloading
#Operator Overloading



class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages

    def __sub__(self, other):
        return self.pages-other.pages

    def __mul__(self, other):
        return self.pages*other.pages

    def __divmod__(self, other):
        return self.pages%other.pages

    def __floordiv__(self, other):
        return self.pages




b1=Book(100)
b2=Book(200)
print(b1+b2)
print(b1-b2)
print(b1*b2)
print(b1 )
print(b1)
print(b2)




















