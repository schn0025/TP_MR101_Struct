# main_tp4.py
from random import randint

from TP4.tp4 import getRegularArray2D, getMin, getMax, isRegular, getSize2D, getCarre2D, getSommeLignes, \
    getSommeColonnes


def test_getRegularArray2D() -> None:
    lst = getRegularArray2D(4, 5, -10, 10)
    print("Tableau de 4 lignes et 5 colonnes :", lst, sep="\n")
    return None


def test_getMinMax():
    for i in range(5):
        col = randint(1, 5)
        lig = randint(1, 5)
        tab = getRegularArray2D(lig, col, -10, 10)
        print(tab, ": min =", getMin(tab), "  max =", getMax(tab))


def test_getRegularArray2D():
    for i in range(10000):
        nl = randint(1, 10)
        nc = randint(1, 10)
        mn = randint(-20, -5)
        mx = randint(5, 20)
        tab = getRegularArray2D(nl, nc, mn, mx)
        assert isRegular(tab), "tab n'est pas régulier"
        assert getSize2D(tab) == (nl, nc), f"les tailles relevés ne sont pas bonnes, {getSize2D(tab)} au lieux de {(nl, nc )} "
        assert getMin(tab) >= mn, "min a planter"
        assert getMax(tab) <= mx, "max a planter"
    print("La fonction getRegularArray2D est correcte !")

def test_getCarre2D():
    for i in range(5):
        n=randint(3,6)
        print(getCarre2D(n))

def test_getSommeLignes():
    for i in range(5):
        matrice = getCarre2D(3)
        somme = getSommeLignes(matrice)
        print(f'{matrice} , somme des lignes : {somme}')

def test_getSommeColonnes():
    for i in range(5):
        matrice = getCarre2D(3)
        somme = getSommeColonnes(matrice)
        print(f'{matrice} , somme des colonnes : {somme}')
# test_getRegularArray2D()
# test_getMinMax()
# test_getRegularArray2D()
# test_getCarre2D()
# test_getSommeLignes()
test_getSommeColonnes()

