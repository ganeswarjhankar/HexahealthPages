class Employee:
    """DocString Description"""
    print(__doc__)
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def info(self):
        print("Employee number", self.eno)
        print("Employee name", self.ename)
        print("Employee sal", self.esal)
        print("Employee address", self.eaddr)

e1=Employee(100,1200000,"Ganeswar","Gurugram")
e2=Employee(100,"Ganeswar",1200000,"Gurugram")
e1.info()
e2.info()



