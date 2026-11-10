import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("spotify_data.csv")

df.info()

colonne_chansons = df["Songs & Artist"]
colonne_streams = df["Streams"]
colonne_daily = df["Daily"]

top_5_chansons = colonne_chansons[:5]
top_5_quotidien = colonne_daily[:5]


total_streams = sum(colonne_streams)
total_daily = sum(colonne_daily)

# x = np.array(["Écoute Totale", "Moyenne Quotidienne"])
# y = np.array([total_streams, total_daily])

plt.bar(top_5_chansons, top_5_quotidien)
plt.ylabel("Nombre d'écoutes")
plt.xlabel("Catégories")
plt.title("Somme des écoutes sur spotify pour le top des chansons")
plt.show()
print("Top 5 des chansons Spotify 2024-2026")
for idx, valeur in enumerate(top_5_chansons):
    print(idx +1, valeur)