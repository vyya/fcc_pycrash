class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def description(self):
        long_desc = f"{self.make}, {self.model},{self.year}"
        return long_desc.upper()
    
fancy_car = Car('BMW', 'roadster', 2021)
print(fancy_car.description())