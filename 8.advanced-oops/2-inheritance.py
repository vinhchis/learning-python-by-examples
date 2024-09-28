class Vehicle: 
    def __init__(self, make, model): 
        self.make = make 
        self.model = model 
 
    def get_info(self): 
        return f"Make: {self.make}, Model: {self.model}" 
 
class Car(Vehicle): 
    def __init__(self, make, model, year): 
        super().__init__(make, model) 
        self.year = year 
 
    def get_info(self): 
        return f"Year: {self.year}, {super().get_info()}" 
 
class ElectricCar(Car): 
    def __init__(self, make, model, year, battery_capacity): 
        super().__init__(make, model, year) 
        self.battery_capacity = battery_capacity 
 
    def get_info(self): 
        return f"Battery Capacity: {self.battery_capacity}, {super().get_info()}" 
 
# Creating instances of the classes 
car1 = Car("Toyota", "Camry", 2022) 
electric_car1 = ElectricCar("Tesla", "Model 3", 2022, "75 kWh") 
 
# Accessing the information using overridden methods 
print(car1.get_info()) 
print(electric_car1.get_info())