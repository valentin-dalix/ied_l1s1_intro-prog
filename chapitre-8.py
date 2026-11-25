#Exemples du cours

with open("texte.txt", "r") as f:
    contenu = f.read()
    print(contenu)

with open("texte.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())

