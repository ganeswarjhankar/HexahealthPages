class MyClass:
    def m1(self):
        pass

c1=MyClass()
c2=MyClass()
c3 =c1
print(id(c1))
print(id(c2))
print(id(c3))

print(c1 is c2)
print(c1 is not c2)
