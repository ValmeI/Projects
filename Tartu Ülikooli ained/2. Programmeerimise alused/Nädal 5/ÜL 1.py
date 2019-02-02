fail = open("mopeedid.txt", encoding="UTF-8")

mopeedid = []

for rida in fail:

   mopeedid.append(int(rida))

fail.close()


kuu = int(input("Palun sisestage mitmes kuu: "))
mopeeti = mopeedid[kuu-1]
print(kuu, "kuul registreeriti", mopeeti, "uut mopeedi.")