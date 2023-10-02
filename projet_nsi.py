from time import *
debut=input(f"voulez vous debuter le jeu ? oui/non ")

labyrinthe ="""
@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@            o @@                         @@
@@              @@  o                      @@
@@    @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@    @@
@@    @                               @    @@
@@    @                               @    @@
@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@
@@    @    @@    o    @         @@    @      
@@    @    @@         @ o       @@  o @    @@ 
@@    @    @@   @@@@@@@@@@@@@   @@@@@@@    @@
@@    @         @@         @@   @@    @    @@
@@    @         @@         @@   @@    @    @@
@@    @    @@   @@   $$$   @@   @@    @    @@
@@    @    @@   @@         @@         @    @@
@@    @  o @@   @@         @@         @    @@
@@    @@@@@@@   @@@@@   @@@@@   @@    @    @@
@@    @    @@  o                @@    @    @@
@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@
@@    @                               @    @@
@@    @  o                            @    @@
@@    @@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@    @@
@@                         @@              @@
@@  o                      @@     o        @@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
print(labyrinthe)
while debut != "oui":
    debut=input(f"voulez vous debuter le jeu ? oui/non ")
intro=("""\nBienvenu dans le jeu du labyrinthe, les règles sont simples:
-des pieces sont disposés dans le labyrinthe, à vous de choisir de les rammaser ou non.
-vous devez rammasser entre 2 et 5 pieces par parties.
-attention a ne pas touchez les murs sinon vous mourez.
-vous devez sortir du labyrinthe avant la fin du temps imparti sous peine de ne plus jamais en resortir.
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

from math import *
px= 4
py= 1
t1="@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
t2="@@            o @@                         @@"
t3="@@              @@  o                      @@"
t4="@@    @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@    @@"
t5="@@    @                               @    @@"
t6="@@    @                               @    @@"
t7="@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@"
t8="@@    @    @@    o    @         @@    @             "
t9="@@    @    @@         @ o       @@  o @    @@"
t10="@@    @    @@   @@@@@@@@@@@@@   @@@@@@@    @@"
t11="@@    @         @@         @@   @@    @    @@"
t12="@@    @         @@         @@   @@    @    @@"
t13="@@    @    @@   @@   $$$   @@   @@    @    @@"
t14="@@    @    @@   @@         @@         @    @@"
t15="@@    @  o @@   @@         @@         @    @@"
t16="@@    @@@@@@@   @@@@@   @@@@@   @@    @    @@"
t17="@@    @    @@  o                @@    @    @@"
t18="@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@"
t19="@@    @                               @    @@"
t20="@@    @  o                            @    @@"
t21="@@    @@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@    @@"
t22="@@                         @@              @@"
t23="@@  o                      @@     o        @@"
t24="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
nb_pieces=0
while True:
    if py==1:
        for i in range(len(t1)):
            if i == px:
                print("x",end="")
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
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
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
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
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
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==4:
        print(t1)
        print(t2)
        print(t3)
        for i in range(len(t4)):
            if i==px:
                print("x", end="")
            else:
                print(t4[i], end="")
        print()
        print(t5)
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==5:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        for i in range(len(t5)):
            if i==px:
                print("x",end="")
            else:
                print(t5[i], end="")
        print()
        print(t6)
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==6:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        for i in range(len(t6)):
            if i==px:
                print("x",end="")
            else:
                print(t6[i], end="")
        print()
        print(t7)
        print(t8)
        print(t9)
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==7:
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        print(t5)
        print(t6)
        for i in range(len(t7)):
            if i==px:
                print("x",end="")
            else:
                print(t7[i], end="")
        print()
        print(t8)
        print(t9)
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
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
                print("x",end="")
            else:
                print(t8[i], end="")
        print()
        print(t9)
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
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
                print("x",end="")
            else:
                print(t9[i], end="")
        print()
        print(t10)
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
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
                print("x",end="")
            else:
                print(t10[i], end="")
        print()
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
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
                print("x",end="")
            else:
                print(t11[i], end="")
        print()
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==12:
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
        print(t11)
        for i in range(len(t12)):
            if i==px:
                print("x",end="")
            else:
                print(t12[i], end="")
        print()
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==13:
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
        print(t11)
        print(t12)
        for i in range(len(t13)):
            if i==px:
                print("x",end="")
            else:
                print(t13[i], end="")
        print()
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==14:
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
        print(t11)
        print(t12)
        print(t13)
        for i in range(len(t14)):
            if i==px:
                print("x",end="")
            else:
                print(t14[i], end="")
        print()
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==15:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        for i in range(len(t15)):
            if i==px:
                print("x",end="")
            else:
                print(t15[i], end="")
        print()
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==16:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        for i in range(len(t16)):
            if i==px:
                print("x",end="")
            else:
                print(t16[i], end="")
        print()
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==17:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        for i in range(len(t17)):
            if i==px:
                print("x",end="")
            else:
                print(t17[i], end="")
        print()
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==18:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        for i in range(len(t18)):
            if i==px:
                print("x",end="")
            else:
                print(t18[i], end="")
        print()
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==19:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        for i in range(len(t19)):
            if i==px:
                print("x",end="")
            else:
                print(t19[i], end="")
        print()
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==20:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        for i in range(len(t20)):
            if i==px:
                print("x",end="")
            else:
                print(t20[i], end="")
        print()
        print(t21)
        print(t22)
        print(t23)
        print(t24)
    if py==21:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        for i in range(len(t21)):
            if i==px:
                print("x",end="")
            else:
                print(t21[i], end="")
        print()
        print(t22)
        print(t23)
        print(t24)
    if py==22:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        for i in range(len(t22)):
            if i==px:
                print("x",end="")
            else:
                print(t22[i], end="")
        print()
        print(t23)
        print(t24)
    if py==23:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        for i in range(len(t23)):
            if i==px:
                print("x",end="")
            else:
                print(t23[i], end="")
        print()
        print(t24)
    if py==24:
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
        print(t11)
        print(t12)
        print(t13)
        print(t14)
        print(t15)
        print(t16)
        print(t17)
        print(t18)
        print(t19)
        print(t20)
        print(t21)
        print(t22)
        print(t23)
        for i in range(len(t24)):
            if i==px:
                print("x",end="")
            else:
                print(t24[i], end="")
        print()
        
        
    if (py==2 and px==14) or (py==3 and px==20) or (py==8 and px==17) or (py==9 and px==24) or (py==9 and px==35) or (py==15 and px==9) or (py==17 and px==15) or (py==20 and px==9) or (py==23 and px==4) or (py==23 and px==34):
        nb_pieces+=1
    tresor=0
    if (px==22 and py==13) or (px==21 and py==13) or (px==23 and py==13):
        tresor+=1
    if tresor == 1:
        print('vous avez obtenu le trésor')
    if nb_pieces >= 1:
        print('nombres de piece(s)',nb_pieces)
        
    if (px==46 and py==8):
        sortir=input("bonjour jeune voyageur, souhaites tu sortir de ce labyrinthe ? oui/non ")
        while sortir!="oui" and sortir!="non":
            sortir=input("bonjour jeune voyageur, souhaites tu sortir de ce labyrinthe ? oui/non ")
        if sortir=="oui":
            print("Montre moi tes pieces...")
            if nb_pieces >= 7 and tresor==1:
                assez_de_piece=input(f"Tu possèdes {nb_pieces} pieces et {tresor} trésor. Souhaite tu me les echanger contre ta libertée ? oui/non ")
                while assez_de_piece!= "oui" and assez_de_piece!="non":
                    assez_de_piece=input(f"Tu possèdes {nb_pieces} pieces et {tresor} trésor. Souhaite tu me les echanger contre ta libertée ? oui/non ")
                if assez_de_piece=="oui":
                    print("C'est parfait tu es libre maintenant... \nBon voyage!!!")
                elif assez_de_piece=="non":
                    print("C'est bien dommage, revient me voir quand tu aura envie de sortir d'ici")
            elif nb_pieces < 7:
                print(f"Tu possède {nb_pieces} pieces et {tresor} trésor. Tu n'en possède pas assez, reviens me voir quand tu aura au moins 7 piece et 1 trésor.")
        if sortir=="non":
            print("Tres bien, bon voyage à toi et reviens me voir si l'envie de sortir te prend. ")
    else:
        print ("")
        
    
    

    m=input("z.haut s.bas q.gauche d.droite ")

    if m=='z':
        py-=1
    if m=='s':
        py+=1
    if m=='q':
        px-=1
    if m=='d':
        px+=1
    print()

#c'est la place des murs pour ensuite pouvoir faire en sorte que quand le personnage rentre dans un mur il retourne au debut 

if (px==1 and py==1) or \
   (px==1 and py==2) or \
   (px==1 and py==7) or \
   (px==1 and py==8) or \
   (px==1 and py==9) or \
   (px==1 and py==10) or \
   (px==1 and py==11) or \
   (px==1 and py==12) or \
   (px==1 and py==13) or \
   (px==1 and py==14) or \
   (px==1 and py==15) or \
   (px==1 and py==16) or \
   (px==1 and py==17) or \
   (px==1 and py==18) or \
   (px==1 and py==19) or \
   (px==1 and py==20) or \
   (px==1 and py==21) or \
   (px==1 and py==22) or \
   (px==1 and py==23) or \
   (px==1 and py==24) or \
   (px==1 and py==25) or \
   (px==1 and py==26) or \
   (px==1 and py==27) or \
   (px==1 and py==28) or \
   (px==1 and py==29) or \
   (px==1 and py==30) or \
   (px==1 and py==31) or \
   (px==1 and py==32) or \
   (px==1 and py==33) or \
   (px==1 and py==34) or \
   (px==1 and py==35) or \
   (px==1 and py==36) or \
   (px==1 and py==37) or \
   (px==1 and py==38) or \
   (px==1 and py==39) or \
   (px==1 and py==40) or \
   (px==1 and py==41) or \
   (px==1 and py==42) or \
   (px==1 and py==43) or \
   (px==1 and py==44) or \
   (px==1 and py==45) or \
   (px==2 and py==1) or \
   (px==2 and py==2) or \
   (px==2 and py==17) or \
   (px==2 and py==18) or \
   (px==2 and py==44) or \
   (px==2 and py==45) or \
   (px==3 and py==1) or \
   (px==3 and py==2) or \
   (px==3 and py==17) or \
   (px==3 and py==18) or \
   (px==3 and py==44) or \
   (px==3 and py==45) or \
   (px==4 and py==1) or \
   (px==4 and py==2) or \
   (px==4 and py==7) or \
   (px==4 and py==8) or \
   (px==4 and py==9) or \
   (px==4 and py==10) or \
   (px==4 and py==11) or \
   (px==4 and py==12) or \
   (px==4 and py==13) or \
   (px==4 and py==14) or \
   (px==4 and py==15) or \
   (px==4 and py==16) or \
   (px==4 and py==17) or \
   (px==4 and py==18) or \
   (px==4 and py==19) or \
   (px==4 and py==20) or \
   (px==4 and py==21) or \
   (px==4 and py==22) or \
   (px==4 and py==23) or \
   (px==4 and py==24) or \
   (px==4 and py==25) or \
   (px==4 and py==26) or \
   (px==4 and py==27) or \
   (px==4 and py==28) or \
   (px==4 and py==30) or \
   (px==4 and py==33) or \
   (px==4 and py==34) or \
   (px==4 and py==35) or \
   (px==4 and py==36) or \
   (px==4 and py==37) or \
   (px==4 and py==38) or \
   (px==4 and py==39) or \
   (px==4 and py==44) or \
   (px==4 and py==45) or \
   (px==5 and py==1) or \
   (px==5 and py==2) or \
   (px==5 and py==7) or \
   (px==5 and py==39) or \
   (px==5 and py==44) or \
   (px==5 and py==45) or \
   (px==6 and py==1) or \
   (px==6 and py==2) or \
   (px==6 and py==7) or \
   (px==6 and py==39) or \
   (px==6 and py==44) or \
   (px==6 and py==45) or \
   (px==7 and py==1) or \
   (px==7 and py==2) or \
   (px==7 and py==7) or \
   (px==7 and py==12) or \
   (px==7 and py==13) or \
   (px==7 and py==14) or \
   (px==7 and py==15) or \
   (px==7 and py==16) or \
   (px==7 and py==17) or \
   (px==7 and py==18) or \
   (px==7 and py==19) or \
   (px==7 and py==20) or \
   (px==7 and py==21) or \
   (px==7 and py==22) or \
   (px==7 and py==23) or \
   (px==7 and py==24) or \
   (px==7 and py==25) or \
   (px==7 and py==26) or \
   (px==7 and py==27) or \
   (px==7 and py==28) or \
   (px==7 and py==29) or \
   (px==7 and py==30) or \
   (px==7 and py==31) or \
   (px==7 and py==32) or \
   (px==7 and py==33) or \
   (px==7 and py==34) or \
   (px==7 and py==39) or \
   (px==7 and py==44) or \
   (px==7 and py==45) or \
   (px==8 and py==1) or \
   (px==8 and py==2) or \
   (px==8 and py==7) or \
   (px==8 and py==12) or \
   (px==8 and py==13) or \
   (px==8 and py==23) or \
   (px==8 and py==33) or \
   (px==8 and py==34) or \
   (px==8 and py==39) or \
   (px==9 and py==1) or \
   (px==9 and py==2) or \
   (px==9 and py==7) or \
   (px==9 and py==12) or \
   (px==9 and py==13) or \
   (px==9 and py==23) or \
   (px==9 and py==33) or \
   (px==9 and py==34) or \
   (px==9 and py==39) or \
   (px==10 and py==1) or \
   (px==10 and py==2) or \
   (px==10 and py==7) or \
   (px==10 and py==12) or \
   (px==10 and py==13) or \
   (px==10 and py==14) or \
   (px==10 and py==15) or \
   (px==10 and py==16) or \
   (px==10 and py==17) or \
   (px==10 and py==18) or \
   (px==10 and py==19) or \
   (px==10 and py==20) or \
   (px==10 and py==21) or \
   (px==10 and py==22) or \
   (px==10 and py==23) or \
   (px==10 and py==24) or \
   (px==10 and py==25) or \
   (px==10 and py==26) or \
   (px==10 and py==27) or \
   (px==10 and py==28) or \
   (px==10 and py==29) or \
   (px==10 and py==33) or \
   (px==10 and py==34) or \
   (px==10 and py==35) or \
   (px==10 and py==36) or \
   (px==10 and py==37) or \
   (px==10 and py==38) or \
   (px==10 and py==39) or \
   (px==10 and py==44) or \
   (px==10 and py==45) or \
   (px==11 and py==1) or \
   (px==11 and py==2) or \
   (px==11 and py==7) or \
   (px==11 and py==17) or \
   (px==11 and py==18) or \
   (px==11 and py==28) or \
   (px==11 and py==29) or \
   (px==11 and py==33) or \
   (px==11 and py==34) or \
   (px==11 and py==39) or \
   (px==11 and py==44) or \
   (px==11 and py==45) or \
   (px==12 and py==1) or \
   (px==12 and py==2) or \
   (px==12 and py==7) or \
   (px==12 and py==17) or \
   (px==12 and py==18) or \
   (px==12 and py==28) or \
   (px==12 and py==29) or \
   (px==12 and py==33) or \
   (px==12 and py==34) or \
   (px==12 and py==39) or \
   (px==12 and py==44) or \
   (px==12 and py==45) or \
   (px==13 and py==1) or \
   (px==13 and py==2) or \
   (px==13 and py==7) or \
   (px==13 and py==12) or \
   (px==13 and py==13) or \
   (px==13 and py==17) or \
   (px==13 and py==18) or \
   (px==13 and py==28) or \
   (px==13 and py==29) or \
   (px==13 and py==33) or \
   (px==13 and py==34) or \
   (px==13 and py==39) or \
   (px==13 and py==44) or \
   (px==13 and py==45) or \
   (px==14 and py==1) or \
   (px==14 and py==2) or \
   (px==14 and py==7) or \
   (px==14 and py==12) or \
   (px==14 and py==13) or \
   (px==14 and py==17) or \
   (px==14 and py==18) or \
   (px==14 and py==28) or \
   (px==14 and py==29) or \
   (px==14 and py==39) or \
   (px==14 and py==44) or \
   (px==14 and py==45) or \
   (px==15 and py==1) or \
   (px==15 and py==2) or \
   (px==15 and py==7) or \
   (px==15 and py==12) or \
   (px==15 and py==13) or \
   (px==15 and py==17) or \
   (px==15 and py==18) or \
   (px==15 and py==28) or \
   (px==15 and py==29) or \
   (px==15 and py==39) or \
   (px==15 and py==44) or \
   (px==15 and py==45) or \
   (px==16 and py==1) or \
   (px==16 and py==2) or \
   (px==16 and py==7) or \
   (px==16 and py==8) or \
   (px==16 and py==9) or \
   (px==16 and py==10) or \
   (px==16 and py==11) or \
   (px==16 and py==12) or \
   (px==16 and py==13) or \
   (px==16 and py==17) or \
   (px==16 and py==18) or \
   (px==16 and py==19) or \
   (px==16 and py==20) or \
   (px==16 and py==21) or \
   (px==16 and py==25) or \
   (px==16 and py==26) or \
   (px==16 and py==27) or \
   (px==16 and py==28) or \
   (px==16 and py==29) or \
   (px==16 and py==33) or \
   (px==16 and py==34) or \
   (px==16 and py==39) or \
   (px==16 and py==44) or \
   (px==16 and py==45) or \
   (px==17 and py==1) or \
   (px==17 and py==2) or \
   (px==17 and py==7) or \
   (px==17 and py==12) or \
   (px==17 and py==13) or \
   (px==17 and py==33) or \
   (px==17 and py==34) or \
   (px==17 and py==39) or \
   (px==17 and py==44) or \
   (px==17 and py==45) or \
   (px==18 and py==1) or \
   (px==18 and py==2) or \
   (px==18 and py==7) or \
   (px==18 and py==12) or \
   (px==18 and py==13) or \
   (px==18 and py==14) or \
   (px==18 and py==15) or \
   (px==18 and py==16) or \
   (px==18 and py==17) or \
   (px==18 and py==18) or \
   (px==18 and py==19) or \
   (px==18 and py==20) or \
   (px==18 and py==21) or \
   (px==18 and py==22) or \
   (px==18 and py==23) or \
   (px==18 and py==24) or \
   (px==18 and py==25) or \
   (px==18 and py==26) or \
   (px==18 and py==27) or \
   (px==18 and py==28) or \
   (px==18 and py==29) or \
   (px==18 and py==30) or \
   (px==18 and py==31) or \
   (px==18 and py==32) or \
   (px==18 and py==33) or \
   (px==18 and py==34) or \
   (px==18 and py==39) or \
   (px==18 and py==44) or \
   (px==18 and py==45) or \
   (px==19 and py==1) or \
   (px==19 and py==2) or \
   (px==19 and py==7) or \
   (px==19 and py==39) or \
   (px==19 and py==44) or \
   (px==19 and py==45) or \
   (px==20 and py==1) or \
   (px==20 and py==2) or \
   (px==20 and py==7) or \
   (px==20 and py==39) or \
   (px==20 and py==44) or \
   (px==20 and py==45) or \
   (px==21 and py==1) or \
   (px==21 and py==2) or \
   (px==21 and py==7) or \
   (px==21 and py==8) or \
   (px==21 and py==9) or \
   (px==21 and py==10) or \
   (px==21 and py==11) or \
   (px==21 and py==12) or \
   (px==21 and py==13) or \
   (px==21 and py==17) or \
   (px==21 and py==18) or \
   (px==21 and py==19) or \
   (px==21 and py==20) or \
   (px==21 and py==21) or \
   (px==21 and py==22) or \
   (px==21 and py==23) or \
   (px==21 and py==24) or \
   (px==21 and py==25) or \
   (px==21 and py==26) or \
   (px==21 and py==27) or \
   (px==21 and py==28) or \
   (px==21 and py==29) or \
   (px==21 and py==30) or \
   (px==21 and py==31) or \
   (px==21 and py==32) or \
   (px==21 and py==33) or \
   (px==21 and py==34) or \
   (px==21 and py==35) or \
   (px==21 and py==36) or \
   (px==21 and py==37) or \
   (px==21 and py==38) or \
   (px==21 and py==39) or \
   (px==21 and py==44) or \
   (px==21 and py==45) or \
   (px==22 and py==1) or \
   (px==22 and py==2) or \
   (px==22 and py==28) or \
   (px==22 and py==29) or \
   (px==22 and py==44) or \
   (px==22 and py==45) or \
   (px==23 and py==1) or \
   (px==23 and py==2) or \
   (px==23 and py==28) or \
   (px==23 and py==29) or \
   (px==23 and py==44) or \
   (px==23 and py==45) or \
   (px==24 and py==1) or \
   (px==24 and py==2) or \
   (px==24 and py==3) or \
   (px==24 and py==4) or \
   (px==24 and py==5) or \
   (px==24 and py==6) or \
   (px==24 and py==7) or \
   (px==24 and py==8) or \
   (px==24 and py==9) or \
   (px==24 and py==10) or \
   (px==24 and py==11) or \
   (px==24 and py==12) or \
   (px==24 and py==13) or \
   (px==24 and py==14) or \
   (px==24 and py==15) or \
   (px==24 and py==16) or \
   (px==24 and py==17) or \
   (px==24 and py==18) or \
   (px==24 and py==19) or \
   (px==24 and py==20) or \
   (px==24 and py==21) or \
   (px==24 and py==22) or \
   (px==24 and py==23) or \
   (px==24 and py==24) or \
   (px==24 and py==25) or \
   (px==24 and py==26) or \
   (px==24 and py==27) or \
   (px==24 and py==28) or \
   (px==24 and py==29) or \
   (px==24 and py==30) or \
   (px==24 and py==31) or \
   (px==24 and py==32) or \
   (px==24 and py==33) or \
   (px==24 and py==34) or \
   (px==24 and py==35) or \
   (px==24 and py==36) or \
   (px==24 and py==37) or \
   (px==24 and py==38) or \
   (px==24 and py==39) or \
   (px==24 and py==40) or \
   (px==24 and py==41) or \
   (px==24 and py==42) or \
   (px==24 and py==43) or \
   (px==24 and py==44) or \
   (px==24 and py==45):
       px==1; py==4
