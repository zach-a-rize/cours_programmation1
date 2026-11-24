potion = {'herbe', 'miel', 'cristal', 'eau'}
ingredients_str = input("Ingrédients : ")
ingredients_set = set(ingredients_str.split(","))
if potion.issubset(ingredients_set):
    print(f"Potion prête !")
else:
    ensemble_manquants = potion - ingredients_set
    liste_manquants = list(ensemble_manquants)
    print(f"Il manque : {" ".join(liste_manquants)}")
    print(f"Inutiles : {" ".join((ingredients_set-potion))}")
