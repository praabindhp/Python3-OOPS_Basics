class Vehicle:
     
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
 
    def fuel_consumption(self):
        pass
 
class Bus(Vehicle):
 
    def __init__(self, brand, year):
        super().__init__(brand, year)
 
    def fuel_consumption(self):
        print('Fuel Consumption For Bus...')
 
class Car(Vehicle):
 
    def __init__(self, brand, year):
        super().__init__(brand, year)
 
    def fuel_consumption(self):
        print('Fuel Consumption For Car...')

bus = Bus(brand='Ford', year=1957)
bus.fuel_consumption()
 
car = Car(brand='BMW', year=1998)
car.fuel_consumption()