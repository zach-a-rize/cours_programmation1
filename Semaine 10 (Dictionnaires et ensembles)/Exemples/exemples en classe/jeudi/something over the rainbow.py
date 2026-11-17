import csv
import pandas as pd
import numpy as np
with open("Periodic Table of Elements.csv", "r", encoding="utf8") as fishier_csv:
    liste_elements = csv.DictReader(fishier_csv)



    total_masse_atomique = 0
    nb_elements = 0
    solides = []
    for element in liste_elements:
        total_masse_atomique += float(element["AtomicMass"])
        nb_elements += 1
       # if element["Phase"] == "solid":

    print(f"Moyenne des masses atomiques: {total_masse_atomique/len(total_masse_atomique)}")



#############################################
dataframe = pd.read_csv("Periodic Table of Elements.csv")
dataframe.info()
print(f"moyenne des masses atomiques: {np.mean(dataframe["AtomicMass"])}")
print(f"Médiane des masses atomiques: {dataframe["AtomicMass"].median}")
