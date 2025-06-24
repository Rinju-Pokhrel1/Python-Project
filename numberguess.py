# Number Guessing Game

import random

number_to_guess = random.randint(1, 200)

while True:
    try:   # prevent the program from crashing 
        guess = int(input("Guess the number between (1, 200): "))  
        
        if guess < number_to_guess:
            print("Too low!")

        elif guess > number_to_guess:
            print("Too high!")

        else:
            print("Congratulations! You guessed the number.")
            break

    except ValueError:
        print("Please enter a valid number.")
