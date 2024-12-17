class Car:
    """A simple attempt to model a car"""
    def __init__(self, make, model, year):
        """initialise attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modifying an attribute value through a method
    def update_odometer(self, mileage):
        """Set odometer reading to given value
        Reject the change if it attempts to roll back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("Odometer reading successfully updated")
        else:
            print("You can't roll back an odometer")

    # Incrementing an attribute value through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't reduce the odometer reading")

    def fill_gas_tank(self):
        """print a statement to indicate that the gas tank has been filled"""
        print(f"Gas tank filled successfully")


class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-KWh battery size")

    def get_range(self):
        """"Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315

        print(f"This car can go about {car_range} miles on a full charge")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """Electric cars don't have gas tank, hence print a statement to overide
        the statement from the parent class"""
        print("This car doesn't need a gas tank")


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
