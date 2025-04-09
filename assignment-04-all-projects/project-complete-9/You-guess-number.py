# Guess the Number - You guess 🎯

import random

print("I'm thinking of a number between 1 and 100...")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} tries 🎉")
        break