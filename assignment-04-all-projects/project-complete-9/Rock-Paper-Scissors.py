# Rock, Paper, Scissors ✊✋✌ie
import random

options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)

user_choice = input("Choose rock, paper, or scissors: ").lower()

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win! 🎉")
else:
    print("You lose 😞")
# Rock, Paper, Scissors ✊✋✌

import random

options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)

user_choice = input("Choose rock, paper, or scissors: ").lower()

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win! 🎉")
else:
    print("You lose 😞")