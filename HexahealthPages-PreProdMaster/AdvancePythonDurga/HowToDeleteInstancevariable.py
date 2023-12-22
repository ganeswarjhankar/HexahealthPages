class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

    def delete(self):
        del self.b
        del self.c


##how to delete instance variables
#del self.variablename
#del objectreference.variablename


t1=Test()
#t1.delete()
del t1.a


t2=Test()
#t2.delete()
del t2.b
print(t1.__dict__)
print(t2.__dict__)

t3=Test()
t3.a=332
t4=Test()
t4.b=7474
print(t3.a,t3.b)
print(t4.a,t4.b)