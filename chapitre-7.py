#Exemples du cours

print("bon" + "jour")

for lettre in "abc":
    print(lettre)

#1
phrase1 = input("Phrase 1 :")
print(phrase1.upper())

#2
phrase2 = input("Phrase 2 :")
phrase2mots = phrase2.split()
print(len(phrase2mots))

#version de la prof
print(len(input("Phrase 2 :").split()))

#3
inverse = ""
chaine_a_inverser = input("Chaine à inverser :")
for lettre in chaine_a_inverser:
    inverse = lettre + inverse
print(inverse)

#4
mot1 = input("Mot 1 :")
mot2 = input("Mot 2 :")
if sorted(mot1.lower()) == sorted(mot2.lower()):
    print("Ce sont des anagrammes")
else:
    print("Ce ne sont pas des anagrammes")