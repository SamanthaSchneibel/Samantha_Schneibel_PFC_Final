#DEBUT

#on admet qu'une fonction random existe et renvoie un chiffre aléatoire entre 1 et 3
#on admet qu'une fonction input existe et demande à l'utilisateur de rentrer une chaine de caractères et la retourne
#definir un fonction pierreFeuilleCiseaux
    #créer une varaible playerPoint et lui associer 0
    #créer une variable ordiPoint et lui associer 0
    #créer une variable score et lui associer la concaténation nickname + ":" + str(playerPoint) + "Ordinateur : " + str(ordiPoint)
    #créer une variable nickname et lui associer le retour de l'exécution de la fonction input("Entrez votre pseudo : ")
    #créer une variable game et lui associer le retour de l'exécution de la fonction input("{nickname}, voulez-vous jouer ? : ")
    #otherGame est égal à vrai
        #si game est égal à "yes"
            #alors game est vrai
        #si game est égal à "no"
            #alors game est faux
        #tant que otherGame est vrai
        #tant que game est vrai
                #céer une variable playerChoice et lui associer le retour de l'exécution de la fonction input ("(P)ierre/(F)euille/(C)iseaux")
                #céer une variable ordiChoice et lui associer le retour de l'exécution de la fonction random
                #afficher "Chi-fou-mi"
                    #si playerChoice est égal à "P" ou "p" ET ordiChoice est égal à 1
                        #alors afficher "Pierre VS Pierre"
                        #afficher "Egalité"
                        #afficher score
                    #sinon si playerChoice est égal à "F" ou "f" ET ordiChoice est égal à 2
                        #alors afficher "Feuille VS Feuille"
                        #afficher "Egalité"
                        #afficher score
                    #sinon si playerChoice est égal à "C" ou "c" ET ordiChoice est égal à 3
                        #alors afficher "Ciseaux VS Ciseaux"
                        #afficher "Egalité"
                        #afficher score
                    #sinon si playerChoice est égal à "P" ou "p" ET ordiChoice est égal à 3
                        #alors afficher "Pierre VS Ciseaux"
                        #incrémenter playerPoint de 1
                        #afficher "Gagné"
                        #afficher score
                    #sinon si playerChoice est égal à "F" ou "f" ET ordiChoice est égal à 1
                        #alors afficher "Feuille VS Pierre"
                        #incrémenter playerPoint de 1
                        #afficher "Gagné"
                        #afficher score
                    #sinon si playerChoice est égal à "C" ou "c" ET ordiChoice est égal à 2
                        #alors afficher "Ciseaux VS Feuille"
                        #incrémenter playerPoint de 1
                        #afficher "Gagné"
                        #afficher score
                    #sinon si playerChoice est égal à "P" ou "p" ET ordiChoice est égal à 2
                        #alors afficher "Pierre VS Feuille"
                        #incrémenter ordiPoint de 1
                        #afficher "Perdu"
                        #afficher score
                    #sinon si playerChoice est égal à "F" ou "f" ET ordiChoice est égal à 3
                        #alors afficher "Feuille VS Ciseaux"
                        #incrémenter ordiPoint de 1
                        #afficher "Perdu"
                        #afficher score
                    #sinon si playerChoice est égal à "C" ou "c" ET ordiChoice est égal à 1
                        #alors afficher "Ciseaux VS Pierre"
                        #incrémenter ordiPoint de 1
                        #afficher "Perdu"
                        #afficher score
                    #si playerPoint est égal à 3
                        #alors afficher nickname + "vous avez gagné la partie ! :)"
                        #casser la boucle
                    #sinon si ordiPoint est égal à 3
                        #alors afficher nickname + "vous avez perdu la partie ! :("
                        #casser la boucle
        #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input("{nickname}, voulez-vous re jouer ? : ")
            #si otherGame est égal à "yes"
                #alors otherGame est vrai
                #afficher "C'est parti !"
            #si otherGame est égal à "no"
                #alors otherGame est faux
                #afficher "A bientôt nickname !"
                #casser la boucle
#éxecuter la fonction pierreFeuilleCiseaux()

#FIN