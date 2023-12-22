class Person:
    def __init__(self):
        self.name="ganeswar"
        self.dob=self.DOB()

    def display(self):
        print("Name",self.name)
        self.dob.Display()
    class DOB:
        def __init__(self):
            self.dd = 20
            self.mm = 4
            self.yyyy=1991

        def Display(self):
            print("DOB={}/{}/{}".format(self.dd,self.mm,self.yyyy))

p=Person()
p.display()