class User:
    """Simulating a user profile"""
    def __init__(self, first_name, last_name, age, gender):
        """Initialising the attributes of the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"here is a summary of the user profile:\n"
              f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Gender: {self.gender}\n")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome to your profile.\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Gideon", "Nwajee", "27", "Male")
user2 = User("John", "Doe", 30, "Male")
user3 = User("Stephanie", "Bold", 29, "Female")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

user1.increment_login_attempts()
print(f"Number of attempted log in: {user1.login_attempts}")

user1.increment_login_attempts()
print(f"Number of attempted log in: {user1.login_attempts}")

user1.increment_login_attempts()
print(f"Number of attempted log in: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Number of attempted log in: {user1.login_attempts}")


class Privileges:
    """Create a class that takes all admin privileges"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """print a statement showing the admin privileges"""
        privileges_str = ",\n".join(self.privileges)
        print(f"The following are the admin privileges:\n"
              f"{privileges_str}")


class Administrator(User):
    """Creating an Administrator which is a special kind of user"""
    def __init__(self, first_name, last_name, age, gender):
        """Initialize the parent attributes.
        Then create attributes specific to the administrator"""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


print()
administrator1 = Administrator("Johnny", "Doe", 30, "Male")
administrator1.privileges.show_privileges()