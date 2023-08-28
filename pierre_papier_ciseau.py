
import random

# liste des choix possibles
choix = ["pierre", "papier", "ciseaux"]

# fonction qui détermine le gagnant du jeu
def gagnant(joueur, ordinateur):
    # si les deux choix sont égaux, c'est une égalité
    if joueur == ordinateur:
        return "Égalité"
    
    # sinon, on compare les choix selon les règles du jeu
    elif joueur == "pierre":
        if ordinateur == "papier":
            return "L'ordinateur gagne"
        else:
            return "vous avez gagné"
        
    elif joueur == "papier":
        if ordinateur == "ciseaux":
            return "L'ordinateur gagne"
        else:
            return "vous avez gagné"
        
    elif joueur == "ciseaux":
        if ordinateur == "pierre":
            return "L'ordinateur gagne"
        else:
            return "vous avez gagné"

# boucle principale du jeu
while True:
    # on demande au joueur de choisir entre pierre, papier ou ciseaux
    joueur = input("Choisissez entre pierre, papier ou ciseaux : ")
    
    # on vérifie que le choix est valide
    if joueur not in choix:
        print("Choix invalide")
        continue
    
    # on fait choisir l'ordinateur au hasard grace à ramdom
    ordinateur = random.choice(choix)
    
    # on affiche les choix du joueur et de l'ordi
    print(f"Vous avez choisi {joueur}")
    print(f"L'ordinateur a choisi {ordinateur}")
    
    # on détermine et affiche le gagnant du jeu
    resultat = gagnant(joueur, ordinateur)
    print(resultat)

    #quelques details à revoir
    
    # on demande à l'utilisateur s'il veut continuer ou arrêter le jeu
    continuer = input("Voulez-vous continuer ? (oui/non) : ")
    # si le joueur veut arrêter, on sort de la boucle
    if continuer.lower() == "non":
        break
        
#quelques modif a completer
