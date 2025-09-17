import random
from turtle import position

COULEURS = ["bleu", "violet", "vert", "blanc", "jaune", "orange", "noir", "rouge"] 

code_secret = []
for i in range(6):  
    couleur = random.choice(COULEURS)  
    code_secret.append(couleur)

saisie = input("Votre essai : ")
proposition = saisie.split()

bien_places = 0
for i in range(6):
    if proposition[i] == code_secret[i]:
        bien_places += 1
print(bien_places)

secret_restant = []
proposition_restante = []

for i in range(6):
    if proposition[i] != code_secret[i]:
        secret_restant.append(code_secret[i])
        proposition_restante.append(proposition[i])

mal_places = 0
for couleur in proposition_restante:
    if couleur in secret_restant:
        mal_places += 1
        secret_restant.remove(couleur)

print("Bien placés :", bien_places, "| Mal placés :", mal_places)

