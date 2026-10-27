x = (1, 2, 3, 4)
y = ("a", "b", "c")

# concaténation
z = x + y
print(f"concaténation: {z}")

# Répétition, multiplication
t = y * 4
print(f"multiplication: {t}")

# On ne peut pas ajouter un type autre qu'un tuple à un tuple
try:
    z = z + "d"  # Donne une erreur
except TypeError as te:
    print("tuple + un autre type, erreur:", te)

# Mais on peut ajouter un tuple à un tuple (concaténation)
z = z + x
print(z)

