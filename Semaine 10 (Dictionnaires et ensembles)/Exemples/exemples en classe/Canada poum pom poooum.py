from time import perf_counter_ns
temps_debut = perf_counter_ns()
liste_impair = []
for i in range(1, 1000000):
    liste_impair.append(i)
    print(liste_impair)

    temps_fin = perf_counter_ns()
    print(temps_fin-temps_debut)
'''liste_impair = [x for x in range(1, 100000, 2)]

liste_fonction = [x**2-1 for x in range(1, 5000)]



liste_communs = []
for i in liste_impair:
    for j in liste_fonction:


temps_fin = perf_counter_ns()
print(temps_fin)'''