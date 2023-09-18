def getsum(a):

    chaine = str(a)
    chiffres = list(map(int, chaine.strip()))
    return sum(chiffres)

a = 345567426
print(getsum(a))