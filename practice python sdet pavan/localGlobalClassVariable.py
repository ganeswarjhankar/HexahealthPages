#Local Variable global variable and  Class variable


i,j=21,31 #Global Variable
class MyClass:
    a,b=10,20 # Class variable

    def add(self,x,y): #local variable
        print(x+y) # accessing the local Variable
        print(self.a+self.b)# accesing the Class variable
        print(i+j)


mc=MyClass()
mc.add(100,200)




