import random

# regle du jeu
print("Winning Rules of the Color choice Game as follows :\n Enter a number from one to five and match computer choice to win")

computer_score = 0
player_score = 0
colors = ["Red",'Yellow','Orange','Green','Blue']
while True:
    print("Red = 1 \nYellow = 2 \nOrange = 3 \nGreen = 4 \nBlue = 5 \nTake a turn: ")

    # Recuperer la donnee saisi par l'utilisateur
    player_choice = int(input("User turn: "))

    # se rassurer que l'utilisateur saisi la bonne donnee
    while player_choice > 5 or player_choice <1:
        player_choice = int(input("Enter a valid input: "))

    # initialiser la variable choice_color qui correspond a la couleur choisi par l'utilisateur
    choice_color = colors[player_choice-1]

    # affiche le choix de l'utilisateur
    print("\nNow its computer turn to choose a color ...")

    # L'ordinateur choisit aleatoirement n'importe quel nombre parmis 1, 2 et 3.
    computer_choice = random.randint(1,5)

    #initialiser la valeur du choix de couleur de l'ordinateur
    computer_choice_color = colors[computer_choice-1]

    print("Computer color choice is: "+ computer_choice_color)
    print("User color choice is :" + choice_color)
    #condition pour gagner
    if(choice_color == computer_choice_color):
        player_score +=1
        print("player score: "+str(player_score))
        print("computer score: " +str(computer_score))
    else:
        computer_score +=1
        print("player score: "+ str(player_score))
        print("computer score: " + str(computer_score))
    print("Veux tu encore jouer? (Y/N)")
    answer = input()

    #isi l'utilisateur choisit n ou N alors la condition est True
    if answer == 'n' or answer == 'N':
        break
