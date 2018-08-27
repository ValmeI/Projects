faili_nimi = input("Sisestage failinimi: ")

fail = open(faili_nimi, encoding="UTF-8")

for i in fail:
    i = i.replace("\n", '')
    i = i.upper()
    i = i.replace("Ä", "AE")
    i = i.replace("Õ", "OE")
    i = i.replace("Ö", "OE")
    i = i.replace("Ü", "UE")
    print(i)

fail.close()
