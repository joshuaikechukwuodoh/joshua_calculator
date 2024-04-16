import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Welcome message
    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")
    
    # Main game loop
    while True:
        # Get user input
        guess = input("Enter your guess (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if guess.lower() == 'q':
            print("Thanks for playing! The number was:", secret_number)
            break
        
        # Check if the input is a valid integer
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        # Convert the input to an integer
        guess = int(guess)
        
        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number correctly!")
            break

# Start the game
guess_number()


