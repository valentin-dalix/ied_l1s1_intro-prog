#Exemples du cours

import math
print(math.pi)
print(math.sqrt(16))
print(math.floor(3.7))

#1
import random
for _ in range (10):
    print(random.randint(1, 100), end=" ")
print()

#2
import math
nombre = float(input("Nombre : "))
print("Racine carrée =", math.sqrt(nombre), "logarithme =", math.log(nombre))

#3
import random
total = 0
for _ in range (100):
    total += random.randint(1, 6)
print(total / 100)

#Version de la prof
import random
lancers = [random.randint(1, 6) for _ in range(100)]
print(sum(lancers) / len(lancers))

#4
# dans stats.py