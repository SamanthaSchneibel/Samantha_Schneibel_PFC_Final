#DEBUT  

#on admet qu'une fonction random existe

#definir la fonction pierreFeuilleCiseaux
    #créer une variable nickname et lui associer le retour de l'exécution de la fonction input pour demander ("Entrez votre pseudo : ")
    #créer une variable playerPoint égale à 0
    #créer une variable computerPoint égale à 0

    #créer une variable game et lui associer le retour de l'exécution de la fonction input pour demander (nickname + ", voulez-vous jouer ? oui ou non : ")
    #si game est égal à oui
        #alors game est vrai
    #si game est égal à non
        #alors game est faux
        #afficher ("tant pis, à bientôt " + nickname + " !")

    #tant que game est vrai
        #afficher ("Chi-fou-mi")

        #créer une variable computerChoice qui renvoie un chiffre aléatoire entre 1 et 3
        #si computerChoice est égal à 1
            #alors computerChoice est égal à pierre
        #si computerChoice est égal à 2
            #alors computerChoice est égal à feuille
        #sinon
            #computerChoice est égal à ciseaux

        #créer une variable playerChoice et lui associer le retour de l'exécution de la fonction input pour demander ("pierre, feuille ou ciseaux ? ")
        #si playerChoice est égal à pierre ET computerChoice est égal à pierre
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Egalité")
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à feuille ET computerChoice est égal à feuille
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Egalité")
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à ciseaux ET computerChoice est égal à ciseaux
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Egalité")
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à pierre ET computerChoice est égal à ciseaux
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Gagné")
            #incrémenter 1 à playerPoint
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à feuille ET computerChoice est égal à pierre
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Gagné")
            #incrémenter 1 à playerPoint
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à ciseaux ET computerChoice est égal à feuille
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Gagné")
            #incrémenter 1 à playerPoint
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à pierre ET computerChoice est égal à feuille
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Perdu")
            #incrémenter 1 à computerPoint
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à feuille ET computerChoice est égal à ciseaux
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Perdu")
            #incrémenter 1 à computerPoint
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")
        #si playerChoice est égal à ciseaux ET computerChoice est égal à pierre
            #alors afficher (playerChoice + " VS " + computerChoice)
            #afficher ("Perdu")
            #incrémenter 1 à computerPoint
            #afficher (nickname + ": " + str(playerPoint) + " Ordinateur : " + str(computerPoint))
            #afficher ("------------------------------")

        #si playerPoint est égal à 3
            #alors afficher (nickname + ", vous avez gagné la partie ! :)")
            #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input qui demande ("Voulez-vous rejouer ? oui ou non : )
            #si otherGame est égal à oui
                #alors afficher ("C'est reparti !")
                #exécuter la fonction pierreFeuilleCiseaux
            #si otherGame est égal à non
                #alors afficher ("A bientôt, " + nickname  + " !")
                #casser la boucle
            #sinon
                #redemander avec la fonction input ("Voulez-vous rejouer ? oui ou non : ")

#exécuter la fonction pierreFeuilleCiseaux