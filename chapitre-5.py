#Exemples du cours

fruits = ["pomme", "banane", "cerise"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(len(fruits))

fruits[1] = "kiwi"
fruits.append("mangue")
fruits.remove("pomme")
print(fruits[0])
print(fruits[1])
print(fruits[2])

L = [10, 59, 295, 598, 35, 25, 93]
print(L[::3])

personne = {"nom": "Anastasia", "age": 18, "ville": "Novosibirsk"}
print(personne["nom"])
print(personne["age"])
print(personne["ville"])
personne["age"] = 19
personne["email"] = "anastasia@fsb.ru"
for key in personne:
    print(key, ":", personne[key])

s = {1, 45, 76, 76, 23, 12, 12, 79, 43}
print(s)
s.add(4)
s.remove(1)
print(s)

carres = [x * x for x in range(10) if x % 2 == 0]
print(carres)

mot = input("Mot? ")
count = {}
for letter in mot:
    count[letter] = count.get(letter, 0) + 1
print(count)

#1
n = [2, 6, 45, 37, 3]
somme = sum(n)
print(somme)

#2
mot = "Novosibirsk"
print(len(set(mot)))

#3
notes = {"Valentin": 20, "Anastasia": 18, "Isabella": 13}
for nom, note in notes.items():
    print(nom, note)

#4
list_ex_4 = [1, 8, 4, 87, 45, 23 ,94, 65 ,2843, 478954, 23457, 2357]
for element in list_ex_4:
    if element % 2 == 0:
        print(element)

#4 (version de la prof)
L = [1, 8, 4, 87, 45, 23 ,94, 65 ,2843, 478954, 23457, 2357]
pairs = [x for x in L if x % 2 == 0]
print(pairs)