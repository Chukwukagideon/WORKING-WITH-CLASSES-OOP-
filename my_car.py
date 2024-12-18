from car import Car


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying attribute values can be done in 3 ways
# Modifying an attribute value directly
print()
my_new_car.odometer_reading = 23
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()