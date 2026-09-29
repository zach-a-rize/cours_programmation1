mot = input("Entrer un mot: ")
sequence = input("Entrer un séquence de lettres: ")
mot_invers = mot[0::-1]
if mot in sequence:
    print("C'est dans la séquence")
if mot_invers in sequence:
    print("C'est dans la séquences")

def invserser_chaine(chaine: str) ->str:

    inverse = ""
    for caractere in chaine:
        inverse = caractere + inverse

    return inverse


if mot.find(sequence) != -1 or mot.find(invserser_chaine(sequence)) != -1:
    print("composable")
else:
    print("non")

