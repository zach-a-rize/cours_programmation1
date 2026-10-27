t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
      'Décembre']

# À chaque fois que l'on insère un nombre de jours, on décale vers la droite.
# En ayant une variable qui incrémente à chaque itération, on peut calculer où insérer
delta = 0
for idx, jours in enumerate(t1):
    # on doit insérer après le mois, donc on doit insérer 1 plus loin (plus le delta) que l'itération en cours
    t2.insert(idx+1+delta, jours)
    delta += 1
print(t2)


