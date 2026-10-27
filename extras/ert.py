# == retourne toujours vrai ou faux
# For parcours une séquence
# if "j" not in lettres:
'''Semaine 7'''
# Retourner une position de str
liste_fruits = ["fraises", "framboises", "pommes", "bleuets"]
st = "patate"
print(st[0])
# À partir de la fin
print(st[-1])
# va chercher le mot puis la lettre
print(liste_fruits[2][0])

# On peut retourner une partie de la liste en utilisant l'opérateur d'indexation [:]
# [debut:fin exclus] ou [debut : fin exclus : pas] (retourne liste)
print(liste_fruits[0:3])

liste_10 = list(range(10))
print(liste_10)
# len longueur de la séquence
print(len(st))

enumerate(st)

lettres = ["a", "b", "c", "b"]
for lettre in enumerate(st):
    print(lettre)

 #  del voyelles[2]

 #   lettre_poppee = lettres.pop()

 #   clear()

print(lettres.index("b"))
print(lettres.count("b"))


nombres = [17, 38, 10, 25, 72]

# append(élement) va rajouter l'elément à la fin de la liste
nombres.append(42)
print(nombres)


# On peut ajouter les éléments d'une liste au bout de la liste en utilisant extend(liste)
nombres_3 = [1, 2, 3, 4, 5]
nombres_4 = [6, 7, 8, 9, 10]
nombres_3.extend(nombres_4)
print(nombres_3)


# sort() trie la liste en la modifiant
##liste_nombres.sort()

#print(liste_nombres)

# sorted(séquence) trie la liste sans la modifier et retourne une nouvelle (triée)
# liste_decroissante = sorted(liste_nombres_2, reverse=True)


jours = ["Lundi", "Jeudi", "Vendredi", "Samedi"]
jours.insert(1, "Mardi")
print(jours)

fable = "Je plie mais ne romps point".split()
# fable est maintenant une liste avec chaque mot
print(fable)
# Faire attention, ici phrase va être un alias de fable et non une copie
phrase = fable
#  Si on change un l'autre va changer
# Copier liste [:] ou copier .copy

liste_mots = ["Bonjour", "les", "amis"]
phrase = " ".join(liste_mots)
print(phrase)
phrase_2 = "AAA".join(liste_mots)
print(phrase_2)




# Str ne peut pas changer, mais une liste oui
# Examen ; ne pas oublier spécifier type par exemple str, int float en mettant les "" ou .0

'''
# +- opérateur binaire ; + - % / * ** // division entière 3.4//2 = 1.0 
priorité des opérateurs    
type: entier; int  float; nombre décimales  str; chaine de caractère (f"ma super{varible} 
\n: nouvelle ligne \t: tabulation:  \\: barre oblique inversée \uxxx: émoji ou \uxxxxxxxx 
 accéder index patate[2] == t
 bool; booléen true or false (True + true = 2)
list; vide[], del, sort(), sorted(), pop(index), remove(élément), clear(), insert(), count(), copy(), extend(liste2), append(élément), élément in séquence
int(), str(), float(), bool() 
identificateur; minuscule ou maj (pas accent), chiffres(0-9), pas commencer chiffre, "_", conventions PEP-008, constantes(OK maj) 
assignation multiples x=y=5, l1=l2=[1, 2, 3] (alias
x, y = 3, 45    
varibles globales et locales fonction(variables locales), global
sqrt(), ceil(), floor(), exp(), log(), pow(), 
Random(), randint(), choice(), shuffle()
str(); upper(), lower(), count(), find()
fonctions; print():end=, sep= input() ->str 
range(début, fin, pas)
emuerate(), len(), abs(), min(), min(), max(), sum(), sorted()
import (random,math) alias
def fonction(arg1, arg2, arg3)
structures conditionnelles; == != < > <= >= not in and or 
if elif else 
pas de match case
while, for, continue, break
test unitaire, assert 
'''