from TP1.tp1 import getRandomList
from TP2.tp2 import estTrie, echanger, triBulles, deplacerCase
print(estTrie([1]))
print(estTrie([2, 1]))
lst = [1, 2, 3]
print(lst)
echanger(lst, 0, 2)
print(lst)

lst = [12, 54, 2, 35, 6, 9, 87, 4, 5]
print(lst)
triBulles(lst)
print(lst)
print("test 1")
lst = [1, 3, 3, 4, 6, 8, 2, 6, 4, 9 ]
print(lst)
deplacerCase(lst, 6)
print(lst)
print("test 2")
lst = [1, 3, 3, 4, 6, 8, 0, 6, 4, 9 ]
print(lst)
deplacerCase(lst, 6)
print(lst)
