from random import *

def getRegularArray2D(nl: int, nc: int, mn: int, mx: int) -> list:
    lst = []
    for i in range(nl):
        lignes = []
        for y in range(nc):
            val = round(random()*(mx-mn)+mn)
            lignes.append(val)
        lst.append(lignes)
    return lst

def isRegular(lst: list) -> bool:
    i = 0
    reg = True
    while i < len(lst)-1 and reg:
        if len(lst[i]) != len(lst[i+1]):
            reg = False
        i += 1
    return reg
