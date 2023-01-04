def getPrix(p: dict, a: str) -> int:
    rep = 0.0
    if a in p:
        rep= p[a]
    return rep

def getPrixTotal(p: dict):
    somme = 0
    for key in p.keys():
        somme += p[key]
    return somme