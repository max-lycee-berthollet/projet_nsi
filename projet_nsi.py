debut=input(f"voulez vous debuter le jeu ? oui/non ")
while debut != "oui":
    debut=input(f"voulez vous debuter le jeu ? oui/non ")
intro=("""\nBienvenu dans le jeu du labyrinthe, les règles sont simples:
-des pieces sont disposés dans le labyrinthe, à vous de choisir de les rammaser ou non.
-vous devez rammasser entre 2 et 5 pieces par parties.
-vous devez sortir du labyrinthe avant la fin du temps imparti sous peine de ne plus  jamais en resortir.
Et voila vous connaissez les bases du jeu, à vous de prendre les bonnes descisions.
""")
print(intro)
difficulte=input("quelle difficulte vous correspond ? facile/difficile ")
seconds = time.time()
if difficulte == 'facile':
    while seconds < 360:
        print(seconds)
        time.sleep(15)
else:
    while seconds < 240:
        print(seconds)
        time.sleep(15)

labyrinthe ="""
 _______ x _____________
|  __   ___  |  ___   * |
|__  | | |  ___|_____|  |
|    |_  |*_|  __  |  __|
|  |_ *|_  |  |* | | |*_|
|__  |___| | |  __|_____|
|   ___  |_  |____|     |
|*_|   |_  |____   __|*_|
|  __| |*|__     |___   |
|  |  _|     _|*_|   |  |
|*_|______|__|  ___|____|
"""
print(labyrinthe)
from math import *
px= 1
py= 1
t1="|_  |_|  |"
t2="| |_|    |"
t3="| |___|  |"
t4="| |_| |__|"
while True:
    if py==1:
        for i in range(len(t1)):
            if i == px:
                print("x",end="")
            else:
                print(t1[i], end="")
        print()
        print(t2)
        print(t3)
        print(t4)
    if py==2:
        print(t1)
        for i in range(len(t2)):
            if i == px:
                print("x",end="")
            else:
                print(t2[i], end="")
        print()
        print(t3)
        print(t4)
    if py==3:
        print(t1)
        print(t2)
        for i in range(len(t3)):
            if i==px:
                print("x", end="")
            else:
                print(t3[i], end="")
        print()
        print(t4)
    if py==4:
        print(t1)
        print(t2)
        print(t3)
        for i in range(len(t4)):
            if i==px:
                print("x", end="")
        print(t4)
    if py==4:
        print(t1)
        print(t2)
        print(t3)
        for i in range(len(t4)):
            if i==px:
                print("x",end="")
            else:
                print(t4[i], end="")
    m=int(input("1.haur 2.bas 3.gauche 4.droite "))
    if m==1:
        py-=1
    if m==2:
        py+=1
    if m==3:
        px-=2
    if m==4:
        px+=2
    print()

