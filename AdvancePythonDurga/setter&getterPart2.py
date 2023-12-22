#Hiding data behind the methods ++++ ENCAPSULATION

#security method ----getter method





class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input("enter the student name:"))
for i in range(n):
    name=input("enter the name of student")
    marks=int(input("enter the marks"))
    s=Student()

    s.setName(name)
    s.setMarks(marks)

    print("Hi",s.getName())
    print("Your marks:",s.getMarks())




