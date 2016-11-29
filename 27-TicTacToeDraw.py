game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 1

while True:
    print("Current board: {}".format(game))
    x, y = (int(i) for i in input("Player {} please enter a coordinate: ".format(player)).split(","))
    if game[x-1][y-1] == 0:
        game[x-1][y-1] = player
        player = abs(player-2)+1
    else:
        print("The cell at ({}, {}) is already occupied.".format(x, y))