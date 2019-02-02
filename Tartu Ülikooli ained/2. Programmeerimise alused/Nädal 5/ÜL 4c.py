from datetime import *

fail = input("Sisestage failinimi: ")

nimekiri = open(fail, encoding="UTF-8")

nimed = []
arvud = []

for nimi in nimekiri:
    nimi = nimi.strip()
    nimed.append(nimi)

for x in range(len(nimed)):
    arvud.append(x+1)

#zip tõmbaba kokku ja teen dic, et pärida key'd ja valuet.
arvud_nimed = dict(zip(arvud, nimed))

for k, v in arvud_nimed.items():
    if datetime.now().day == k:
        print("Vastama tuleb:", v)


nimekiri.close()