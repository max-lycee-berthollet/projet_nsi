from random import randint
debut = ''
niveauDeFacilite = ''
while debut != 'oui':
  debut=input(f"voulez vous debuter le jeu ? oui/non ")
while True:
  niveauDeFacilite = input('Quel niveau de difficulté ? facile/difficile ')
  if niveauDeFacilite == 'difficile':
    visionHorizontal = 9
    visionVertical = 5
    break
  elif niveauDeFacilite == 'facile':
    visionHorizontal = 13
    visionVertical = 9
    break
labyrintheCarte ="""
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
print(labyrintheCarte)
labyrinthe ="""@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@            o @@            @            @@
@@              @@  o               @      @@
@@    @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@    @@
@@    @      @                        @    @@
@@    @             @       @         @  @@@@
@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @    @@
@@  @@@    @@    o    @         @@    @      
@@    @    @@         @ o       @@  o @    @@ 
@@    @@@  @@   @@@@@@@@@@@@@   @@@@@@@    @@
@@    @         @@         @@   @@    @ @@ @@
@@@@  @         @@         @@   @@    @    @@
@@    @    @@   @@   $$$   @@   @@    @    @@
@@    @    @@   @@         @@         @@@  @@
@@    @  o @@   @@         @@         @    @@
@@  @@@@@@@@@   @@@@@   @@@@@   @@    @    @@
@@    @    @@  o                @@  @@@    @@
@@    @    @@@@@@@@@@@@@@@@@@@@@@@    @ @@ @@
@@ @@ @                      @        @    @@
@@    @  o           @                @    @@
@@    @@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@  @@@@
@@                         @@              @@
@@  o    @                 @@     o  @@    @@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""".split("\n")
labyrinthe = [list(ligne) for ligne in labyrinthe]
nbPiece = 0
tresor = 0
px= 4
py= 0
sac = []
position = [i for i in range(1,25)] #liste qui contient toutes les positions y
while True:
  if py != 0:
    indiceY=py-2
  else:
    indiceY=py
  for i in range(visionVertical):
    if px >= 4:
      indiceX=px-4
    else:
      indiceX=0
    for j in range(visionHorizontal):
      #print(indiceY, indiceX)
      if indiceY == py and indiceX == px:
        print('x',end="")
        visionHorizontal-=1
        indiceX+=1
      print(labyrinthe[indiceY][indiceX], end="")
      indiceX+=1
    print()
    indiceY+=1

  deplacement = False #booléen pour savoir si un deplacement a été effectué ou non pour continuer la boucle si mur
  while deplacement == False:
      if (px!=46 or py!=8):
              m=input("z.haut s.bas q.gauche d.droite c.carte ")
              if m=='z':
                  if labyrinthe[py-1][px] == '@':
                    print('deplacement impossible : mur')
                  else:
                    py-=1
                    deplacement = True
              if m=='s':
                if labyrinthe[py+1][px] == '@':
                  print("deplacement impossible : mur")
                else:
                  py+=1
                  deplacement = True
              if m=='q':
                if labyrinthe[py][px-1] == '@':
                  print('deplacement impossible : mur')
                else:
                  px-=1
                  deplacement = True
              if m=='d':
                if labyrinthe[py][px+1] == '@':
                  print('deplacement impossible : mur')
                else:
                  px+=1
                  deplacement = True
              if m=='c':
                  print(labyrintheCarte)
              print()

  bonus=[]                              #liste des bonus a définir
  if labyrinthe[py][px] == 'o':
      booster=bonus[randint(len(bonus))] #donne a booster le bonus pour pouvoir le print et l'ajouter au sac a dos
      print('Bonus trouvé !!', booster) #choisi un bonus au hazard et lui donne
      sac.append(booster)
      labyrinthe[py][px]= ' '
