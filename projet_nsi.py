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

