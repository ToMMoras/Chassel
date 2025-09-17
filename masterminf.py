import random

COULEURS = ["R", "V", "B", "J", "M", "N"] 
essai = 1

code_secret = []
for i in range(6):  
    couleur = random.choice(COULEURS)  
    code_secret.append(couleur)

bien_places = 0 


while essai <= 12 and bien_places <6:

    saisie = input("Essai : ")
    proposition = list(saisie)
    
    for i in range(6):
        if proposition[i] == code_secret[i]:
            bien_places +=1

    secret_restant = []
    proposition_restante = []

    for i in range (6):
        if proposition[i] != code_secret[i]:
            secret_restant.append(code_secret[i])
            proposition_restante.append(proposition[i])

    mal_places = 0 
    for couleur in proposition_restante:
        if couleur in secret_restant:
            mal_places += 1 
            secret_restant.remove(couleur)

    essai += 1

    print("Bien placés :", bien_places, "Mal placés :", mal_places)

if bien_places == 6:
    print("Bravo c'est win")
