"""x = int(input("Saisissez un nombre : "))
x = x+1
print(x)"""

saisieInvalide = True
while saisieInvalide:
    try:
        x = int(input("Saisissez un entier : "))
        saisieInvalide = False
    except:
        print("Saisie invalide")
        saisieInvalide = True
    print(f'Nombre saisi : {x}.')