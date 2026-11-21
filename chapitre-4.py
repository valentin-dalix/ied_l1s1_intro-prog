#Exemples du cours
for x in range(1,9):
    print(x, end=" ")

print()
print()

for y in "солнышко":
    print(y, end=" ")

print()
print()

i=1
while i <= 5:
    print(i)
    i += 1

print()

for i in range(1, 4): 
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
    print("---")


#1
for n in range(1, 21):
    if n % 2 == 0:
        print(n)

#version de la prof:
for i in range(2, 21, 2):
    print(i)

#2
n = int(input("Nombre: "))
somme_des_chiffres = 0
while n > 0:
    somme_des_chiffres += n % 10
    n //= 10
print("Somme =", somme_des_chiffres)



#3
n = int(input("Nombre d'étoiles = "))
for i in range(1, n+1):
    print("*" * i)

#4
mot = input("Mot? ")
somme_des_voyelles = 0
for lettre in mot:
    if lettre == "a" or lettre == "e" or lettre == "i" or lettre == "o" or lettre == "u" or lettre == "A" or lettre == "E" or lettre == "I" or lettre == "O" or lettre == "U":
        somme_des_voyelles += 1
    else:
        continue
print(somme_des_voyelles)

#4 (avec l'ouril de la prof pour les voyelles)
mot = input("Mot? ")
somme_des_voyelles = 0
for lettre in mot:
    if lettre in "aeiouAEIOU":
        somme_des_voyelles += 1
    else:
        continue
print(somme_des_voyelles)