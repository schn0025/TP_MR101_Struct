def estTrie(lst: list) -> bool:
    rep = False
    i = 0
    if not lst:
        rep = True
    while i < len(lst) - 1 and lst[i] <= lst[i + 1]:
        i += 1
    if i == len(lst) - 1:
        rep = True
    return rep

def echanger(lst: list, i1: int, i2: int) -> None:
    lst[i1], lst[i2] = lst[i2], lst[i1]
    return None

def triBulles(lst: list) -> None:
    etape = 1
    modif = -1
    while modif != 0:
        modif = 0
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                echanger(lst, i, i+1)
                modif += 1
        etape += 1
    return None

def getMin(lst: list) -> int:
    mini=lst[0]
    for elt in lst:
        if elt < mini:
            mini = elt
    return mini

def getIndexMin(lst: list) -> int:
    idMini=0
    for i in range(1, len(lst)):
        if lst[i] < lst[idMini]:
            idMini = i
    return idMini

def getIndexMinFrom(lst: list, depart: int) -> int:
    idMini = depart
    for i in range(depart, len(lst)):
        if lst[i] < lst[idMini]:
            idMini = i
    return idMini

def triSelection(lst: list) -> None:
    for i in range(len(lst)):
        idMini=getIndexMinFrom(lst, i)
        echanger(lst, i, idMini)
    return None

def deplacerCase(lst: list, i: int) ->None:
    while i > 0 and lst[i] < lst[i-1]:
        echanger(lst, i, i-1)
        i -= 1
    return None

def triInsertion(lst: list) -> None:
    for i in range(len(lst)):
        deplacerCase(lst, i)
    return None
