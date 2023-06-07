class Human:
     def __init__(self):
         self.name="Durga"
         self.head=self.Head()

     def display(self):
         print("Name:",self.name)
         self.head.talk()
         self.head.Brain.think(self)

     class Head:
         def __init__(self):
             self.brain=self.Brain()


         def talk(self):
             print("Talking...")

         class Brain:
             def think(self):
                 print("Thinking....")


h=Human()
h.display()
