# Settings
numOfPlayers = 2

# List of valid words for input
listRock = ["R", "r", "Rock", "rock"]
listPaper = ["P", "p", "Paper", "paper"]
listScissors = ["S", "s", "Scissors", "scissors"]

# Infinite loop
while True:
    # Ask for input
    plays = []
    for i in range(numOfPlayers):
        plays.append(input("Player " + str(i+1) + " please choose from Rock(R), Paper(P) or Scissors(S): "))
    print()

    # Check input validity
    for i in range(numOfPlayers):
        if plays[i] in listRock:
            print("Player " + str(i+1) + " chooses Rock.")
            plays[i] = 1
        elif plays[i] in listPaper:
            print("Player " + str(i+1) + " chooses Paper.")
            plays[i] = 2
        elif plays[i] in listScissors:
            print("Player " + str(i+1) + " chooses Scissors.")
            plays[i] = 3
        else:
            print("Player " + str(i+1) + "'s input is invalid.")
            plays[i] = 0

    # Compare pairs of result
    winOver = []
    for i in range(numOfPlayers):
        winOver.append([])
        for j in range(numOfPlayers):
            if (i != j) and ((plays[i] == 1 and plays[j] == 3) or (not (plays[i] == 3 and plays[j] == 1) and plays[i] > plays[j])):
                winOver[i].append(j)
    
    # Determine winner
    draw = True;                
    for i in range(numOfPlayers):
        if len(winOver[i]) == numOfPlayers-1:
            draw = False
            print("== Player " + str(i+1) + " won the game! ==")
            break
    if draw:
        print("== It is a draw! ==")
    print()

    # Ask if continue
    if input("Start a new game? (Y/N): ") not in ("Y", "y", "Yes", "yes"):
        break