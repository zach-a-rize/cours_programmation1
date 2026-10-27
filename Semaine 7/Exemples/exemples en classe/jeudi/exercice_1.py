t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
      'Décembre']

# Solution de la classe
t3 = list()

for i in t2:
    idx = t2.index(i)
    t3.append(i)
    t3.append(t1[idx])

t2 = t3
print(t2)

