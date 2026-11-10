import random


def vainqueur(utilisateur, ordinateur):
    global choix, ordi_choix
    if utilisateur == ordinateur:
        print(f"nul {utilisateur} vs {ordinateur}")
    else:
        if utilisateur == "r":
            if ordinateur == "c":
                print(f"Gangnant {choix} vs {ordi_choix}")
            else:
                print(f"Perdant {choix} vs {ordi_choix}")
        if utilisateur == "p":
            if ordinateur == "r":
                print(f"Gangnant {choix} vs {ordi_choix}")
            else:
                print(f"Perdant {choix} vs {ordi_choix}")
        if utilisateur == "c":
            if ordinateur == "p":
                print(f"Gangnant {choix} vs {ordi_choix}")
            else:
                print(f"Perdant {choix} vs {ordi_choix}")





while True:
    h = ("r", "c", "p")
    ordi_choix = random.choice(h)

    choix = input("Roche(r), papier(p), ciseau(c):")
    match choix:
        case "r":
            vainqueur(choix, ordi_choix)
            if ordi_choix == "c":
                print(f"Gangnant {choix} vs {ordi_choix}")
            elif ordi_choix =="p":
                print(f"perdant {choix} vs {ordi_choix}")
        case "p":
            vainqueur(choix, ordi_choix)
            if ordi_choix == "r":
                print(f"Gagnant {choix} vs {ordi_choix}")
            elif ordi_choix != choix or "r":
                print(f"perdant {choix} vs {ordi_choix}")
        case "c":
            vainqueur(choix, ordi_choix)
            if ordi_choix == "p":
                print(f"Gagnant {choix} vs {ordi_choix}")
            elif ordi_choix == "r":
                print(f"Perdant {choix} vs {ordi_choix}")
        case _:
            print("Valeur invalide")
            continue
