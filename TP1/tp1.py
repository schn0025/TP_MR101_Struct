from random import *


def getRandomList(taille: int, mn: int, mx: int) -> list:
    lst = []
    for i in range(taille):
        lst.append(randint(mn, mx - 1))
    return lst
