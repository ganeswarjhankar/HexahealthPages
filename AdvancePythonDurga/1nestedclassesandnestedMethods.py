def DOB():
    pass


class Person:
    def __init__(self):
        self.name="durga"
        self.dob=DOB()

    def display(self):
        print("Name is",self.name)
        self.dob.Display()


    class DOB:
        def __init__(self):
            self.dd=15
            self.mm=8
            self.yyyy=1947

        def Display(self):
            print("date of birth is :{}/{}/{}".format("dd","mm","yyyy"))

p=Person()
p.display()

