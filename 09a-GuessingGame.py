import random

# Generate a random integer between 1 and 9
target_num = random.randint(1, 10)

# Ask the user to guess the number
while True:
    guess = input("Guess a number between 1 and 9: ")
    if guess == "exit":
        break
    else:
        guess_num = int(guess)
    
    if guess_num > target_num:
        print("You guessed too high! Try again.")
    elif guess_num < target_num:
        print("You guessed too low! Try again.")
    else:
        print("You guessed it! Good job! Care for another round?")
        target_num = random.randint(1, 10)
        