import random

print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100. \n Guess the number. \n You have 5 chances to guess the number.")

number_to_guess = random.randint(1, 10)

chances = 5

guess_counter = 0

while guess_counter < chances:
    guess_counter +=  1
    my_guess = int(input("Make a guess: "))

    if my_guess == number_to_guess:
        print(f"YOU GOT IT! The Answer Was {number_to_guess}")
        break
    elif my_guess < number_to_guess:
        print("Your Number is too low.")
    else:
        print("Your Number is too high.")

if guess_counter == chances:
    print(f"You've run out of guesses. The number was {number_to_guess}")

