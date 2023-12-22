class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def info(self):
        self.marks=60      #instance variable sa self is used
                   #local varaible inside a method

#####where we can declare instance variable
#####inside constructor by using self
#####Inside instance method by using self
#####from outside of the class by using the object reference

#3 instance variable
s2=Student("pavan",322)
s2.wife="renu"
print((s2.__dict__))


#4instance variable
s1=Student("ganesh",100)
s1.info()
s1.age=24
print(s1.__dict__)
