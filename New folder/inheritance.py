# class car:
#     def __init__(self,car_name):
#         self.name =car_name
#         print("Car name: Innova")

# class wheel(car):
#     def __init__(self, wheel_type, car_name):
#         self.wheeltype = wheel_type
#         super.__init__(car_name)
#         print("Alloy")

# class model(wheel):
#     def __init__(self, car_model, car_name, wheel_type ):
#         self.model = car_model
#         wheel.__init__(self, car_name, wheel_type )


class Wheel:
    def __init__(self, wheel_type):
        self.wheel=wheel_type

class Paint:
    def __init__(self, car_color):
        self.paint=car_color
    
class Stearing():
    def __init__(self, stear_type):
        self.stearing=stear_type
        

class Car(Wheel, Paint, Stearing):
    def __init__(self, car_name, car_model, wheel_type,  stear_type, car_color):
        self.cname=car_name
        self.model=car_model
        Wheel.__init__(self,wheel_type)        
        Paint.__init__(self,car_color)
        Stearing.__init__(self,stear_type)

    def printCarDetails(self):
        print("Car Name:", self.cname, '\n'"Model:", self.model, '\n'"Wheel Type:",self.wheel,'\n'
            "Stearing Type:", self.stearing, '\n'"Color:",self.paint)
        print("--------")
    
    

vechical=Car("Innova", 2005, "Alloy", "folks","Metalic Blue")
vechical.printCarDetails()

# johncar=Car("KIA", "2000", "Metal", "basic","Red")
# johncar.printCarDetails()

meenacar=Car("Qualis", "2007", "Iron", "Common","Gold")
meenacar.printCarDetails()




        


        
        
    