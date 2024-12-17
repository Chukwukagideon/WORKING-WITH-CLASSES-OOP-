class User:
    """Simulating a user profile"""
    def __init__(self, first_name, last_name, age, gender):
        """Initialising the attributes of the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"here is a summary of the user profile:\n"
              f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Gender: {self.gender}\n")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome to your profile.\n")


user1 = User("Gideon", "Nwajee", "27", "Male")
user2 = User("John", "Doe", 30, "Male")
user3 = User("Stephanie", "Bold", 29, "Female")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()