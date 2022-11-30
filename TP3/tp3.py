# renvois le premeir indice de la valeur val
def indexOf(lst: list, val: int) -> int:
    i = 0
    while i < len(lst) and lst[i] != val:
        i += 1
    if i == len(lst):
        i = -1
    return i