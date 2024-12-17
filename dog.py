class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def rollover(self):
        """simulate a dog rolling over in response to  command"""
        print(f"{self.name} is now rolling")


my_dog = Dog("Billy", 8)
your_dog = Dog("shirley", 6)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old")
my_dog.sit()
my_dog.rollover()
your_dog.sit()
