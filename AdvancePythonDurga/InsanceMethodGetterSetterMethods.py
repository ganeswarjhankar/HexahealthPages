class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.marks)



    def grade(self):
        if self.marks>=20:
            print("third class")

        elif self.marks>=50:
            print("2nd class")

        elif self.marks>90:
            print("First class")
        else:
            print("Failed")


