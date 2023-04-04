class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
Test.x=888
t1.y=999
print(t1.x,t1.y)  #x=888,y=999
print(t2.x,t2.y)  #x=888, y=20
