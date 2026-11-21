#Exemples du cours

def saluer(nom="monsieur ou madame"):
    print("Bonjour", nom)
saluer("Valentin")
saluer("Sarah")
saluer()

def addition(a, b):
    return a + b
resultat = addition(3, 5)
print(resultat * 2)

def puissance(base, exposant=2):
    return base ** exposant
print(puissance(3))
print(puissance(2,5))
print(puissance(exposant=3, base=4))

def somme(*nombres):
    return sum(nombres)
print(somme(1, 2, 3))
print(somme(10, 20))

def aire_rectangle(l, h):
    """Calcule l'air d'un rectangle"""
    return l * h
print(aire_rectangle.__doc__)

def factorielle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat
print(factorielle(5))

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(8):
    print(fibonacci(i))


#1
def carre(n):
    return (n * n)

#2
def compteur_voyelles():
    mot = input("Mot? ")
    somme_des_lettres = 0
    for lettre in mot:
        somme_des_lettres += 1 if lettre in "aeiouAEIOU" else 0
    print(somme_des_lettres) 
compteur_voyelles()


#3
def est_premier():
    integer_a_tester = int(input("Nombre? :"))
    if integer_a_tester < 2:
        return False # 0 et 1 ne sont pas premier par définition
    for i in range (2, integer_a_tester - 1):
        if integer_a_tester % i == 0:
            return False
    return True
print(est_premier())

#4
e = float(input("Prix en euros?"))
def euro_dollar():
    print(e * 1.10)
euro_dollar()