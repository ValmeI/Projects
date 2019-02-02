ostjate_arv = int(input("Sisestage ostjate arv: "))
kokku = 0


if ostjate_arv % 2 == 1:
    ostjate_arv = ostjate_arv
elif ostjate_arv % 2 == 0:
    ostjate_arv -= 1

uus_arv = ostjate_arv

for x in range(ostjate_arv):
        kokku += uus_arv
        uus_arv -= 2 # ei hakkaks lahutamist, kuna läheb miinusesse
        if uus_arv < 0:
            break

print("Lillede koguarv on ", str(kokku) + ".")
