from car import Car

my_new_car = Car('Subaru', 'Forester', 2007)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 79
my_new_car.read_odometer()