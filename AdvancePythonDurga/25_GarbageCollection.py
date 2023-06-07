import time


class Test:
    def __init__(self):
        print("Constructor Execution ")

    def __del__(self):
        print("destructor execution")

t1=Test()
t2=t1
t3=t2

del t1
time.sleep(10)
print("object not yet destroyed t1")
del t2
time.sleep(10)
print("object not destroyed after deleting t2 also")



time.sleep(10)
print("object  destroyed after deleting last reference ")
del t3
print("end of statement")
