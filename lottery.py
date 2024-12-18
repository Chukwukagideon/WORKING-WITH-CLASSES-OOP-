import random

ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

# randomly select 4 numbers or letters
winning_combination = random.sample(ticket, k=4)
print(f"Any ticket matching these for numbers or letters wins a prize:\n {winning_combination}")


# initializing the counter
count = 0

while True:
    # randomly select 4 numbers or letters
    pulled_ticket = random.sample(ticket, k=4)
    count += 1

    # check if our pulled ticket match the winning combination
    if set(winning_combination) == set(pulled_ticket):
        break

print(pulled_ticket)
print(f"It took {count} times to pull the winning ticket")
