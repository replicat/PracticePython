import random
import string

def start_game():
    # Greet the user
    print("Welcome to the Cows and Bulls Game!")

    # Generate random 4-digit number
    target = "".join(random.choice(string.digits) for i in range(4))
    count = 0

    while True:
        # Increase count
        count += 1
        # Ask for user input
        guess = input("Guess a 4-digit number (0000-9999):\n")

        # Compare every digit for cows
        cow = 0
        for i in range(4):
            if guess[i] == target[i]:
                cow += 1   
        # Count substring for bulls (Beware of dupes)
        bull = -cow
        for i in range(10):
            bull += min(guess.count(str(i)), target.count(str(i)))
        
        # Print result
        if cow == 4:
            print("You guessed it! It took you {} guess{}.".format(count, "" if count==1 else "es"))
            break
        else:
            print("{} cow{}, {} bull{}".format(cow, "" if cow == 1 else "s", bull, "" if bull == 1 else "s"))

if __name__=="__main__":
    start_game()