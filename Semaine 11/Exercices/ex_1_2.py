mot_de_passe = input("Mot de passe : ")

raisons = []
if len(mot_de_passe) < 8:
    raisons.append("Trop court")
if mot_de_passe.lower() == mot_de_passe:
    raisons.append("Pas de majuscule")
a_un_chiffre = False
for c in mot_de_passe:
    if c in [str(n) for n in range(0,10)]:
        a_un_chiffre = True
        break
if not a_un_chiffre:
    raisons.append("aucun chiffre")

if len(raisons) > 0:
    print(f"Porte verrouillée : ", end="")
    for r in raisons:
        print(r, " ", end ="")
else:
    print("Porte ouverte")