# main_tp4.py
from random import randint
from TP4.tp4 import getRegularArray2D, getMin, getMax


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


# test_getRegularArray2D()
test_getMinMax()