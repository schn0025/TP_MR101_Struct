from TP1.tp1 import getRandomList
from TP2.tp2 import triBullesRect, tirInsertionRect, triSelectionRect
from view.Canvas import *
from view.Rect import *

nb = 20
tps = 0.1
lst = getRandomList(nb, 20, 300)
cv = Canvas(getCanvasSizeFrom(lst))
lstRec = []
for i in range(len(lst)):
    r = Rect(i, lst[i], cv)
    lstRec.append(r)

# tri par selection
for i in range(len(lst)):
    r = Rect(i, lst[i], cv)
    lstRec.append(r)
print('Lancement du tri : cliquez dans la fenêtre')
waitClick()
triSelectionRect(lstRec, tps)
print("Fin du tri : cliquez pour finir")
waitClick()

# tri a bulles
for i in range(len(lst)):
    r = Rect(i, lst[i], cv)
    lstRec.append(r)
print('Lancement du tri : cliquez dans la fenêtre')
waitClick()
triBullesRect(lstRec, tps)
print("Fin du tri : cliquez pour finir")
waitClick()

# tri par insertion
for i in range(len(lst)):
    r = Rect(i, lst[i], cv)
    lstRec.append(r)
print('Lancement du tri : cliquez dans la fenêtre')
waitClick()
tirInsertionRect(lstRec, tps)
print("Fin du tri : cliquez pour finir")
waitClick()