#1
nombre = float(input("Nombre = "))
if nombre > 0:
    print("Ce nombre est positif.")
elif nombre < 0 :
    print("Ce nombre est négatif.")
elif nombre == 0:
    print("Ce nombre est nul.")

#ou alors...
nombre = float(input("Nombre = "))
if nombre > 0:
    print("Ce nombre est positif.")
elif nombre < 0 :
    print("Ce nombre est négatif.")
else:
    print("Ce nombre est nul.")

#2
password = str(input("Mot de passe = "))
if password == "python123": 
    print("Mot de passe correct.")
else:
    print("Mot de passe incorrect.")

#3
n1 = float(input("Nombre 1 = "))
n2 = float(input("Nombre 2 = "))
n3 = float(input("Nombre 3 = "))
if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)

#4
age = float(input("Âge de la personne = "))
if age < 12:
    print("Prix = 12 euros.")
elif 12 <= age < 65:
    print("Prix = 25 euros.")
else:
    print("Prix = 18 euros.")

#version de la prof:
age = int(input("Age de la personne = "))
if age < 12:
    prix = 12
elif age >= 65:
    prix = 18
else:
    prix = 25
print("Prix = ", prix, "euros")