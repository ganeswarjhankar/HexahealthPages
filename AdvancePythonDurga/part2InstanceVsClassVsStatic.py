#To track number of objects for a class
class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def getNoOfObjects(cls):
        print("The number of objects created :",Test.count)

t1=Test()
t2=Test()
t3=Test()
t4=Test()
t5=Test()
Test.getNoOfObjects()
