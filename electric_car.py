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


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
