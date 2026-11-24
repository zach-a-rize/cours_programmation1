import string
abc =set(string.ascii_lowercase)
while True:
    ensemble = (input("Phrase:"))
    ensemble = ensemble.replace(" ", "")
    ensemble = set(ensemble)
    if ensemble == abc:
        print("C'est un pangramme !")
    else:
        print(f"Pas un pangramme. Lettres manquantes : {" ".join(sorted(abc - ensemble))}")