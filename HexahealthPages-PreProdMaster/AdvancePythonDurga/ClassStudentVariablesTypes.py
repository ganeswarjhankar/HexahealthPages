class Students:

    cname="Class level variable /static variable"

    def __init__(self,x,y):  #local variable/method variable
        self.instancevariable1=x
        self.instancevariable2=y

    #@instancemethod
    def display(self):
        methodvariable1=10
        methodvariable2=42

    @classmethod
    def getCollegeName(cls): #class
        print("college name",cls.cname)

#idont want to use class level data or Object level data then see the next data
    # using static method
    @staticmethod
    def findaverage(x,y):
        print("average:",(x+y)/2)

s1=Students("durga",100)
s1.findaverage(10,20)
