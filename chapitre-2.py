#1
a = float(input("Nombre A = "))
b = float(input("Nombre B = "))
print("A + B = ", a + b)

#2
longueur = float(input("Longueur du rectangle = "))
largeur = float(input("Largeur du rectangle = "))
print("Périmètre du rectangle = ", (longueur + largeur) * 2)

#3
prix_ht = float(input("Prix hors taxe = "))
tva = float(input("TVA (en %) = "))
print("Prix TTC =", prix_ht * (1 + tva / 100))

#4
secondes = int(input("Nombres de secondes = "))
print("Durée =", (secondes // 3600), "heures,", (secondes // 60) % 60, "minutes, et", secondes % 60 , "secondes.")

#Version du corrigé, même résultat mais plus élégant
total = int(input("Secondes = "))
h = total // 3600
m = (total % 3600) // 60
s = total % 60
print(h, "h", m, "min", s, "s")