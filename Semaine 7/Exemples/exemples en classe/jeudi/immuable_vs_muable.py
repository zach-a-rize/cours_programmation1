# une structure de données qui est muable peut être modifiée
liste1 = [0, 1, 2, 3, 4]
print(liste1)
# on accède à un élément par son index
print(liste1[2])

# les listes sont muables
liste1[2] = 42
print(liste1)

# Les str sont immuables, on ne peut les modifier
citation = "L'information n'est pas la connaissance"
print(citation[0])
# Ceci va générer un TypeError
citation[0] = "D"




