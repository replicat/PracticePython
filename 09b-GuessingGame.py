import random

# Generate a random integer between 1 and 9
target_num = random.randint(1, 10)
count = 0

# Ask the user to guess the number
while True:
    guess = input("Guess a number between 1 and 9: ")
    if guess == "exit":
        break
    else:
        guess_num = int(guess)
    
    count += 1
    if guess_num > target_num:
        print("You guessed too high! Try again.")
    elif guess_num < target_num:
        print("You guessed too low! Try again.")
    else:
        print("You guessed it in {} times! Care for another round?".format(count))
        target_num = random.randint(1, 10)
        count = 0