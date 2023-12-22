import time

class Test:
    def __init__(self):
        print("Onject initialization")

    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities ")

list=[Test(),Test(),Test()]
time.sleep(10)
list=None
time.sleep(10)
print("end of application")
