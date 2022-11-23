def estTrie(lst: list) -> bool:
    rep = False
    i = 0
    if not lst:
        rep = True
    while i < len(lst) - 1 and lst[i] < lst[i + 1]:
        i += 1
    if i == len(lst) - 1:
        rep = True
    return rep
