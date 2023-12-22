#Local Variable global variable and  Class variable


i,j=21,31 #Global Variable
class MyClass:
    a,b=10,20 # Class variable

    def add(self,x,y): # local variable
        print(x+y) # accessing the local Variable###300
        print(self.a+self.b)# accesing the Class variable  ##30
        print(globals()['i']+(globals()['j']))   #####52



mc=MyClass()
mc.add(100,200)




