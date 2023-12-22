class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("hello",self.name)    #instance variable sa self is used
        print("My roll no",self.rollno)


s=Student("durga",33)
s.display()

print(s.name,s.rollno)

s1=Student("ravi",43)
s1.display()

print(s1.name,s1.rollno)
