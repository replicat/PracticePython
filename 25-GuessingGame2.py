# On the trail of binary search again.
min = 0
max = 100

# Greet the user.
print("Hi! Think of a number between {} and {}, and I will try to guess it!".format(min, max))
count = 0

# Main loop.
while True:
    count += 1
    guess = (min+max)//2
    print("I am guessing {}.".format(guess))
    print("Am I right? Or am I guessing too high or too low?")
    i = input("Type C for correct, H for too high and L for too low: ")
    if i == "C":
        print("See? I am clever. It only took me {} guess{}!".format(count, "" if count == 1 else "es"))
        break
    elif i == "H":
        max = guess-1
        print("Let me try again.")
    elif i == "L":
        min = guess+1
        print("Let me try again.")
    else:
        print("What were you saying?")