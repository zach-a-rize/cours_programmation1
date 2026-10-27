fable = "Je plie mais ne romps point".split()
# fable est maintenant une liste avec chaque mot
print(fable)
# Faire attention, ici phrase va être un alias de fable et non une copie
phrase = fable
print(phrase)
# fable[4] est le mot romps
fable[4] = "casse"
print(fable)
print(phrase)


