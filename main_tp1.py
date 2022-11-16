# main_tp1.py
from TP1.tp1 import *


for i in range(5):
    print(getRandomList(10, -20, 20))

liste = getRandomList(10, -5, 6)
print(compter(liste, 0))
print(compter(liste, 10))
