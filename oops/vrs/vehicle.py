class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rentalrate = rental_rate


class Car(Vehicle):
    def calculate(self, brand, model, rental_rate, distance, load_capacity):
        self.brand = brand
        self.model = model
        self.total = rental_rate
        self.distance = distance
        self.load = load_capacity


class bike(Vehicle):
    def calculate(self, brand, model, bike_rental_cost, distance, load_capacity):
        self.brand = brand
        self.model = model
        self.total = bike_rental_cost
        self.distance = distance
        self.load = load_capacity


class truck(Vehicle):
    def calculate(self, brand, model, truck_rental_cost, distance, load_capacity):
        self.brand = brand
        self.model = model
        self.total = truck_rental_cost
        self.distance = distance
        self.load = load_capacity
