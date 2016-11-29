# Elegancy? Who cares!
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

# Testing examples
if __name__ == "__main__":

    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]  
    print(check(game))
    
    winner_is_2 = [ [2, 2, 0],
	                [2, 1, 0],
    	            [2, 1, 1]]
    print(check(winner_is_2))

    winner_is_1 = [ [1, 2, 0],
	                [2, 1, 0],
	                [2, 1, 1]]
    print(check(winner_is_1))

    winner_is_also_1 = [[0, 1, 0],
    	                [2, 1, 0],
    	                [2, 1, 1]]
    print(check(winner_is_also_1))

    no_winner = [   [1, 2, 0],
	                [2, 1, 0],
    	            [2, 1, 2]]
    print(check(no_winner))

    also_no_winner = [  [1, 2, 0],
	                    [2, 1, 0],
	                    [2, 1, 0]]
    print(check(also_no_winner))