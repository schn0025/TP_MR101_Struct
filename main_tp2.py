from TP1.tp1 import getRandomList
from TP2.tp2 import triBullesRect, tirInsertionRect
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
print('Lancement du tri : cliquez dans la fenêtre')
waitClick()
tirInsertionRect(lstRec, tps)
print("Fin du tri : cliquez pour finir")
waitClick()
