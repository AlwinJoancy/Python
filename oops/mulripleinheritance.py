# parent class
class Wheel: 
    # __init__ is a constructor. It initializes object attributes.
    def _init_(self, wheel_type):
        self.wheel=wheel_type

class Paint:
    def _init_(self, car_color):
        self.paint=car_color
    
class Stearing():
    def _init_(self, stear_type):
        self.stearing=stear_type
        
# Car class inheriting from Wheel, Paint, and Stearing classes.
class Car(Wheel, Paint, Stearing):
    # Inside Car.__init__(), we call the constructors of the parent classes
    # to initialize their attributes.
    def _init_(self, car_name, car_model, wheel_type,  stear_type, car_color):
        self.cname=car_name
        self.model=car_model
         # Call parent class constructors
        Wheel._init_(self,wheel_type)        
        Paint._init_(self,car_color)
        Stearing._init_(self,stear_type)

    # printCarDetails() prints all the attributes.
    def printCarDetails(self): 
        print("Car Name:", self.cname, '\n'"Model:", self.model, '\n'"Wheel Type:",self.wheel,'\n'
            "Stearing Type:", self.stearing, '\n'"Color:",self.paint)
        print("--------")
    
    
# Vechical is object variable 
vechical=Car("Innova", 2005, "Alloy", "folks","Metalic Blue")
vechical.printCarDetails()

johncar=Car("KIA", "2000", "Metal", "basic","Red")
johncar.printCarDetails()

meenacar=Car("Qualis", "2007", "Iron", "Common","Gold")
meenacar.printCarDetails()