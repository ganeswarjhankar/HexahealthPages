class Duck:
    def talk(self):
        print("Duck Talks")

class cat:
    def talk(self):
        print("Cat Talks")
class Goat:
    def talk(self):
        print("Goat Talks")

def f1(obj):
    obj.talk()


def ganesh():
    def talk():
     pass


I=[Duck(),Goat(),cat(),ganesh()]
for obj in I:
    f1(obj)