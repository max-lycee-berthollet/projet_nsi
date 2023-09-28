from time import *
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
seconds = time()
if difficulte == 'facile':
    while seconds < 360:
        print(seconds)
        time.sleep(15)
else:
    while seconds < 240:
        print(seconds)
        time.sleep(15)

labyrinthe ="""
@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@              @@                         @@
@@              @@                         @@
@@    @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@    @@
@@    @                               @    @@
@@    @                               @    @@
@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@
@@    @    @@         @         @@    @      
@@    @    @@         @         @@    @      
@@    @    @@   @@@@@@@@@@@@@   @@@@@@@    @@
@@    @         @@         @@   @@    @    @@
@@    @         @@         @@   @@    @    @@
@@    @    @@   @@   $$$   @@   @@    @    @@
@@    @    @@   @@         @@         @    @@
@@    @    @@   @@         @@         @    @@
@@    @@@@@@@   @@@@@   @@@@@   @@    @    @@
@@    @    @@                   @@    @    @@
@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@
@@    @                               @    @@
@@    @                               @    @@
@@    @@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@    @@
@@                         @@              @@
@@                         @@              @@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
print(labyrinthe)
from math import *
px= 5
py= 1
t1="@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
t2="@@              @@                         @@"
t3="@@              @@                         @@"
t4="@@    @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@    @@"
t5="@@    @                               @    @@"
t6="@@    @                               @    @@"
t7="@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@"
t8="@@    @    @@         @         @@    @      "
t9="@@    @    @@         @         @@    @      "
t10="@@    @    @@   @@@@@@@@@@@@@   @@@@@@@    @@"
t11="@@    @         @@         @@   @@    @    @@"
t12="@@    @         @@         @@   @@    @    @@"
t13="@@    @    @@   @@   $$$   @@   @@    @    @@"
t14="@@    @    @@   @@         @@         @    @@"
t15="@@    @    @@   @@         @@         @    @@"
t16="@@    @@@@@@@   @@@@@   @@@@@   @@    @    @@"
t17="@@    @    @@                   @@    @    @@"
t18="@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@"
t19="@@    @                               @    @@"
t20="@@    @                               @    @@"
t21="@@    @@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@    @@"
t22="@@                         @@              @@"
t23="@@                         @@              @@"
t24="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
while True:
    if py==1:
        for i in range(len(t1)):
            if i == px:
                print("`",end="")
            else:
                print(t1[i], end="")
        print()
        print(t2)
        print(t3)            ##boucle?
        print(t4)
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
    if py==2:
        print(t1)
        for i in range(len(t2)):
            if i == px:
                print("`",end="")
            else:
                print(t2[i], end="")
        print()
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
    if py==3:
        print(t1)
        print(t2)
        for i in range(len(t3)):
            if i==px:
                print("`", end="")
            else:
                print(t3[i], end="")
        print()
        print(t4)
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
    if py==4:
        print(t1)
        print(t2)
        print(t3)
        for i in range(len(t4)):
            if i==px:
                print("`", end="")
        print()
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
    if py==5:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        for i in range(len(t5)):
            if i==px:
                print("`",end="")
            else:
                print(t4[i], end="")
        print()
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
    if py==6:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        for i in range(len(t6)):
            if i==px:
                print("`",end="")
            else:
                print(t4[i], end="")
        print()
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
    if py==7:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        for i in range(len(t7)):
            if i==px:
                print("`",end="")
            else:
                print(t4[i], end="")
        print()
        print(t8)
        print(t9)
        print(t10)
        print(t11)
    if py==8:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        print(t7)
        for i in range(len(t8)):
            if i==px:
                print("`",end="")
            else:
                print(t4[i], end="")
        print()
        print(t9)
        print(t10)
        print(t11)
    if py==9:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        for i in range(len(t9)):
            if i==px:
                print("`",end="")
            else:
                print(t4[i], end="")
        print()
        print(t10)
        print(t11)
    if py==10:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        for i in range(len(t10)):
            if i==px:
                print("`",end="")
            else:
                print(t4[i], end="")
        print()
        print(t11)
    if py==11:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        for i in range(len(t11)):
            if i==px:
                print("`",end="")
            else:
                print(t4[i], end="")
        print()
    m=int(input("1.haut 2.bas 3.gauche 4.droite "))
    if m==1:
        py-=1
    if m==2:
        py+=1
    if m==3:
        px-=2
    if m==4:
        px+=2
    print()

