from math import *
# Tout est importé, plus besoin de mettre de préfixe
# En utilisant *, tout est importé, même ce qui ne sera pas utilisé
nombre = 121
# pi est défini dans math
angle = pi / 6

print("Racine carré de 121:", sqrt(nombre))
print("Sinus de 30 degrés:", sin(angle))

# Les définitions de fonctions se retrouvent maintenant dans les globales
print(globals())