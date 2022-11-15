#DEBUT

#on admet qu'une fonction random existe
from random import randint

#définir la fonction pierreFeuilleCiseaux qui demande le pseudo puis instaure le score du joueur et de l'ordi
def pierreFeuilleCiseaux():
    nickname = input("Entrez votre pseudo : ")
    playerPoint = 0
    computerPoint = 0
    
    #créer une variable game et lui associer le retour de l'exécution de la fonction input pour demander de jouer ou non
    game = input(nickname + ", voulez-vous jouer ? oui ou non : ")
    #si game est égal à oui
    if game == "oui":
        #alors game est vrai
        game = True
    #si game est égal à non
    elif game == "non":
        #alors game est faux et dit au revoir
        game = False
        print("Tant pis, à bientôt " + nickname  + " !")

    #tant que game est vrai le jeu Chifoumi se lance
    while game == True:
        print("------------------------------")
        print("Chi-fou-mi")

        #le choix de l'ordinateur renvoie un chiffre aléatoire entre 1 et 3, 1 étant la Pierre, 2 étant la Feuille et 3 étant les Ciseaux
        computerChoice = randint(1, 3)
        if computerChoice == 1:
            computerChoice = "Pierre"
        elif computerChoice == 2:
            computerChoice = "Feuille"
        else: 
            computerChoice = "Ciseaux"

        #créer une variable playerChoice et lui associer le retour de l'exécution de la fonction input qui demande de choisir Pierre, Feuille ou Ciseaux
        playerChoice = input("Pierre, Feuille ou Ciseaux ? ")

        #si le joueur choisis Pierre ET l'ordi choisis Pierre aussi alors il y a égalité 
        if playerChoice == "Pierre" and computerChoice == "Pierre":
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Feuille ET l'ordi choisis Feuille aussi alors il y a égalité 
        elif playerChoice == "Feuille" and computerChoice == "Feuille":
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Ciseaux ET l'ordi choisis Ciseaux aussi alors il y a égalité 
        elif playerChoice == "Ciseaux" and computerChoice == "Ciseaux":
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Pierre ET l'ordi choisis Ciseaux alors le joueur gagne un point
        elif playerChoice == "Pierre" and computerChoice == "Ciseaux":
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Feuille ET l'ordi choisis Pierre alors le joueur gagne un point
        elif playerChoice == "Feuille" and computerChoice == "Pierre":
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Ciseaux ET l'ordi choisis Feuille alors le joueur gagne un point
        elif playerChoice == "Ciseaux" and computerChoice == "Feuille":
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Pierre ET l'ordi choisis Feuille alors l'ordi gagne un point
        elif playerChoice == "Pierre" and computerChoice == "Feuille":
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Feuille ET l'ordi choisis Ciseaux alors l'ordi gagne un point
        elif playerChoice == "Feuille" and computerChoice == "Ciseaux":
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis Ciseaux ET l'ordi choisis Pierre alors l'ordi gagne un point
        elif playerChoice == "Ciseaux" and computerChoice == "Pierre":
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")

        #si le joueur est à trois points alors il a gagné la partie
        if playerPoint == 3:
            print(nickname + ", vous avez gagné la partie ! :)")
            #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input qui demande si le joueur veut refaire une partie
            otherGame = input("Voulez-vous rejouer ? oui ou non : ")
            #si otherGame est égal à oui alors le jeu se relance en exécutant la fonction pierreFeuilleCiseaux
            if otherGame == "oui":
                print("C'est reparti !")
                pierreFeuilleCiseaux()
            #si otherGame est égale à non alors le jeu s'arrête
            elif otherGame == "non":
                print("A bientôt, " + nickname  + " !")
                break
        #si l'ordi est à trois points alors il a gagné la partie
        elif computerPoint == 3:
            print(nickname + ", vous avez perdu la partie ! :(")
            #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input qui demande si le joueur veut refaire une partie
            otherGame = input("Voulez-vous rejouer ? oui ou non : ")
            #si otherGame est égal à oui alors le jeu se relance en exécutant la fonction pierreFeuilleCiseaux
            if otherGame == "oui":
                print("C'est reparti !")
                pierreFeuilleCiseaux()
            #si otherGame est égale à non alors le jeu s'arrête
            elif otherGame == "non":
                print("A bientôt, " + nickname  + " !")
                break

#exécuter la fonction pierreFeuilleCiseaux()
pierreFeuilleCiseaux()

#FIN