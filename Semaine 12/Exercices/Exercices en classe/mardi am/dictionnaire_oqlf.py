import csv

domaines_differents = []
#Ouverture de fichier
with open("termes_officialises_2026-01-14.csv", mode="r", encoding="utf8") as fichier:
    dict_reader = csv.DictReader(fichier)
    for ligne in dict_reader:
        key = ligne["Domaines"]
        if key in domaines_differents:
            continue
        else:
            domaines_differents.append(key)
domaines = []
for ligne_dict in dict_reader:
    domaines.append(ligne_dict["Domaines"])

domaines_ensemble = set(domaines)
domaines = list(domaines)

print(domaines)

print(len(domaines_differents))
