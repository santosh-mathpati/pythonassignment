#oops concept
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        return f"Car: {self.brand} {self.model}"

# Creating objects of Car class

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.show_details())  # Output: Car: Toyota Corolla
print(car2.show_details())  # Output: Car: Honda Civic


class ElectricCar(Car):  # Child class inherits from Car
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call parent constructor
        self.battery_capacity = battery_capacity

    def show_details(self):  # Overriding method
        return f"Electric Car: {self.brand} {self.model}, Battery: {self.battery_capacity} kWh"

# Creating object of ElectricCar

tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.show_details())  # Output: Electric Car: Tesla Model S, Battery: 100 kWh
