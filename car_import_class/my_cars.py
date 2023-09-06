'''# from car import Car, ElectricCar
import car

# my_nissan = Car('Nissan', 'Terrano', 2008)
my_nissan = car.Car('Nissan', 'Terrano', 2008)
print(my_nissan.get_descriptive_name())
# my_tesla = ElectricCar('Tesla', 'Lotus', 2019)
my_tesla = car.ElectricCar('Tesla', 'Lotus', 2019)
print(my_tesla.get_descriptive_name())'''

from car import Car
from electric_car import ElectricCar

my_leaf = Car('nissan', 'leaf', 2022)
print(my_leaf.get_descriptive_name())

my_zeekr = ElectricCar('zeekr', 'bomb', 2021)
print(my_zeekr.get_descriptive_name())
