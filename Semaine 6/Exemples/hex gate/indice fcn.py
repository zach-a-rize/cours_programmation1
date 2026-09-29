import math
# Pour les fonctions
# Dans cet exemple, j'indique que le premier paramètre devrait être une

def afficher_nombre(nom: str, nombre:  float) -> float:
    print(f"Bonjour `{nom}! Votre nombre est {nombre}")
    return nombre**2


# Ceci indique à pyvharm qu'il s'attend à de que la fonction soit appellée
print(afficher_nombre("Poire Luc", 42.0))
print(afficher_nombre(42, [7, 79]))

# On peut faire ceci pour toute déclaration de variables
mon_int: int = 2
mon_float: float = 42.0
phrase: str = "Une str"
# etc...
# Les builtins de python incluent tous les indices de type
math.