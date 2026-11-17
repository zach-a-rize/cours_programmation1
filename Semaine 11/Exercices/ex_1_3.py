message = input("Phrase : ")
print(message.upper())
phrase_chuchotee = ""
nb_voyelle = 0
for i in message:
    if i in "aeiouy":
        nb_voyelle +=1
        phrase_chuchotee += "*"
    else:
        phrase_chuchotee += i
print((f"Voyelles : {nb_voyelle}"))
print(phrase_chuchotee)