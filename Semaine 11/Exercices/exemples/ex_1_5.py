import random
prenom = input("Prénom:")
nom = input("Nom:")
dragon_nom = prenom[0:3] + nom[-3:].lower()
titres = ["le malicieux", "cannibale", "pédophile", "cutie pie"]
print(f"Ton nom de dragon: {dragon_nom} {random.choice(titres)}")