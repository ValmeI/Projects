fail = open("konto.txt", encoding="UTF-8")

konto = []

for rida in fail:
    rida = rida.strip()
    rida = float(rida)
    if rida > 0:
        print(rida)
        konto.append(rida)


fail.close()

