'''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*self.width + 2*self.length
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
square = Square(4)
print(square.area())'''
'''class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = Student("Wilbert", "Galitz", 2018)
print(x.graduationyear)'''
'''class Base1(object):
    def __init__(self):
        self.str1 = "Python"
        print("First Base class")
class Base2(object):
    def __init__(self):
        self.str2 = "Programming"
        print("Second Base class")
class Derived(Base1, Base2):
    def __init__(self):
        #Calling constructors of Base1
        #and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived class")
    def printStrs(self):
        print(self.str1, self.str2)
ob = Derived()
ob.printStrs()'''