"""Instance method vs Class Method"""

#inside method body if we are usig only static variable then
#it is highly recommended to declare that method as class method

    #2.To declare instance method we are not reqired to use any decorator
    #To declare class method compulsory we should use @classmethod
    #3. The first argument to the instance method should be self ,which is reference to current object and by using self, we can access instance variable inside method


    #5. we can call instacne instance method object reference
    #5.1.we can call class method either using object reference
# or by using class name, but remended to use class name

class Animal:
    legs=4


    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))

Animal.walk("Dog")
Animal.walk("Cat")






