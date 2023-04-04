class Employee:
    def __init__(self,eno,ename,esal): ##as self is added we can say
                                      # Instance variable
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):   # as firsd argument is self we can say that it is
                              # instance Method
        print("employee number",self.eno)
        print("employee name",self.ename)
        print("employee salary",self.esal)
class Test:
      #it isnt argument as self not instance method
                      #not classmethod as not @classmethod decorator
      @staticmethod
      def modify(emp):            #@staticmethod 100%
          emp.esal=emp.esal+10000
          emp.display()




e=Employee(32323,"durga",1000000)
Test.modify(e)



