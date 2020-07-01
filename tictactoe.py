class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    
class Game:
    def play(board, player, row, column):
        board[row][column] = player.symbol
    

    #Player uses numbers 1, 2 , 3 for horizontol movement and numbers 1, 2, 3 for vertical movement for example if player wanted to move to center of the board 2,2.