from abc import ABC,abstractmethod

class Colour(ABC):
    @abstractmethod
    def colortype(self):
        print("You have choosen light colour")

class Txtcolour(Colour):
    # def tcolour(self): - this will throw below error
    # Can't instantiate abstract class Txtcolour without an implementation for abstract method 'colortype'
    def colortype(self): #You need to implement the abstract method colortype() in every subclass.
     print("Your txt colour is light blue")

class bgcolour(Colour):
    def colortype(self):
    # def bckclolour(self):
        print("Your background colour is contrast")


if(__name__=="__main__"): 
    c = Txtcolour()
    c.colortype()