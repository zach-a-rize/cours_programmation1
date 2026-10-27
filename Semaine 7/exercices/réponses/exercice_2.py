a1 = "Francais:quatorze:14"
a2 = "Russe:TCHETJRE:4"
a3 = "Grec:DUO:2"
a4 = "francais:Mille:1000"
a5 = "sanskrit:navati:90"
a6 = "francais:Deux cent seize mille:216000"

liste_a = [a1, a2, a3, a4, a5, a6]
liste_chiffre_langue = []
liste_chiffre_lettre = []
liste_chiffre = []

for a in liste_a:
    liste_split = a.split(":")
    liste_chiffre_langue.append(liste_split[0])
    liste_chiffre_lettre.append(liste_split[1])
    liste_chiffre.append(liste_split[2])

chiffre_demande = input("Entrez un chiffre: ")
langue_demandee = input("Entrez une langue: ")

if chiffre_demande in liste_chiffre:
    idx_chiffre = liste_chiffre.index(chiffre_demande)
    langue_disponible: str = liste_chiffre_langue[idx_chiffre]
    if langue_disponible.lower() != langue_demandee.lower():
        print("Langue non disponible")
        exit()
    print(f"Le chiffre {chiffre_demande} s'écrit {liste_chiffre_lettre[idx_chiffre]} en {langue_demandee}")
else:
    print("Chiffre non disponible!")
