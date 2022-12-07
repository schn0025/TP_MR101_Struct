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
def getReponse(val: int) -> str:
    print("Proposition de l’ordinateur :", val)
    rep = input("Votre nombre est-il (E)gal, plus (G)rand ou plus (P)etit ?")
    return rep.upper()

# creation du choix de l'ordi

def devinerNombre(mn: int, mx: int, lst: list = None) -> bool:
    nb = mn - 1
    idDeb = mn
    idFin = mx
    trouver = False
    while nb < mn or nb > mx:
        nb = int(input(f'Choisissez un nombre entre {mn} {mx} '))
    posible = ['P', 'E', 'G']
    c = (idDeb+idFin)//2
    n = 1
    rep = 'pas de rep'
    while rep != 'E' and idDeb <= idFin:
        rep = 'pas de rep'
        while rep not in posible:
            rep = (getReponse(c)).upper()
        couple = (c, rep)
        if lst is not None:
            lst.append(couple)
        if rep == 'P':
            idFin = c - 1
        elif rep == 'G':
            idDeb = c + 1
        else:
            trouver = True
        c = (idDeb + idFin) // 2
        n += 1
    print(lst)
    return trouver

# b) verification

def demanderReponse() -> int:
    rep = int(input("quel nombre avez-vous choisi? "))
    return rep

def verifierIntervalle(mn, mx, n) -> bool:
    ilEst = False
    if n < mx and n > mn:
        ilEst = True
    else:
        print(f"Le nombre {n} choisi n’est pas compris dans l’intervalle [{mn}, {mx}] ")
    return ilEst

def verifierReponses(lst: list, n: int) -> bool:
    ok = True
    i = 0
    while i < len(lst) and ok:
        elt = lst[i]
        nb = elt[0]
        if nb < n:
            bonneRep = 'G'
        elif nb > n:
            bonneRep = 'P'
        else:
            bonneRep = "E"

        if elt[1] != bonneRep:
            print(f"Lors de la proposition du nombre {elt[0]}, vous avez répondu {elt[1]} alors que c’était {bonneRep}")
            ok = False
        i += 1
    return ok

def deviner(mn: int, mx: int) -> None:
    lst = []
    idMin = mn
    idMax = mx
    if not devinerNombre(idMin, idMax, lst):
        n = demanderReponse()
        if verifierIntervalle(mn, mx, n):
            verifierReponses(lst, n)
    return None
