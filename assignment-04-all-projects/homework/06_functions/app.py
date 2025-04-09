# ----------00------------------------------------------------------------
def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    

if __name__ == '__main__':
    main()


    -# ----------01------------------------------------------------------------
    import random

DONE_LIKELIHOOD = 0.3  # You can change this value (between 0 and 1) to adjust randomness

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # this ends the function execution, so we'll get back to the main() function!
        print(curr_num)

# There is no need to edit code beyond this point

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
# ----------02------------------------------------------------------------


def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0: 
            count += 1 

 

    print(count) 

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  
        lst.append(int(user_input)) 
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()

# ----------03------------------------------------------------------------
def double(num: int):
    return num * 2

def main():
    num = int(input("Enter a number: "))  # User input
    num_times_2 = double(num)  # Call the double function
    print("Double that is", num_times_2)  # Output the result

if __name__ == '__main__':
    main()
# ----------04------------------------------------------------------------
def get_name():
    return "alishba"

def main():
    name = get_name()
    print(f"Howdy {name} ! 🤠")

main()
# ----------05------------------------------------------------------------
def main():
    for i in range(10):
        if is_odd(i):
            print('odd')
        else:
            print('even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2 
    return remainder == 1


if __name__ == '__main__':
    main()
# ----------06------------------------------------------------------------
def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

main()
# ----------07------------------------------------------------------------
def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)
def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
# ----------08------------------------------------------------------------
def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech entered.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
# ----------09------------------------------------------------------------
def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)
if __name__ == '__main__':
    main()
