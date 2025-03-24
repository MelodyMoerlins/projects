#gUSSING GAME PROJECT 3/24/2025
import random

low = input("You want your number to guess to be in between: ")
high = input("and: ")

number = int(random.uniform(int(low), int(high)))

guess = int(input(f"What's your first guess for a random number between {low} and {high}? "))

while guess != number:
    if number > guess:
        lower = "higher"
    else:
        lower = "lower"
    print(f"That's wrong. Your number is {lower}")
    guess = int(input(f"What's your next guess for a random number between {low} and {high}? "))

if number == guess:
    print("Congratulations! You won!")
