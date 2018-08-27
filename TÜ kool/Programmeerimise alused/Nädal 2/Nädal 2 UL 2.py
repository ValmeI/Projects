suurus = float(input("Sisesta kirja suurus: "))
pealkiri = input("Sisesta kirja teema pealkiri: ")
fail = input("Kas kirjaga on kaasas fail?: ")

if len(pealkiri) == 0 or (suurus > 1 and "jah" in fail.lower()):
    print("Kiri on spämm")
    print(pealkiri)
else:
    print("Kiri ei ole spämm")
