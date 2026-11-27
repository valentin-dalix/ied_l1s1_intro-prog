import math

def moyenne(liste):
    return sum(liste) / len(liste)


def ecart_type(liste):
    ecart = 0
    m = moyenne(liste)
    for i in liste:
        ecart += (m - i) ** 2
    return math.sqrt(ecart / len(liste))

#Version de la prof
# def moyenne(L):
#     return sum(L) / len(L)

# def ecart_type(L):
#     m = moyenne(L)
#     return math.sqrt(sum((x - m) ** 2 for x in L) / len(L))