arv = int(input("Sisestage külaliste arv: "))

def tervitus(sisse_arv):
    print("Tänan", str(sisse_arv) + ".kord tervitada, mõtiskleb võõrustaja.")
    print('Külaline: "Tere, suur tänu kutse eest!"')
    print('Võõrustaja: "Tere!')


i = 1
while i <= arv:
    tervitus(i)
    i += 1




