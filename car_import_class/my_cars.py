# from car import Car, ElectricCar
import car

# my_nissan = Car('Nissan', 'Terrano', 2008)
my_nissan = car.Car('Nissan', 'Terrano', 2008)
print(my_nissan.get_descriptive_name())
# my_tesla = ElectricCar('Tesla', 'Lotus', 2019)
my_tesla = car.ElectricCar('Tesla', 'Lotus', 2019)
print(my_tesla.get_descriptive_name())