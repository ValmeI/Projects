faili_nimi = input("Sisestage failinimi: ")
alam66t = int(input("Sisestage püügi alammõõt: "))
tysedusindeks_in = float(input("Sisestage Fultoni tüsedusindeks: "))
kalad = []


def kala_kaal(pikkus, tysedusindeks):

        kaal = pikkus**3 * tysedusindeks/100

        return round(kaal)


fail = open(faili_nimi, encoding="UTF-8")

for r in fail:
    r = int(r)

    if r < alam66t:
        print("Kala lasti vette tagasi")
    else:
        kaal_g = kala_kaal(r, tysedusindeks_in)
        print("Püütud kala kaaluga", kaal_g, "grammi")
        kalad.append(kaal_g) #list kalade arvutatud kaalust, et võtta sealt max

        k6ige_suurem_kg = max(kalad)/1000

print("Kõige raskem püütud kala:", round(k6ige_suurem_kg, 3) , "kg")



