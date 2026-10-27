# insert(idx, elem) insert elem à l'index idx
# Les éléments existants à l'index et après seront décalés vers la droite

jours = ["Lundi", "Jeudi", "Vendredi", "Samedi"]
jours.insert(1, "Mardi")
print(jours)

jours.insert(0, "Dimanche")

# Pour insérer à la fin
# append()
jours.append("Patate")
print(jours)
# en utilisant l'index du dernier élément, il est mieux d'utiliser append()
# N'importe index supérieur au dernier index existant, va rajouter l'élément à la fin
jours.insert(len(jours), "Toto")
print(jours)

jours.insert(999, "Vindredi")
print(jours)
