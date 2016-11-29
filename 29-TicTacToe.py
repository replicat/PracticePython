# Piecing 24, 26 and 27 together
SYMBOL = {0: " ", 1: "X", 2: "O"}

# From 24, modified heavily
def board(game):
    _board = ""
    for i in range(3):
        _board += " ---"*3 + "\n"
        for j in range(3):
            _board += "| {} ".format(SYMBOL[game[i][j]])
        _board += "|\n"
    _board += " ---"*3
    return _board

# From 26
def check(game):
    for p in range(1, 3):
        # Check verticals and horizontals
        for i in range (3):
            if (game[i][0] == p and game[i][1] == p and game[i][2] == p) or (game[0][i] == p and game[1][i] == p and game[2][i] == p):
                return p
        # Check diagonals
        if (game[0][0] == p and game[1][1] == p and game[2][2] == p) or (game[0][2] == p and game[1][1] == p and game[2][0] == p):
                return p
    return 0

# From 27
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 1

while True:
    # Print the board
    print(board(game))

    # Check winning condition
    if check(game):
        print("Player {} won the game!".format(check(game)))
        break

    # Check board filling condition
    if all([all(i) for i in game]):
        print("The board is filled. Nobody wins!")
        break
        
    # Ask for input
    x, y = (int(i) for i in input("Player {} please choose a cell by entering a coordinate (row, col):\n".format(player)).split(","))
    if game[x-1][y-1]:
        print("The cell at ({}, {}) is already occupied. Please choose another cell.".format(x, y))
    else:
        game[x-1][y-1] = player
        player = abs(player-2)+1