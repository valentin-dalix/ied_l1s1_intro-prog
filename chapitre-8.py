#Exemples du cours

with open("texte.txt", "r") as f:
    contenu = f.read()
    print(contenu)

with open("texte.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())

try:
    nombre = int(input("Entrez le nombre à diviser :"))
    diviseur = int(input("Entrez le diviseur :"))
    resultat = nombre / diviseur
except ZeroDivisionError:
    print("Division par zero impossible")
else:
    print("Le resultat de la division est :", resultat)

def racine(x):
    if x < 0:
        raise ValueError("x doit etre positif")
    return x ** 0.5
print(racine(int(input("Nombre :"))))

#1
with open ("texte.txt", "w") as f:
    f.write("Ligne 1\n")
    f.write("Ligne 2\n")
    f.write("Ligne 3\n")
    f.write("Ligne 4\n")
    f.write("Ligne 5\n")
with open ("texte.txt", "r") as f:
    contenu2 = f.read()
    print(contenu2)

#2
nbr_ligne = 0
with open ("texte.txt", "r") as f:
    for ligne in f:
        nbr_ligne += 1
print(nbr_ligne)

#Version de la prof
with open("texte.txt") as f:
    lignes = len(f.readlines())
print(lignes)

#3
try:
    with open (input("Nom du fichier : "), "r") as f:
        contenu3 = f.read()
except FileNotFoundError:
    print("Le fichier n'existe pas!")
else:
    print(contenu3)

#4
liste_de_nombres = [6, 237, 673, 2345234, 234234, 32567, 4221578, 32467]
with open ("sauvegarde-nombre.txt", "w") as f:
    for nombre in liste_de_nombres:
        f.write(str(nombre) + "\n")

#Version de la prof
liste_de_nombres = [6, 237, 673, 2345234, 234234, 32567, 4221578, 32467]
with open ("sauvegarde-nombre.txt", "w") as f:
    for nombre in liste_de_nombres:
        f.write(f"{nombre}\n")