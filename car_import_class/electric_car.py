from car import Car


class Battery:
    """An attempt to model a battery for an electric car"""
    def __init__(self, battery_size = 75 ):
        """Initialize the batterrie's attribute"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing a battery size """
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        """Print a statement about a range this battery can provide"""
        if self.battery_size == 75:
            range = 150
        elif self.battery_size == 90:
            range = 195
        print(f'This car can go {range} miles on a full charge.')

class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicle's"""
    def __init__(self, make, model, year):
        """Initialize attribute of a parent class"""
        """Then Initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tank"""
        print('This car doesn\'t have a gas tank!')