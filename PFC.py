from random import randint

def pierreFeuilleCiseaux():
    nickname = input("Entrez votre pseudo : ")
    playerPoint = 0
    computerPoint = 0
    
    game = input(nickname + ", voulez-vous jouer ?")
    if game == "yes":
        game = True
    elif game == "no":
        game = False

    while game == True:
        print("Chi-fou-mi")

        computerChoice = randint(1, 3)
        if computerChoice == 1:
            computerChoice = "Pierre"
        elif computerChoice == 2:
            computerChoice = "Feuille"
        else: computerChoice = "Ciseaux"

        playerChoice = input("(P)ierre/(F)euille/(C)iseaux")
        if playerChoice == "P" or "p":
            playerChoice = "Pierre"
        elif playerChoice == "F" or "f":
            playerChoice = "Feuille"
        elif playerChoice == "C" or "c":
            playerChoice = "Ciseaux"

        if playerChoice == computerChoice :
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ":" + str(playerPoint) + "Ordinateur :" + str(computerPoint))

        elif playerChoice == "Pierre" and computerChoice == "Ciseaux" or (playerChoice == "Feuille" and computerChoice == "Pierre") or(playerChoice == "Ciseaux" and computerChoice == "Feuille"):
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ":" + str(playerPoint) + "Ordinateur :" + str(computerPoint))
        
        elif playerChoice == "Pierre" and computerChoice == "Feuille" or (playerChoice == "Feuille" and computerChoice == "Ciseaux") or(playerChoice == "Ciseaux" and computerChoice == "Pierre"):
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ":" + str(playerPoint) + "Ordinateur :" + str(computerPoint))

        if playerPoint == 3:
            print(nickname + ", vous avez gagné la partie ! :)")
            break
        elif computerPoint == 3:
            print(nickname + ", vous avez perdu la partie ! :(")
            break

pierreFeuilleCiseaux()