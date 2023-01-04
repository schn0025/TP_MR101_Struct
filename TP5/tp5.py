def getPrix(p: dict, a: str) -> int:
    rep = 0.0
    if a in p:
        rep = p[a]
    return rep


def getPrixTotal(p: dict):
    somme = 0
    for key in p.keys():
        somme += p[key]
    return somme


def afficherPanier(p: dict) -> None:
    total = getPrixTotal(p)
    a = 'Articles'
    pr = 'Prix'
    print(f'{a:>10} {pr:>20}')
    print('-----------------------------------')
    for key in p.keys():
        print(f'{key:<20}:{str(p[key]):>14}')
    print('-----------------------------------')
    print(f'{"Prix Total":>18}  : {str(total):>13}')