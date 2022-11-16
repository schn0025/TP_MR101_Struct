from random import *


def getRandomList(taille: int, mn: int, mx: int) -> list:
    lst = []
    for i in range(taille):
        lst.append(randint(mn, mx - 1))
    return lst

def compter(lst: list, elmt: int) -> int:
    nb = 0
    for e in lst:
        if e == elmt:
            nb += 1
    return nb
