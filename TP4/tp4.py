from random import *


def getRegularArray2D(nl: int, nc: int, mn: int, mx: int) -> list:
    tab = []
    for i in range(nl):
        lignes = []
        for y in range(nc):
            val = round(random() * (mx - mn) + mn)
            lignes.append(val)
        tab.append(lignes)
    return tab


def isRegular(tab: list) -> bool:
    i = 0
    reg = True
    while i < len(tab) - 1 and reg:
        if len(tab[i]) != len(tab[i + 1]):
            reg = False
        i += 1
    return reg


def getMin(tab: list) -> float:
    mini = min(tab[0])
    for elt in tab:
        miniTemp = min(elt)
        if mini > miniTemp:
            mini = miniTemp
    return mini


def getMax(tab: list) -> float:
    maxi = max(tab[0])
    for elt in tab:
        maxiTemp = max(elt)
        if maxi < maxiTemp:
            maxi = maxiTemp
    return maxi


def getSize2D(tab: list) -> tuple:
    nbLingne = len(tab)
    nbCol = len(tab[0])
    return (nbLingne, nbCol)

