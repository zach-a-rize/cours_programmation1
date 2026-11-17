from tkinter.font import names

import requests

numero_poke = int(input("Entrez un numéro de pokémon: "))

dict_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero_poke}").json()

print()

listes_moves = dict_pokemon["moves"]
print()
liste_movs_pokmon = []

for move_dict in listes_moves:
    liste_movs_pokmon.append(move_dict["move"]["name"])
print(liste_movs_pokmon)

liste_stats = dict_pokemon["stats"]
listesspecail = []
for i in liste_stats:
    cle = i["stat"]["name"]
    valeur = i["base_stat"]
    stats_pokemon[cle] = valeur
print(stats_pokemon)
for cle, valeur in stats_pokemon.items():
    print(f"\t{cle}: {valeur}")