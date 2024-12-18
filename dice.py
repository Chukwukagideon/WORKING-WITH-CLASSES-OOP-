import random


class Die:
    """A class that models a dice"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = random.randint(1, self.sides)
        print(roll, end=",")


dice = Die()
no_of_rolls = 0
while no_of_rolls < 10:
    dice.roll_die()
    no_of_rolls += 1

dice = Die(10)
print()
no_of_rolls = 0
while no_of_rolls < 10:
    dice.roll_die()
    no_of_rolls += 1

dice = Die(20)
print()
no_of_rolls = 0
while no_of_rolls < 10:
    dice.roll_die()
    no_of_rolls += 1

