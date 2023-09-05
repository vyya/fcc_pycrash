"""A class that can be used to represent a car"""
class Car:
    """An attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_level = 20

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car's milage"""
        print(f'This car has a {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        """Set odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

