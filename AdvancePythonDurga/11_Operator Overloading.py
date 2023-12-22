"""Overloading > and <= operators for teh student class"""
class students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __gt__(self, other):
        return self.marks>other.marks


s1=students("Durga",100)
s2=students("shiva",200)
print(10>20)

