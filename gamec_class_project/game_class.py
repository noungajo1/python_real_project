# Cette classe est utile pour controler le start, end and stop du jeu
from gameboard_class import Gameboard


class Game():
    # game start
    def game_start(self):
        self.controlBoard = Gameboard()
        self.game_board = self.controlBoard.gameBoard
        self.playerOne = 'O'
        self.playerTwo = 'X'
        print('Bienvenue au jeu X-O ')
        print('Entrer le nom du premier joueur s\'il vous plait')
        self.player_one = input(' : ')
        print('Entrer le nom du deuxieme joueur s\'il vous plait')
        self.player_two = input(' : ')
        print('Voici votre tableau de jeu, chaque place est represente par 1-9, debutant de la colonne gauche chaque fois et se deplacant sur la ligne')
        self.controlBoard.printBoard(self.game_board)
        self.turn = 1

    #fin du jeu et rejouer
    def game_end(self):
        #verifier si le joueur veut terminer le jeu
        if self.game_running == False:
            replay = input('Appuyer 0 pour quitter ou 1 pour jouer encore ')
            try:
                if int(replay):
                    self.game_running == True
                    self.game_start()
            except:
                print('Un nombre doit etre saisi ')
                self.game_end()

    # tourner le jeu
    def takeTurn(self, user, item):
        print(user + ' choisi une place, 1-9')
        try:
            position = int(input(' : '))
            if position > 9 or position < 1:
                raise Exception
        except:
            print('Prendre un nombre compris entre 1-9 ')
            return self.takeTurn(user, item)
        
        if self.controlBoard.is_place_taken(self.game_board, position):
            print('Cette place est occupee')
            self.takeTurn(user, item)
        else:
            self.controlBoard.set_items(item, position, self.game_board)
            self.controlBoard.printBoard(self.game_board)
            if self.controlBoard.is_game_won(self.game_board):
                print(user + ' a gagne.')
                self.game_running = False

    # gestion du jeu
    def main(self,):
        self.game_running = True
        self.game_start()
        while self.game_running:
            if self.turn % 2 != 0:
                self.takeTurn(self.player_one, 'O')
            else:
                self.takeTurn(self.player_two, 'X')
            if self.controlBoard.is_board_full(self.game_board):
                print('C\'est un null !! Vous avez tous perdu')
                self.game_running = False
            self.turn += 1
            if not self.game_running:
                self.game_end()

# demarreur du jeu
if __name__ == '__main__':
    Game().main()
