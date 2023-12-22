#Whenever we are calling the + operator then __add__() method will be called
#whenever we are printing Book object reference then __str__() method will be called



class Book:
    def __init__(self,pages):
        self.pages=pages

    def __str__(self):
        return "the number of pages "+str(self.pages)

    def __add__(self, other):
        total=self.pages+other.pages
        b=Book(total)
        return b



b1=Book(100)
b2=Book(200)
b3=Book(200)
b4=Book(121)

print("The total number of pages:",b1+b2+b3+b4)


