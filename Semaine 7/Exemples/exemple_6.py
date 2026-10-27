proverbe = ["La", "raison", "du", "plus", "fort", "est", "toujours", "la", "meilleure"]


for mot in proverbe:
    print(mot, end=" ")
print()
# le paramètre end du print permet de changer la str qui sera ajoutée au print (par défaut "\n", nouvelle ligne)
for mot in proverbe:
    print(mot, end="->")

print()
fruits = [["raisin", "papaye", "pomme"], "pamplemousse", "ananas", "citron", "poire", "banane", ["lime", "papaye"]]

for mes_preferes in fruits:
    print(mes_preferes, end=" ")


