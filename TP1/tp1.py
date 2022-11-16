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


def contient(lst: list, nb: int) -> bool:
    rep = False
    i = 0
    while not rep and i < len(lst):
        if lst[i] == nb:
            rep = True
        i += 1
    return rep


def firstIndexOf(lst: list, nb: int) -> int:
    i = 0
    while i < len(lst) and lst[i] != nb:
        i += 1
    if i == len(lst):
        i = -1
    return i


def lastIndexOf(lst: list, nb: int) -> int:
    id = -1
    for i in range(len(lst)):
        if lst[i] == nb:
            id = i
    return id


def nthIndexOf(lst: list, n: int, elmt: int) -> int:
    i = 0
    nb = 0
    id = -1
    while i < len(lst) and nb < n:
        if lst[i] == elmt:
            nb += 1
            if nb == n:
                id = i
        i += 1
    if n < nb:
        id = -1
    return id


def creerListeSansDoublon(lst: list) -> list:
    lstTemp=lst
    lstRep = []
    while lstTemp:
        nb = lstTemp.pop(0)
        if compter(lstTemp, nb) == 0:
            lstRep.append(nb)
        else:
            while compter(lstTemp, nb) > 0:
                lstTemp.pop(lastIndexOf(lstTemp, nb))
            lstRep.append(nb)

    return lst

def supprimerDoublons(lst: list) -> None:
    i = 0
    while i < len(lst):
        while firstIndexOf(lst, lst[i]) != lastIndexOf(lst, lst[i]):
            del lst[lastIndexOf(lst, lst[i])]
        i += 1
    return None