from random import randint

def pierreFeuilleCiseaux():
    nickname = input("Entrez votre pseudo : ")
    playerPoint = 0
    computerPoint = 0
    
    game = input(nickname + ", voulez-vous jouer ? ")
    if game == "oui":
        game = True
    elif game == "non":
        game = False

    while game == True:
        print("Chi-fou-mi !")

        computerChoice = randint(1, 3)
        if computerChoice == 1:
            computerChoice = "Pierre"
        elif computerChoice == 2:
            computerChoice = "Feuille"
        else: 
            computerChoice = "Ciseaux"

        playerChoice = input("(P)ierre/(F)euille/(C)iseaux ? ")

        if playerChoice == "P" or "p" and computerChoice == 1:
            print(playerChoice + " VS " + computerChoice)
            print("Egalité")
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")
        
        if playerChoice == "P" or "p" and computerChoice == 3:
            print(playerChoice + " VS " + computerChoice)
            print("Gagné")
            playerPoint = playerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")

        if playerChoice == "P" or "p" and computerChoice == 2:
            print(playerChoice + " VS " + computerChoice)
            print("Perdu")
            computerPoint = computerPoint + 1
            print(nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            print("------------------------------")

        if playerPoint == 3:
            print(nickname + ", vous avez gagné la partie ! :)")
            otherGame = input("Voulez-vous rejouer ? ")
            if otherGame == "oui":
                print("C'est reparti !")
                pierreFeuilleCiseaux()
            elif otherGame == "no":
                print("A bientôt, " + nickname  + " !")
                break
        elif computerPoint == 3:
            print(nickname + ", vous avez perdu la partie ! :(")
            otherGame = input("Voulez-vous rejouer ? ")
            if otherGame == "oui":
                print("C'est reparti !")
                pierreFeuilleCiseaux()
            elif otherGame == "no":
                print("A bientôt, " + nickname  + " !")
                break

pierreFeuilleCiseaux()