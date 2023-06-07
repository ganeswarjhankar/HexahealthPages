class Person:
    def __init__(self,dd,mm,yyyy):
        self.name="Durga"
        self.dob=self.DOB(dd,mm,yyyy)

    def display(self):
        print("Name:",self.name)
        self.dob.display()


    class DOB:
        def __init__(self):
            self.dd=15
            self.mm=8
            self.yyyy=1947
        def display(self):
            print("Date of Birth:{}/{}/{}".format(self.dd,self.mm,self.yyyy))


p=Person()
p.display()
p.dob.display()













