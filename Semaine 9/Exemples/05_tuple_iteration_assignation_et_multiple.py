x = (1, 2, 3, 4)

# On peut faire des assignations multiples (dans les faits, on fait du "unpacking")
# le nombre de variables assignées doit correspondre au nombre d'éléments du tuple.
a1, a2, a3, a4 = x
print(f"a1, a2, a3, a4:", a1, a2, a3, a4)

# On peut itérer sur un tuple, c'est une séquence indexée (itérable)
print("Itération:")
for i in x:
    print(i, end=" ")

print()
# Version while, peu utilisé
print("Itération while:")
i = 0
while i < len(x):
    print(x[i], end=" ")
    i += 1
print()
# on peut retourner la longueur d'un tuple avec len(), car c'est un itérable
print(f"len(x): {len(x)}")


