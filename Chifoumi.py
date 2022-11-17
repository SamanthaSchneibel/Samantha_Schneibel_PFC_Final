#DEBUT

#on admet qu'une fonction random existe
from random import randint

#définir la fonction pierreFeuilleCiseaux qui demande le pseudo puis instaure le score du joueur et de l'ordi
def pierreFeuilleCiseaux():
    nickname = input("Entrez votre pseudo : \n")
    playerPoint = 0
    computerPoint = 0
    
    #créer une variable game et lui associer le retour de l'exécution de la fonction input pour demander de jouer ou non
    game = input(nickname + ", voulez-vous jouer ? oui ou non : \n")
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
        print("Chi-fou-mi")

        #créer une variable computerChoice qui renvoie un chiffre aléatoire entre 1 et 3, 1 étant la pierre, 2 étant la feuille et 3 étant les ciseaux
        computerChoice = randint(1, 3)
        if computerChoice == 1:
            computerChoice = "pierre"
        elif computerChoice == 2:
            computerChoice = "feuille"
        else: 
            computerChoice = "ciseaux"

        #créer une variable playerChoice et lui associer le retour de l'exécution de la fonction input qui demande de choisir pierre, feuille ou ciseaux
        playerChoice = input("pierre, feuille ou ciseaux ? \n")
        #si le joueur choisis pierre ET l'ordi choisis pierre aussi alors il y a égalité 
        if playerChoice == "pierre" and computerChoice == "pierre":
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis feuille ET l'ordi choisis feuille aussi alors il y a égalité 
        elif playerChoice == "feuille" and computerChoice == "feuille":
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis ciseaux ET l'ordi choisis ciseaux aussi alors il y a égalité 
        elif playerChoice == "ciseaux" and computerChoice == "ciseaux":
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis pierre ET l'ordi choisis ciseaux alors le joueur gagne un point
        elif playerChoice == "pierre" and computerChoice == "ciseaux":
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis feuille ET l'ordi choisis pierre alors le joueur gagne un point
        elif playerChoice == "feuille" and computerChoice == "pierre":
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis ciseaux ET l'ordi choisis feuille alors le joueur gagne un point
        elif playerChoice == "ciseaux" and computerChoice == "feuille":
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis pierre ET l'ordi choisis feuille alors l'ordi gagne un point
        elif playerChoice == "pierre" and computerChoice == "feuille":
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis feuille ET l'ordi choisis ciseaux alors l'ordi gagne un point
        elif playerChoice == "feuille" and computerChoice == "ciseaux":
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        #si le joueur choisis ciseaux ET l'ordi choisis pierre alors l'ordi gagne un point
        elif playerChoice == "ciseaux" and computerChoice == "pierre":
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")

        #si le joueur est à trois points alors il a gagné la partie
        if playerPoint == 3:
            print(nickname + ", vous avez gagné la partie ! :)")
            #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input qui demande si le joueur veut refaire une partie
            otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
            #si otherGame est égal à oui alors le jeu se relance
            if otherGame == "oui":
                print("C'est reparti !")
                game = True
                playerPoint = 0
                computerPoint = 0
            #si otherGame est égal à non alors le jeu s'arrête
            elif otherGame == "non":
                print("A bientôt, " + nickname  + " !")
                break
            #sinon redemander la question
            else: 
                otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
        #si l'ordi est à trois points alors il a gagné la partie
        elif computerPoint == 3:
            print(nickname + ", vous avez perdu la partie ! :(")           
            #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input qui demande si le joueur veut refaire une partie
            otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
            #si otherGame est égal à oui alors le jeu se relance
            if otherGame == "oui":
                print("C'est reparti !")
                game = True
                playerPoint = 0
                computerPoint = 0
            #si otherGame est égal à non alors le jeu s'arrête
            elif otherGame == "non":
                print("A bientôt, " + nickname  + " !")
                break
            #sinon redemander la question
            else: 
                otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
                     
#exécuter la fonction pierreFeuilleCiseaux
pierreFeuilleCiseaux()

#FIN