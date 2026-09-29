for nb in range(600, 701, 2):
    for k in str(nb):
        if int(k) == 3:
            compteur = 0
            for j in str(nb):
                compteur += int(j)
            if compteur == 11:
                print(f"J'ai trouvé le nombre: {nb}")
                break

# Autre exemple
for nob in range(600, 701, 2):
    nb_str = str(nob)
    premeier_chiffre = int(nb_str[0])
    deuxieme_chiffre = int(nb_str[1])
    troisieme_chiffre = int(nb_str[2])

    if premeier_chiffre == 3 or deuxieme_chiffre == 3 or troisieme_chiffre ==3:
        if premeier_chiffre + deuxieme_chiffre + troisieme_chiffre ==11:
            print(f"le nombre est: {nob}")
            break
    
