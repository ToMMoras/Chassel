import random as r


def plus_petitgrang():
    niv= int(input("niveau 1 à 3"))
    if niv == 1:
        niv_1()
    elif niv==2:
        niv_2()
    else:
        niv_3()


def niv_1():
    pt = 10
    c = r.randint(1,100)
    boo=True
    nb= 0
    while boo and pt>0:
        try:
            nb = int(input("tu choisis quoi :"))
            if nb>c:
                print ("inférieur, prends -1point")
                pt-=1
            elif nb<c:
                print ("supérieur, prends -1point")
                pt-=1
            else: 
                boo=False
        except:
            print("reesaye")
    print("votre score",pt, "la réponse",c)


def niv_2():
    pt = 30
    c = r.randint(1,1000)
    boo=True
    nb= 0
    while boo and pt>0:
        try:
            nb = int(input("tu choisis quoi :"))
            if nb>c:
                print ("inférieur, prends -1point")
                pt-=1
            elif nb<c:
                print ("supérieur, prends -1point")
                pt-=1
            else: 
                boo=False
        except:
            print("reesaye")
    print("votre score",pt, "la réponse",c)



def niv_3():
    pt = 80
    c = r.randint(1,10000)
    boo=True
    nb= 0
    while boo and pt>0:
        try:
            nb = int(input("tu choisis quoi :"))
            if nb>c:
                print ("inférieur, prends -1point")
                pt-=1
            elif nb<c:
                print ("supérieur, prends -1point")
                pt-=1
            else: 
                boo=False
        except:
            print("reesaye")
    print("votre score",pt, "la réponse",c)

    
plus_petitgrang()