# Guess the Number - Computer guesses the number
print("Think of a number between 1 and 100. I will try to guess it!")

low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    print(f"My guess is {guess}")
    feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()
    attempts += 1

    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'c':
        print(f"Yay! I guessed your number in {attempts} tries! 🎉")
        break
    else:
        print("Please enter h, l, or c only.")