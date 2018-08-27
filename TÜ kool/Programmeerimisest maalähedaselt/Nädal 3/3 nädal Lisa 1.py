supiTemp = int(input("Sisesta supi temperatuur: "))
toaTemp = int(input("Sisesta toa temperatuur: "))

while supiTemp >= 100:
    print("Supi temperatuur peab olema alla 100 kraadi.")
    supiTemp = int(input("Sisesta supi temperatuur: "))

while toaTemp <= 0:
    print("Toa temperatuur peab olema üle 0 kraadi.")
    toaTemp = int(input("Sisesta toa temperatuur: "))


Minutid = 0
Vahe = supiTemp-toaTemp


while Minutid != 10:

    JahtusKraadi = (Vahe * 0.19)
    supiTemp -= JahtusKraadi
    Vahe = supiTemp - toaTemp
    Minutid += 1

print("Supi temperatuur 10 minuti pärast:", round(supiTemp))










