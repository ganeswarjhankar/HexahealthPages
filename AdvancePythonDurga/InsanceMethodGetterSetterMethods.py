###class methods and Static methods

#instance methods:
#def m1(self):
#    we are using instance variables
#by using self
#object reference

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("hi",self.name)
        print("Hi",self.marks)


    def grade(self):
        if self.marks>=60:
            print("pass first")
        elif self.marks<=40:
            print("2nd class mark")

        else:
            print("Fail")

n=int(input("enter number of students:"))
for i in range(n):
    name=input("Enter Student Name")
    marks=int(input("enter marks"))
    s=student(name,marks)
    s.display()
    s.grade()




