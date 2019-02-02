nimi = input("Sisestage Leedu perekonnanimi: ")


if nimi[-2:] == "ne":
    print("Abielus")
elif nimi[-2:] == "te":
    print("Vallaline")
elif nimi[-1:] == "e" and (nimi[-2:] != "ne" or nimi[-2:] != "te"):
    print("Määramata")
else:
    print("Pole ilmselt leedulanna perekonnanimi")
