# creer une classe Gameboard
class Gameboard():
    # creer le constructeur de la classe
    def __init__(self):
        self.game_board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

    # Ensuite nous creons une fonction setter pour les items
    def set_items(self, user, position, game_board):
        game_board[position] = user
        return game_board
    
    # Creer un decorateur (@property) pour la fonction gameboard afin d'ajouter une intense separe self pour game_board
    @property
    def gameBoard(self):
        return self.game_board
    
    #ajouter une autre fonction appelee reinitialise les boards
    def clearboard(self):
        self.game_board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

    # ajouter une autre fonction appelle prendre une place
    def is_place_taken(self,game_board, index):
        if game_board[index] != ' ':
            return True
        
    # ajouter une autre fonction pour savoir si le board est plein
    def is_board_full(self,game_board):
        for index in range(1, 10):
            if game_board[index] == ' ':
                return False
        return True
    
    # ajouter pour savoir si le jeu est gagne
    def is_game_won(self, game_board):
        win_conds = ((1,2,3), (4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
        for win_cond in win_conds:
            if game_board[win_cond[0]] == game_board[win_cond[1]] and game_board[win_cond[1]] == game_board[win_cond[2]] and game_board[win_cond[0]] != ' ':
                return True
            
    # fonction qui affiche le tableau du jeu.
    def printBoard(self, game_board):
        index = 0
        for row in range(1, 4):
            for column in range(1, 4):
                index += 1
                if column != 3:
                    print(game_board[index], end="")
                    print('|', end='')
                else:
                    print(game_board[index])
