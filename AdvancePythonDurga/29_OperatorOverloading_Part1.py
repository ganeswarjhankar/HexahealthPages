class Book:
    def __init__(self,pages):

        self.pages=pages

    def __str__(self):
        return "the number of pages :"+str(self.pages)

    def __add__(self, other):

        total=self.pages+other.pages
        b=Book(total)
        return b

    def __mul__(self, other):

        total=self.pages+other.pages
        b=Book(total)
        return b


b1=Book(100)
b2=Book(323)
print(b1+b2)

print(b1*b2)





