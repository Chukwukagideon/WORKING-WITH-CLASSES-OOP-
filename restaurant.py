class Restaurant:
    """A simple restaurant model"""
    def __init__(self, restaurant_name, cuisine_type):
        """initialising restaurant attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"Our strength is the {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

    def set_number_served(self, customers_served):
        self.number_served = customers_served

    def increment_number_served(self, customer):
        self.number_served += customer



restaurant = Restaurant("Hot n Spicy", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print()
restaurant.open_restaurant()
restaurant.describe_restaurant()

restaurant2 = Restaurant("Hot pot", "Japanese")
restaurant3 = Restaurant("Sweet","Chinese")

print()
restaurant2.describe_restaurant()
restaurant2.set_number_served(5)
print(f"Total number of customer's sevred today is {restaurant2.number_served}")

restaurant2.increment_number_served(2)
print(f"Total number of customer's sevred today is {restaurant2.number_served}")

print()
restaurant3.describe_restaurant()
print(f"Total number of customer's served for today is {restaurant3.number_served}")


class IceCreamStand(Restaurant):
    """Represents an Ice cream stand which is a kind of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the parent class attributes.
        Then initialize attributes specific to the Ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "Strawberry", "Chocolate"]

    def display_flavors(self):
        """print a statement that shows the various flavors offered"""
        print(f"At {self.restaurant_name}, we offer the following flavours:\n"
              f"{self.flavors}")

print()
my_Ice_cream_stand = IceCreamStand("Sweet cream", "Mexican")
my_Ice_cream_stand.display_flavors()

