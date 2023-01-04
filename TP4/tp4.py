from random import *
from view.Color import Color
import view
from view.TextRect import *
from view.Text import *
from view.Canvas import *


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
    nbLigne = len(tab)
    nbCol = len(tab[0])
    return nbLigne, nbCol


def getCarre2D(n: int) -> list:
    matrice = []
    val = []
    for i in range(1, n ** 2 + 1):
        val.append(i)
    shuffle(val)
    for i in range(n):
        ligne = []
        for y in range(n):
            ligne.append(val.pop())
        matrice.append(ligne)
    return matrice


def getSommeLignes(matrice: list) -> list:
    somme = []
    for elt in matrice:
        compt = 0
        for i in range(len(elt)):
            compt += elt[i]
        somme.append(compt)
    return somme


def getSommeColonnes(matrice: list) -> list:
    somme = []
    for i in range(len(matrice[0])):
        compt = 0
        for elt in matrice:
            compt += elt[i]
        somme.append(compt)
    return somme


def getSommeDiagonale1(matrice: list) -> int:
    somme = 0
    for i in range(len(matrice[0])):
        somme += matrice[i][i]
    return somme


def getSommeDiagonale2(matrice: list) -> int:
    somme = 0
    longMat = len(matrice[0]) - 1
    for i in range(longMat + 1):
        somme += matrice[i][longMat - i]
    return somme


def dessinerCarre(matrice: list) -> view.Canvas:
    nLigne = getSommeLignes(matrice)
    nCol = getSommeColonnes(matrice)
    nDiag1 = getSommeDiagonale1(matrice)
    nDiag2 = getSommeDiagonale2(matrice)
    n = getMax([getSommeLignes(matrice), getSommeColonnes(matrice), [getSommeDiagonale1(matrice)], [getSommeDiagonale2(matrice)]])
    txt = Text((0, 0), str(n))
    w, h = txt.getSize()
    tail = len(matrice)
    # Ajout de la marge h/2
    w += h
    h += h
    # Taille des cadres pour les nombres : (w, h)
    cv = Canvas((w * (tail + 2), h * (tail + 1)))
    print(nLigne)
    print(matrice)
    for i in range(tail):
        vide = TextRect((0, i * h), "", rect=(w, h))
        vide.setFill(Color(100, 100, 100))
        vide.draw(cv)
        for y in range(len(matrice[i])):
            n = matrice[y][i]
            mat = TextRect(((1 + i) * w, (y) * h), str(n), rect=(w, h))
            mat.setFill(Color(255, 255, 255))
            mat.draw(cv)
        lin = TextRect(((tail + 1) * w, i * h), str(nLigne[i]), rect=(w, h))
        lin.setFill(Color(100, 100, 100))
        lin.draw(cv)
    col1 = TextRect((0, tail * h), str(nDiag1), rect=(w, h))
    col1.setFill(Color(100, 100, 100))
    col1.draw(cv)
    for i in range(len(nCol)):
        col = TextRect(((i + 1) * w, (tail) * h), str(nCol[i]), rect=(w, h))
        col.setFill(Color(100, 100, 100))
        col.draw(cv)
    col2 = TextRect(((tail + 1) * w, tail * h), str(nDiag2), rect=(w, h))
    col2.setFill(Color(100, 100, 100))
    col2.draw(cv)
    waitClick()
    return cv

def zeros(n1: int, n2: int) -> list:
    tab = []
    for i in range(n1):
        ligne = [0] * n2
        tab.append(ligne)


def getArray2D(lst: list) -> list:
    tab = []
    for elt in lst:
        ligne = []
        for i in range(elt):
            ligne.append(0)
        tab.append(ligne)
    return tab

def zeros(nl: int, nc: int) -> list:
    tab = []
    for i in range(nl):
        tab.append([0]*nc)
    return tab

def creerCarreMagique(n: int) -> list:
    rep=None
    if n % 2 != 0:
        tab=zeros(n,n)
        case=n*n
        x= 0
        y= n //2
        for i in range(1,case+1):
            tab[x][y] = i
            xTemp = x
            yTemp = y
            xTemp -= 1
            yTemp += 1
            if xTemp < 0:
                xTemp = n-1
            if yTemp >= n:
                yTemp = 0
            if tab[xTemp][yTemp] == 0:
                x = xTemp
                y = yTemp
            else:
                x += 1
                if x >= n:
                    x=0
        rep=tab

    return rep