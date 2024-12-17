class Restaurant:
    """A simple restaurant model"""
    def __init__(self, restaurant_name, cuisine_type):
        """initialising restaurant attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"Our strength is the {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")


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
print()
restaurant3.describe_restaurant()

