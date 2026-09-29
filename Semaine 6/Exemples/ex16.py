from math import pow, log
from random import seed, random
# Ceci importe seulement ce que l'on a de besoin, pas obligé de mettre les préfixes

seed(42)
nombre = random()
log_nombre = log(nombre)
puissance = pow(log_nombre, 6)

print(globals())

