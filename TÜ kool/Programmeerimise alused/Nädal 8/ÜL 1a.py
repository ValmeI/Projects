faili_nimi = input("Sisestage  failinimi: ")
pikad_lõimed = int(input("Sisestage 5-meetriste ja pikemate vaipidae lõimede arv: "))
lüh_lõimed = int(input("Sisestage lüheate vaipdate lõimede arv: "))

lõim = 0
kogu_pikkus = 0

def lõimede_pikkus(vaiba_lõpp_pikkus, lõimede_arv):
        lõime_kogu_pikkus = lõimede_arv * (vaiba_lõpp_pikkus * 1.2 + 0.5)
        lõime_kogu_pikkus = round(lõime_kogu_pikkus, 2)
        return lõime_kogu_pikkus


o_fail = open(faili_nimi, encoding="UTF-8")
for i in o_fail:
    i = float(i)
    if i >= 5:
        lõim = pikad_lõimed
        print(lõimede_pikkus(i, lõim))
        kogu_pikkus += lõimede_pikkus(i, lõim)
    else:
        lõim = lüh_lõimed
        print(lõimede_pikkus(i, lõim))
        kogu_pikkus += lõimede_pikkus(i, lõim)

print("Kõigi vaipade peale läheb vaja", round(kogu_pikkus, 2) , "meetrit lõimeniiti.")




