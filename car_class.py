class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # set default value for an attribute
        
    def description(self):
        print(f"Brand new {self.make} {self.model} model, produced in {self.year}")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on odometer")

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print(f'You cannot roll back an odometer')

my_car = Car('audi', 'A8', 2022)
my_car.description()
my_car.odometer_reading = 45
my_car.update_odometer(55)
my_car.read_odometer()
my_car.increment_odometer(-100)
my_car.read_odometer()
