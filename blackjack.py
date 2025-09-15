import random


argent = 500


cartes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 

print("Tu commences à 500 €")
print("Règles : atteindre 21 sans dépasser. Le joueur gagne si son score est plus proche de 21 que la banque, ou si la banque dépasse 21.")

while argent > 0:
    mise = int(input(f"\nTu as {argent} €. Combien veux-tu miser ? "))

    mes_cartes = [random.choice(cartes), random.choice(cartes)]
    banque_cartes = [random.choice(cartes), random.choice(cartes)]

    print(f"Tes cartes : {mes_cartes}, total = {sum(mes_cartes)}")
    print(f"Carte visible de la banque : {banque_cartes[0]}")

    while sum(mes_cartes) < 21:
        choix = input("Veux-tu tirer une carte ? (oui/non) : ")
        if choix.lower() == "oui":
            mes_cartes.append(random.choice(cartes))
            print(f"Tes cartes : {mes_cartes}, total = {sum(mes_cartes)}")
        else:
            break

    if sum(mes_cartes) > 21:
        print("Tu as dépassé 21 ! LOOOOOOOOOOOOOOSER.")
        argent = argent - mise
        continue

    print(f"Cartes de la banque : {banque_cartes}, total = {sum(banque_cartes)}")
    while sum(banque_cartes) < 17:
        banque_cartes.append(random.choice(cartes))
        print(f"La banque tire : {banque_cartes}, total = {sum(banque_cartes)}")

    score_joueur = sum(mes_cartes)
    score_banque = sum(banque_cartes)

    if score_banque > 21 or score_joueur > score_banque:
        print("Tu gagnes !")
        argent = argent + mise
    elif score_joueur < score_banque:
        print(" LOOOOOOOOOOOOOOOOOOOOOSER !")
        argent = argent - mise
    else:
        print("Égalité, la mise est rendue.")

print("Tu n'as plus d'argent... Fin de la partie.")
