import time
import sys

class Test:
    def __init__(self):
        print("Object Initialization")

t1=Test()
t2=t1


print(sys.getrefcount(t1))
