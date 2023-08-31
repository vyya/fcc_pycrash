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
    
    def fill_gas_tank(self):
        print(f'Safety level of gas is {self.gas_tank_level}.')



class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicle's"""
    def __init__(self, make, model, year):
        """Initialize attribute of a parent class"""
        """Then Initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing a battery size"""
        print(f'This car has a {self.battery_size}-kWh battery size.')

    def fill_gas_tank(self):
        """Electric cars don't have gas tank"""
        print('This car doesn\'t have a gas tank!')

        

my_tesla = ElectricCar('tesla', 'obsidian', 2022 )
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
    

