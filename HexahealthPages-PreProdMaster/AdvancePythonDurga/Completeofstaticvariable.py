class Student:
    cname="DurgaSoft"   ####statc variable

    def __init__(self,name,rollno):
        self.name=name    #instance variable
        self.rollno=rollno  ### instance variable


s1=Student("Durga",32)
s2=Student("ganesh",43)
print(s1.name,s1.rollno,s1.cname)
print(s2.name,s2.rollno,s2.cname)