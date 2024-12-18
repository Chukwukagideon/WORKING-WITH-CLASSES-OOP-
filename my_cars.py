import car


my_beetle = car.Car("volkswagen", "beetle", 2020)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar("tesla", "roadster", 2023)
print(my_tesla.get_descriptive_name())
