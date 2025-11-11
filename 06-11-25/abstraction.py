# if we want to create an abstract class
from abc import ABC,abstractmethod

# when we inherit the ABC class from abc module is said to be abstact class
class Shape(ABC):
    # decorators or annotation
    @abstractmethod
    def calculatePerimeter(self):
        return
    def calculateArea(self):
        print("area is calculating......")

# triangle => concrete class
# shape => abstract class => calculatePerimeter => abstracted / unimplemented
class Triangle(Shape):
# override
    def calculatePerimeter(self):
        print("trianlge perimeter is calculating....")
    def sayHi(self):
        print("hi.....")

class Circle(Shape):
# override
    def calculatePerimeter(self):
        print("circle perimeter is calculating......")
    def sayHi(self):
        print("hi.....")

t1 = Triangle()

# condition in 'if' statement - you will get the result only if you run this 
# main file(abstraction.py) directly
if(__name__=="__main__"): 
    t1.calculatePerimeter()

# s1 = Shape()
# s1.calculatePerimeter()
# s1.calculateArea()


# note: when we define an abstract method into an abstract class
#  we don't need to create an object or we can't instantiate the class