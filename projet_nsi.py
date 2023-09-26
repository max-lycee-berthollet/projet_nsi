debut=input(f"voulez vous debuter le jeu ? oui/non ")
while debut != "oui":
    debut=input(f"voulez vous debuter le jeu ? oui/non ")
intro=("""\nBienvenu dans le jeu du labyrinthe, les règles sont simples:
-des bonus sont disposés dans le labyrinthe, à vous de choisir de les rammaser ou non, ils peuvent vous aider ou pas.
-vous ne pouvez rammaser que 5 bonus par parties.
-vous devez sortir du labyrinthe avant la fin du temps impartie sous peine de ne plus  jamais en resortir.
Et voila vous connaissez les bases du jeu, à vous de prendre les bonnes descisions.
""")
print(intro)
difficulte=input("quelle difficule vous correspond ? facile/difficile ")
if difficulte=="facile":
    rtr
elif difficulte=="difficile":
    hij


labyrinthe ="""
 _______ x _____________
|  __   ___  |  ___     |
|__  | | |  ___|_____|  |
|    |_  |_|  __  |   __|
|  |_  |_  | |  | |  |  |
|__  |___| | |   _|_____|
|   ___  |_  |____|     |
|__|   |_  |____   __|__|
|  __| | |__    |____   |
| |   _|     _|_|    |  |
|_|______|__|______|____|
"""
print(labyrinthe)
