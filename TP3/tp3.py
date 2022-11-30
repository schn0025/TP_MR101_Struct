# renvois le premeir indice de la valeur val
def indexOf(lst: list, val: int) -> int:
    i = 0
    while i < len(lst) and lst[i] != val:
        i += 1
    if i == len(lst):
        i = -1
    return i

# recherche de val classique
def indexOfSorted(lst: list, val: int) -> tuple:
    i = 0
    while i < len(lst) and lst[i] < val:
        i += 1
    rep = i
    if i == len(lst):
        rep = -1
    elif lst[i] > val:
        rep = -1
    return rep, i

# recherche dichotomies
def binarySearch(lst: list, val: float) -> int:
    ideb = 0
    ifin = len(lst)-1
    imilieu = (ideb + ifin) // 2
    id = -1
    while ideb <= ifin and id == -1:
        if lst[imilieu] < val:
            ideb = imilieu + 1
        elif lst[imilieu] > val:
            ifin = imilieu - 1
        else:
            id = imilieu
        imilieu = (ideb + ifin) // 2
    return id

# programation du jeu "deviner un nombre"
# création de la fonction de sesie d'un nombre
def getReponse(val :int) -> str:
    print("Proposition de l’ordinateur :", val)
    rep = input("Votre nombre est-il (E)gal, plus (G)rand ou plus (P)etit ?")
    return rep.upper()

# creation du choix de l'ordi

def devinerNombre(mn: int, mx: int) -> int:
    nb = int(input(f'Choisissez un nombre entre {mn} {mx} '))