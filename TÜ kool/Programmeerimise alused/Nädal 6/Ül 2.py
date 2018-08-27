kaugus = float(input("Sisestage kaugus: "))


def teleri_diagonaal(kaugus_m):
    tv_diag = kaugus_m*100*0.39/2.5
    return round(tv_diag)





print(teleri_diagonaal(kaugus))