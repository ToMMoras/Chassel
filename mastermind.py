import random

COULEURS = ["bleu", "violet", "vert", "blanc", "jaune", "orange", "noir", "rouge"] 

code_secret = []
for i in range(6):  
    couleur = random.choice(COULEURS)  
    code_secret.append(couleur)
