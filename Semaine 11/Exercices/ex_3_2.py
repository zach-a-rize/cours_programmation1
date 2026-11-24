phrase = input("Phrase : ")
lettres = phrase.replace(" ", "")
frequences = {}


for x in lettres:
    frequences[x] = frequences.get(x, 0) + 1
print(frequences)
plus_frequente = ()
for x, freq in frequences.items():
    if frequences.get(plus_frequente <= freq):
        plus_frequente = x
print(f"Lettre la plus fréquente : {plus_frequente} ({frequences[plus_frequente]} fois)")
